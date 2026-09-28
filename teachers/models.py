from django.db import models
from organizations.models import Organization, Department

class Teacher(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="teachers",
    )
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        blank=True,
    )
    employee_id = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="teachers",
    )
    profile_photo = models.CharField(
        max_length=255,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "employee_id"],
                name="unique_employee_id_per_organization",
            ),
        ]
    def __str__(self):
        return f"{self.employee_id} - {self.full_name}"