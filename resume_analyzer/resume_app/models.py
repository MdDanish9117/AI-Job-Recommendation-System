from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    resume_file = models.FileField(
        upload_to='resumes/'
    )

    extracted_text = models.TextField(
        blank=True,
        null=True
    )

    detected_skills = models.TextField(
        blank=True,
        null=True
    )

    resume_score = models.IntegerField(
        default=0
    )

    recommendation = models.TextField(
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} Resume"