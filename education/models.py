from django.db import models
from datetime import date


class Education(models.Model):
    institution_name = models.CharField(
        max_length=255,
        verbose_name="Institution Name",
        help_text="Name of the educational institution"
    )
    degree = models.CharField(
        max_length=255,
        verbose_name="Degree",
        help_text="Name of the degree or qualification earned"
    )
    field_of_study = models.CharField(
        max_length=255,
        verbose_name="Field of Study",
        help_text="Field of study or major",
        blank=True
    )
    start_date = models.DateField(
        verbose_name="Start Date",
        help_text="When you started this education",
        blank=True,
        null=True
    )
    end_date = models.DateField(
        verbose_name="End Date",
        help_text="When you completed this education (leave blank if ongoing)",
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Additional information about your studies, projects, or achievements",
        blank=True
    ),
    point = models.FloatField(
        verbose_name="Point",
        help_text="Your point",
        blank=True,
        null=True
    )
    grade = models.CharField(
        max_length=10,
        verbose_name="Grade",
        help_text="Your final grade or GPA (optional)",
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date Updated"
    )

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"

    from datetime import date

    def get_duration(self):
        """Calculate the duration from start_date to end_date (or to today if ongoing) and return as years, months, and weeks."""
        # Check if start_date is provided
        if not self.start_date:
            return "No start date provided"
        end_date = self.end_date or date.today()
        delta = end_date - self.start_date

        years = delta.days // 365
        remaining_days_after_years = delta.days % 365

        months = remaining_days_after_years // 30
        remaining_days_after_months = remaining_days_after_years % 30

        weeks = remaining_days_after_months // 7

        # Build the duration string
        duration = []
        if years > 0:
            duration.append(f"{years} years")
        if months > 0:
            duration.append(f"{months} months")
        if weeks > 0:
            duration.append(f"{weeks} weeks")

        return ", ".join(duration) if duration else "Less than a week"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
