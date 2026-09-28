from django.db import models
from organizations.models import Organization, AcademicSession, Section
from subjects.models import Subject
from teachers.models import Teacher

class CourseAssignment(models.Model):
    class AssignmentType(models.TextChoices):
        THEORY = "THEORY", "Theory"
        LAB = "LAB", "Lab"
        PRACTICAL = "PRACTICAL", "Practical"
        OTHER = "OTHER", "Other"
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="course_assignments",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="course_assignments",
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="course_assignments",
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="course_assignments",
    )
    academic_session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE,
        related_name="course_assignments",
    )
    assignment_type = models.CharField(
        max_length=20,
        choices=AssignmentType.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "organization",
                    "subject",
                    "teacher",
                    "section",
                    "academic_session",
                    "assignment_type",
                ],
                name="unique_course_assignment",
            ),
        ]
    def __str__(self):
        return f"{self.subject.name} - {self.teacher.full_name} - {self.section.name}"