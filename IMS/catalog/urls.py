from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="catalog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Dashboard
    path("", views.dashboard, name="dashboard"),

    # Inventory
    path("inventory/", views.inventory_list, name="inventory_list"),
    path("inventory/<int:pk>/", views.component_detail, name="component_detail"),
    path("inventory/add/", views.component_create, name="component_create"),
    path("inventory/<int:pk>/edit/", views.component_edit, name="component_edit"),

    # Orders
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
    path("orders/new/<int:component_pk>/", views.order_create, name="order_create"),
    path("orders/<int:pk>/accept/", views.order_accept, name="order_accept"),
    path("orders/<int:pk>/reject/", views.order_reject, name="order_reject"),
    path("orders/<int:pk>/cancel/", views.order_cancel, name="order_cancel"),
]
