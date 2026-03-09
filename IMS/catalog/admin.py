from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect
from .models import Component, User, Order, OrderItem

# Register your models here.
@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "quantity", "quick_quantity_actions", "rental_rate", "etan_rate_display", "location")
    readonly_fields = ("product_image_preview",)
    
    fieldsets = (
        (None, {
            "fields": (
                "product_image_preview", "product_image", "name", "category", 
                "quantity", "is_rentable", "rental_rate", "datasheet_url", 
                "description", "location"
            )
        }),
    )

    def product_image_preview(self, obj):
        if obj.product_image:
            return format_html('<img src="{}" style="max-height: 200px; margin-bottom: 10px;"/>', obj.product_image.url)
        return "No Image"
    product_image_preview.short_description = "Image Preview"

    def etan_rate_display(self, obj):
        return obj.etan_rate
    etan_rate_display.short_description = "E-Tan Rate"

    def quick_quantity_actions(self, obj):
        return format_html(
            '<a class="button" style="margin-right: 5px;" href="{}">+5</a>'
            '<a class="button" href="{}">-5</a>',
            f"{obj.pk}/add-qty/",
            f"{obj.pk}/sub-qty/"
        )
    quick_quantity_actions.short_description = "Quick Qty"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/add-qty/', self.admin_site.admin_view(self.add_qty_view), name='component-add-qty'),
            path('<int:pk>/sub-qty/', self.admin_site.admin_view(self.sub_qty_view), name='component-sub-qty'),
            path('barcode-scan/', self.admin_site.admin_view(self.barcode_scan_view), name='component-barcode-scan'),
        ]
        return custom_urls + urls

    def add_qty_view(self, request, pk):
        comp = Component.objects.get(pk=pk)
        comp.quantity += 5
        comp.save()
        return redirect('..')

    def sub_qty_view(self, request, pk):
        comp = Component.objects.get(pk=pk)
        comp.quantity -= 5
        comp.save()
        return redirect('..')

    def barcode_scan_view(self, request):
        if request.method == 'POST':
            barcode = request.POST.get('barcode', '').strip()
            if barcode:
                if '-' in barcode:
                    cat, name = barcode.split('-', 1)
                    valid_cats = [choice[0] for choice in Component.Category.choices]
                    cat_final = cat if cat in valid_cats else Component.Category.MISC
                    
                    component, created = Component.objects.get_or_create(
                        name=name,
                        defaults={'category': cat_final, 'quantity': 1}
                    )
                    
                    if not created:
                        component.quantity += 1
                        component.save()
                        self.message_user(request, f"Incremented quantity of {name} to {component.quantity}", level=messages.SUCCESS)
                    else:
                        self.message_user(request, f"Successfully added {cat}-{name}", level=messages.SUCCESS)
                else:
                    self.message_user(request, "Invalid barcode format. Expected <cat>-<name>", level=messages.ERROR)
            else:
                self.message_user(request, "Empty barcode submitted.", level=messages.WARNING)
                
        return redirect('..')


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "pid", "role", "is_member")
    list_filter = ("role", "is_member")
    fieldsets = BaseUserAdmin.fieldsets + (
        ("E-Tan Fields", {"fields": ("pid", "role", "phone_number", "is_member")}),
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("user__username", "user__email")
    inlines = [OrderItemInline]