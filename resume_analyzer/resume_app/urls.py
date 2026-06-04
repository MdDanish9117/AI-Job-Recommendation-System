from django.urls import (
    path,
    include
)

from rest_framework.routers import (
    DefaultRouter
)

from . import views
from .views import (
    ResumeViewSet
)


router = DefaultRouter()

router.register(
    r"resumes",
    ResumeViewSet,
    basename="resume"
)


urlpatterns = [

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

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'upload/',
        views.upload_resume,
        name='upload'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'download-pdf/<int:resume_id>/',
        views.download_pdf,
        name='download_pdf'
    ),

    path(
        'delete-resume/<int:resume_id>/',
        views.delete_resume,
        name='delete_resume'
    ),

    # API
    path(
        'api/',
        include(
            router.urls
        )
    ),
]