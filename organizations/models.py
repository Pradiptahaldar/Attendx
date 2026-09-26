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

class Department(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="departments",
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
                name="unique_department_code_per_organization",
            ),
            models.UniqueConstraint(
                fields=["organization", "name"],
                name="unique_department_name_per_organization",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"

class AcademicSession(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="academic_sessions",
    )
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "name"],
                name="unique_academic_session_per_organization",
            ),
            models.CheckConstraint(
                condition=models.Q(end_date__gt=models.F("start_date")),
                name="academic_session_end_after_start",
            ),
        ]
    def __str__(self):
        return f"{self.name} - {self.organization.name}"
class Section(models.Model):
    class StudyYear(models.TextChoices):
        FIRST_YEAR = "FIRST_YEAR", "First Year"
        SECOND_YEAR = "SECOND_YEAR", "Second Year"
        THIRD_YEAR = "THIRD_YEAR", "Third Year"
        FOURTH_YEAR = "FOURTH_YEAR", "Fourth Year"

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sections",
    )
    academic_session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    study_year = models.CharField(
        max_length=20,
        choices=StudyYear.choices,
    )
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "organization",
                    "department",
                    "academic_session",
                    "study_year",
                    "name",
                ],
                name="unique_section_per_academic_context",
            ),
        ]
    def __str__(self):
        return f"{self.name} - {self.get_study_year_display()}"