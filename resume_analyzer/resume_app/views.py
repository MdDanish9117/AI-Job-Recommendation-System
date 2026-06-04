from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth import (
    login,
    logout
)

from django.contrib.auth.forms import (
    AuthenticationForm
)

from django.contrib.auth.decorators import (
    login_required
)

from django.http import (
    HttpResponse
)

from reportlab.pdfgen import canvas

from rest_framework import (
    viewsets,
    filters
)

from rest_framework.permissions import (
    IsAuthenticated
)

from .forms import (
    RegisterForm,
    ResumeUploadForm
)

from .models import Resume

from .serializers import (
    ResumeSerializer
)

from .utils import (
    extract_text_from_pdf,
    detect_skills,
    calculate_resume_score,
    get_recommendation
)


# ===================================
# REGISTER
# ===================================

def register_view(request):

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "login"
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )


# ===================================
# LOGIN
# ===================================

def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(
                request,
                user
            )

            return redirect(
                "dashboard"
            )

    else:

        form = AuthenticationForm()

    return render(
        request,
        "login.html",
        {
            "form": form
        }
    )


# ===================================
# DASHBOARD
# ===================================

@login_required
def dashboard(request):

    query = request.GET.get(
        "search"
    )

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by(
        "-uploaded_at"
    )

    if query:

        resumes = resumes.filter(
            detected_skills__icontains=query
        )

    return render(
        request,
        "dashboard.html",
        {
            "resumes": resumes
        }
    )


# ===================================
# UPLOAD RESUME
# ===================================

@login_required
def upload_resume(request):

    if request.method == "POST":

        form = ResumeUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            resume = form.save(
                commit=False
            )

            resume.user = (
                request.user
            )

            resume.save()

            extracted_text = (
                extract_text_from_pdf(
                    resume.resume_file.path
                )
            )

            skills = (
                detect_skills(
                    extracted_text
                )
            )

            score = (
                calculate_resume_score(
                    skills
                )
            )

            recommendation = (
                get_recommendation(
                    skills
                )
            )

            resume.extracted_text = (
                extracted_text
            )

            resume.detected_skills = (
                ", ".join(skills)
            )

            resume.resume_score = (
                score
            )

            resume.recommendation = (
                recommendation
            )

            resume.save()

            return redirect(
                "dashboard"
            )

    else:

        form = ResumeUploadForm()

    return render(
        request,
        "upload.html",
        {
            "form": form
        }
    )


# ===================================
# DOWNLOAD PDF
# ===================================

@login_required
def download_pdf(
    request,
    resume_id
):

    resume = (
        get_object_or_404(
            Resume,
            id=resume_id,
            user=request.user
        )
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = (
        'attachment; filename="resume_report.pdf"'
    )

    pdf = canvas.Canvas(
        response
    )

    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawString(
        150,
        800,
        "Resume Analysis Report"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        80,
        740,
        f"Username: {request.user.username}"
    )

    pdf.drawString(
        80,
        700,
        f"Skills: {resume.detected_skills}"
    )

    pdf.drawString(
        80,
        660,
        f"Resume Score: {resume.resume_score}%"
    )

    pdf.drawString(
        80,
        620,
        f"Recommendation: {resume.recommendation}"
    )

    pdf.save()

    return response


# ===================================
# DELETE RESUME
# ===================================

@login_required
def delete_resume(
    request,
    resume_id
):

    resume = (
        get_object_or_404(
            Resume,
            id=resume_id,
            user=request.user
        )
    )

    resume.delete()

    return redirect(
        "dashboard"
    )


# ===================================
# LOGOUT
# ===================================

def logout_view(request):

    logout(
        request
    )

    return redirect(
        "login"
    )


# ===================================
# API VIEWSET
# ===================================

class ResumeViewSet(
    viewsets.ModelViewSet
):

    serializer_class = (
        ResumeSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        "detected_skills",
        "recommendation"
    ]

    def get_queryset(self):

        return Resume.objects.filter(
            user=self.request.user
        ).order_by(
            "-uploaded_at"
        )

    def perform_create(
        self,
        serializer
    ):

        resume = serializer.save(
            user=self.request.user
        )

        extracted_text = (
            extract_text_from_pdf(
                resume.resume_file.path
            )
        )

        skills = (
            detect_skills(
                extracted_text
            )
        )

        score = (
            calculate_resume_score(
                skills
            )
        )

        recommendation = (
            get_recommendation(
                skills
            )
        )

        resume.extracted_text = (
            extracted_text
        )

        resume.detected_skills = (
            ", ".join(skills)
        )

        resume.resume_score = (
            score
        )

        resume.recommendation = (
            recommendation
        )

        resume.save()