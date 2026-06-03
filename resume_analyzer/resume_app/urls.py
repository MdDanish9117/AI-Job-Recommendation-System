from django.urls import path
from . import views


urlpatterns = [

    # Register Page
    path(
        '',
        views.register_view,
        name='register'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    # Login Page
    path(
        'login/',
        views.login_view,
        name='login'
    ),

    # Dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # Upload Resume
    path(
        'upload/',
        views.upload_resume,
        name='upload'
    ),

    # Logout
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # PDF Download
    path(
        'download/<int:resume_id>/',
        views.download_pdf,
        name='download_pdf'
    ),

    # Delete Resume
    path(
        'delete/<int:resume_id>/',
        views.delete_resume,
        name='delete_resume'
    ),
]