print("Welcome to AI Resume Analyzer")

resume = input("Paste your resume text here: ").lower()

job_skills = ["python", "java", "machine learning", "cloud", "sql"]

matched_skills = []

for skill in job_skills:
    if skill in resume:
        matched_skills.append(skill)

score = (len(matched_skills) / len(job_skills)) * 100

print("\nMatched Skills:", matched_skills)
print("Resume Score:", score, "%")

