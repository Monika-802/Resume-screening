
from chains.pipeline import run_pipeline

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

jd = load_file("data/job_description.txt")

resumes = {
    "Strong": load_file("data/resume_strong.txt"),
    "Average": load_file("data/resume_avg.txt"),
    "Weak": load_file("data/resume_weak.txt")
}

for label, resume in resumes.items():
    result = run_pipeline(resume, jd)
    print("\n", "="*50)
    print(label)
    print(result)