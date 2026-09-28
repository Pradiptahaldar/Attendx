from django.db import models
from organizations.models import Organization, Department

class Subject(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="subjects",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subjects",
    )
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="unique_subject_code_per_organization",
            ),
            models.UniqueConstraint(
                fields=["organization", "name"],
                name="unique_subject_name_per_organization",
            ),
        ]
    def __str__(self):
        return f"{self.name} ({self.code})"