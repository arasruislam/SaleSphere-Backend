from django.db import models
from django.contrib.auth.models import User

# Constant
ROLE_CHOICES = [
    ("cashier", "Cashier"),
    ("manager", "Manager"),
]


# Admin Model
class AdminModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin")
    is_admin = models.BooleanField(default=True)
    profile_img = models.ImageField(upload_to="accounts/images", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Admins"

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name} "


# Staff Model
class Staff(models.Model):
    admin = models.ForeignKey(
        AdminModel, on_delete=models.CASCADE, related_name="staff_members"
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="staff_profile"
    )
    profile_img = models.ImageField(
        upload_to="accounts/images", null=True, blank=True, verbose_name="Profile Image"
    )
    phone = models.CharField(
        max_length=16,
        verbose_name="Phone Number",
        help_text="Enter phone number with country code",
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Salary",
        help_text="Enter monthly salary",
    )
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="cashier", verbose_name="Job Role"
    )
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    address = models.CharField(
        max_length=300, verbose_name="Address", help_text="Enter full address"
    )
    additional_info = models.TextField(
        null=True,
        blank=True,
        verbose_name="Additional Information",
        help_text="Optional additional information",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff Members"
        ordering = ["user__first_name"]  # Orders staff by first name by default

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role.capitalize()}"
