import PyPDF2


# ==========================
# PDF TEXT EXTRACTION
# ==========================

def extract_text_from_pdf(
    pdf_path
):

    text = ""

    try:

        with open(
            pdf_path,
            'rb'
        ) as file:

            reader = PyPDF2.PdfReader(
                file
            )

            for page in reader.pages:

                page_text = (
                    page.extract_text()
                )

                if page_text:

                    text += page_text

    except Exception as e:

        print(
            "PDF Error:",
            e
        )

    return text


# ==========================
# SKILL DETECTION
# ==========================

def detect_skills(
    text
):

    skills_database = [

        'python',
        'java',
        'c++',
        'django',
        'flask',
        'html',
        'css',
        'javascript',
        'react',
        'nodejs',
        'sql',
        'mysql',
        'mongodb',
        'machine learning',
        'data science',
        'ai',
        'git',
        'github',
        'api',
        'rest api',
        'bootstrap'
    ]

    detected = []

    text = text.lower()

    for skill in skills_database:

        if skill.lower() in text:

            detected.append(
                skill
            )

    return detected


# ==========================
# RESUME SCORE
# ==========================

def calculate_resume_score(
    skills
):

    total_skills = len(
        skills
    )

    score = total_skills * 10

    if score > 100:
        score = 100

    return score


# ==========================
# JOB RECOMMENDATION
# ==========================

def get_recommendation(
    skills
):

    skills = [
        skill.lower()
        for skill in skills
    ]

    if (
        'django' in skills
        or 'python' in skills
    ):
        return (
            "Backend Developer"
        )

    elif (
        'react' in skills
        or 'javascript' in skills
    ):
        return (
            "Frontend Developer"
        )

    elif (
        'machine learning'
        in skills
        or 'ai' in skills
    ):
        return (
            "AI/ML Engineer"
        )

    elif (
        'sql' in skills
        or 'mongodb'
        in skills
    ):
        return (
            "Database Developer"
        )

    return (
        "Software Developer"
    )