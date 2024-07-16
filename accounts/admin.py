from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_from = UserCreationForm

    fieldsets = (
        (
            None,
            {
                "fields": ("username", "email", "full_name", "password"),
            },
        ),
        (
            "permissions",
            {"fields": ("is_active", "is_admin", "last_login")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("username", "email", "full_name", "password1", "password2"),
            },
        ),
        (
            "permissions",
            {"fields": ("is_active", "is_admin", "last_login")},
        ),
    )
    ordering = (
        "email",
        "phone_number",
    )
    search_fields = ("username", "email", "full_name")
    list_filter = ("is_admin", "is_active")
    list_display = ("username", "email", "full_name", "is_staff")
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
