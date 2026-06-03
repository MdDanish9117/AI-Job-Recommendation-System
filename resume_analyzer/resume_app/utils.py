import pdfplumber


skills_db = [
    'python',
    'django',
    'mysql',
    'html',
    'css',
    'javascript',
    'react',
    'api',
    'machine learning',
    'sql',
    'git',
    'github',
    'bootstrap',
    'django rest framework',
    'docker',
    'aws'
]


# Extract text
def extract_text_from_pdf(
    pdf_path
):

    text = ""

    with pdfplumber.open(
        pdf_path
    ) as pdf:

        for page in pdf.pages:

            page_text = (
                page.extract_text()
            )

            if page_text:

                text += (
                    page_text.lower()
                )

    return text


# Detect skills
def detect_skills(text):

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text:

            found_skills.append(
                skill
            )

    return found_skills


# Better score
def calculate_resume_score(
    skills
):

    total_skills = len(
        skills_db
    )

    matched = len(
        skills
    )

    score = int(
        (matched / total_skills)
        * 100
    )

    return score


# Recommendation system
def get_recommendation(
    skills
):

    missing_skills = []

    important_skills = [
        'python',
        'django',
        'api',
        'sql',
        'git'
    ]

    for skill in important_skills:

        if skill not in skills:

            missing_skills.append(
                skill
            )

    if len(
        missing_skills
    ) == 0:

        return (
            "Excellent Resume!"
        )

    return (
        "Recommended Skills: "
        + ", ".join(
            missing_skills
        )
    )