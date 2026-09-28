from django.db import models
from organizations.models import Organization, Department, AcademicSession, Section

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

class StudentEnrollment(models.Model):
    class StudyYear(models.TextChoices):
        FIRST_YEAR = "FIRST_YEAR", "First Year"
        SECOND_YEAR = "SECOND_YEAR", "Second Year"
        THIRD_YEAR = "THIRD_YEAR", "Third Year"
        FOURTH_YEAR = "FOURTH_YEAR", "Fourth Year"
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    academic_session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE,
        related_name="student_enrollments",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="student_enrollments",
    )
    study_year = models.CharField(
        max_length=20,
        choices=StudyYear.choices,
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="student_enrollments",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.student.full_name} - {self.academic_session.name}"