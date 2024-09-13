from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AdminModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=True)
    profile_img = models.ImageField(upload_to="accounts/images", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Admins"

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name} "

