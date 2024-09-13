from django.contrib import admin
from .models import AdminModel, Staff


# Register your models here.
class AdminPanel(admin.ModelAdmin):
    list_display = ["full_name", "username", "is_admin", "profile_img"]

    def full_name(self, obj):
        return obj.user.get_full_name()

    def username(self, obj):
        return obj.user.username


# staff admin
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        "user_full_name",
        "role",
        "phone",
        "salary",
        "date_of_birth",
        "admin_full_name",
    ]
    search_fields = [
        "user__first_name",
        "user__last_name",
        "user__email",
        "phone",
        "role",
    ]
    list_filter = ["role", "admin__user__first_name"]

    def user_full_name(self, obj):
        return obj.user.get_full_name()

    user_full_name.short_description = "Staff Full Name"

    def admin_full_name(self, obj):
        return obj.admin.user.get_full_name()

    admin_full_name.short_description = "Admin Full Name"


admin.site.register(AdminModel, AdminPanel)
admin.site.register(Staff, StaffAdmin)
