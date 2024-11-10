from django.db import models
from datetime import date
# Create your models here.
class Experience(models.Model):
    company_name = models.CharField(
        max_length=255,
        verbose_name="Company Name",
        help_text="Name of the company where you worked"
    )
    job_title = models.CharField(
        max_length=255,
        verbose_name="Job Title",
        help_text="Your job title at the company"
    )
    start_date = models.DateField(
        verbose_name="Start Date",
        help_text="The date you started working at the company"
    )
    end_date = models.DateField(
        verbose_name="End Date",
        help_text="The date you stopped working at the company",
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="A brief description of your responsibilities and achievements"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Created",
        help_text="When the experience entry was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date Updated",
        help_text="When the experience entry was last updated"
    )

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
    # def get_duration(self):
    #     """Calculate the duration from start_date to end_date (or to today if ongoing) and return as years and months."""
    #     end_date = self.end_date or date.today()
    #     delta = end_date - self.start_date

    #     years = delta.days // 365
    #     months = (delta.days % 365) // 30

    #     if years > 0 and months > 0:
    #         return f"{years} years, {months} months"
    #     elif years > 0:
    #         return f"{years} years"
    #     else:
    #         return f"{months} months"
    def get_duration(self):
        """Calculate the duration from start_date to end_date (or to today if ongoing) and return as years, months, and weeks."""
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
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"