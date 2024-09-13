from django.contrib import admin
from .models import AdminModel


# Register your models here.
class AdminPanel(admin.ModelAdmin):
    list_display = ["full_name", "username", "is_admin", "profile_img"]

    def full_name(self, obj):
        return obj.user.get_full_name()

    def username(self, obj):
        return obj.user.username


admin.site.register(AdminModel, AdminPanel)
