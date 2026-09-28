from django.db import models
from organizations.models import Organization

class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        OTHER = "OTHER", "Other"
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="students",
    )
    student_id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(
        blank=True,
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        blank=True,
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
                fields=["organization", "student_id"],
                name="unique_student_id_per_organization",
            ),
        ]
    def __str__(self):
        return f"{self.student_id} - {self.full_name}"