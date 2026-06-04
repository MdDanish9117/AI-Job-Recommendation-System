from django.contrib import admin
from .models import Resume


@admin.register(Resume)
class ResumeAdmin(
    admin.ModelAdmin
):

    list_display = [
        'id',
        'user',
        'resume_score',
        'recommendation',
        'uploaded_at'
    ]

    search_fields = [
        'user__username',
        'detected_skills'
    ]