from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseForbidden

from .models import Component, Order, OrderItem, User
from .forms import CustomerRegistrationForm, ComponentForm, OrderItemForm


def register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomerRegistrationForm()
    return render(request, "catalog/register.html", {"form": form})


@login_required
def dashboard(request):
    user = request.user
    if user.role == "admin":
        recent_orders = Order.objects.select_related("user").order_by("-created_at")[:10]
        borrowed_count = Order.objects.filter(status="accepted").count()
        return render(request, "catalog/admin_dashboard.html", {
            "recent_orders": recent_orders,
            "borrowed_count": borrowed_count,
        })
    else:
        orders = Order.objects.filter(user=user).order_by("-created_at")
        return render(request, "catalog/customer_dashboard.html", {
            "orders": orders,
        })


def inventory_list(request):
    components = Component.objects.all()
    show_all = request.GET.get("show_all", False)
    if not show_all:
        components = components.filter(is_rentable=True, quantity__gt=0)
    return render(request, "catalog/inventory_list.html", {
        "components": components,
        "show_all": show_all,
    })


@login_required
def component_detail(request, pk):
    component = get_object_or_404(Component, pk=pk)
    return render(request, "catalog/component_detail.html", {
        "component": component,
    })


@login_required
def component_create(request):
    if request.user.role != "admin":
        return HttpResponseForbidden("Admin access required.")
    if request.method == "POST":
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("inventory_list")
    else:
        form = ComponentForm()
    return render(request, "catalog/component_form.html", {"form": form})


@login_required
def component_edit(request, pk):
    if request.user.role != "admin":
        return HttpResponseForbidden("Admin access required.")
    component = get_object_or_404(Component, pk=pk)
    if request.method == "POST":
        form = ComponentForm(request.POST, request.FILES, instance=component)
        if form.is_valid():
            form.save()
            return redirect("component_detail", pk=pk)
    else:
        form = ComponentForm(instance=component)
    return render(request, "catalog/component_form.html", {"form": form, "edit": True})


@login_required
def order_create(request, component_pk):
    component = get_object_or_404(Component, pk=component_pk)
    if request.method == "POST":
        form = OrderItemForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data["quantity"]
            order = Order.objects.create(user=request.user)
            OrderItem.objects.create(order=order, component=component, quantity=qty)
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderItemForm(initial={"component": component, "quantity": 1})
    return render(request, "catalog/order_create.html", {
        "form": form,
        "component": component,
    })


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.user != request.user and request.user.role != "admin":
        return HttpResponseForbidden("Access denied.")
    items = order.items.select_related("component").all()
    return render(request, "catalog/order_detail.html", {
        "order": order,
        "items": items,
    })


@login_required
def order_list(request):
    if request.user.role == "admin":
        orders = Order.objects.select_related("user").order_by("-created_at")
    else:
        orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "catalog/order_list.html", {"orders": orders})


@login_required
def order_accept(request, pk):
    if request.user.role != "admin":
        return HttpResponseForbidden("Admin access required.")
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.Status.ACCEPTED
    order.decided_at = timezone.now()
    order.save()
    return redirect("order_detail", pk=pk)


@login_required
def order_reject(request, pk):
    if request.user.role != "admin":
        return HttpResponseForbidden("Admin access required.")
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.Status.REJECTED
    order.decided_at = timezone.now()
    order.save()
    return redirect("order_detail", pk=pk)


@login_required
def order_cancel(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.user != request.user:
        return HttpResponseForbidden("You can only cancel your own orders.")
    order.status = Order.Status.CANCELLED
    order.save()
    return redirect("order_detail", pk=pk)
