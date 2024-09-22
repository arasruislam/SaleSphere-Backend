from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"list", views.AdminApiView)
router.register(r"staff", views.StaffApiView, basename="staff")


urlpatterns = [
    path("", include(router.urls)),

]
