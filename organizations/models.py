from django.db import models

class Organization(models.Model):
    class OrganizationType(models.TextChoices):
        SCHOOL = "SCHOOL", "School"
        COLLEGE = "COLLEGE", "College"
        COACHING = "COACHING", "Coaching"
        COMPANY = "COMPANY", "Company"
        OTHER = "OTHER", "Other"
    name = models.CharField(max_length=150)
    type = models.CharField(
        max_length=20,
        choices=OrganizationType.choices,
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        blank=True,
    )
    address = models.TextField()
    logo = models.CharField(
        max_length=255,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name