from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Component, User, Order, OrderItem

# Register your models here.
admin.site.register(Component)


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