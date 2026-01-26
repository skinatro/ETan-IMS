from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Component, User

# Register your models here.
admin.site.register(Component)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "pid", "role", "is_member")
    list_filter = ("role", "is_member")
    fieldsets = BaseUserAdmin.fieldsets + (
        ("E-Tan Fields", {"fields": ("pid", "role", "phone_number", "is_member")}),
    )