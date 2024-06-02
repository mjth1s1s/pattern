import pandas as pd

# 원본 데이터셋
original_data = [
    {"직무": "소프트웨어 엔지니어", "요구 기술": ["Java", "Spring", "MySQL", "Git"], "급여 범위": "연봉 4,000만 원 ~ 6,000만 원"},
    {"직무": "데이터 분석가", "요구 기술": ["Python", "R", "SQL", "Tableau"], "급여 범위": "연봉 3,500만 원 ~ 5,500만 원"},
    {"직무": "웹 개발자", "요구 기술": ["HTML", "CSS", "JavaScript", "React"], "급여 범위": "연봉 3,000만 원 ~ 4,500만 원"},
    {"직무": "UX/UI 디자이너", "요구 기술": ["Sketch", "Figma", "Adobe XD", "Photoshop"], "급여 범위": "연봉 3,800만 원 ~ 5,200만 원"},
    {"직무": "프로젝트 매니저", "요구 기술": ["프로젝트 관리", "Agile", "Scrum", "MS Project"], "급여 범위": "연봉 5,000만 원 ~ 7,000만 원"},
    {"직무": "데브옵스 엔지니어", "요구 기술": ["AWS", "Docker", "Kubernetes", "CI/CD"], "급여 범위": "연봉 4,500만 원 ~ 6,500만 원"},
    {"직무": "네트워크 관리자", "요구 기술": ["Cisco", "Juniper", "LAN/WAN", "Network Security"], "급여 범위": "연봉 4,200만 원 ~ 6,200만 원"},
    {"직무": "모바일 앱 개발자", "요구 기술": ["Swift", "Kotlin", "iOS", "Android"], "급여 범위": "연봉 3,800만 원 ~ 5,500만 원"}
]

# 원본 데이터를 바탕으로 유사한 데이터를 추가 생성
additional_data = []
for i in range(50):  # 50개의 추가 데이터 셋을 생성하여 총 400개 이상 데이터 생성
    for job in original_data:
        new_job = job.copy()
        new_job["직무"] = job["직무"]
        new_job["요구 기술"] = job["요구 기술"][:]
        new_job["급여 범위"] = job["급여 범위"]
        additional_data.append(new_job)

data = original_data + additional_data

# 데이터를 DataFrame으로 변환
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('pattern.csv', index=False)
