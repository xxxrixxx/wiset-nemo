import sqlite3
import pandas as pd
import json

# 1. 데이터 로드
conn = sqlite3.connect('data/nemo_stores.db')
df = pd.read_sql('SELECT * FROM stores', conn)
conn.close()

# 2. 통계 가공
stats = {
    "deposit": {"mean": 28898, "median": 20000, "labels": ["0-1억", "1억-2억", "2억이상"], "values": [df[df['deposit']<100000].shape[0], df[(df['deposit']>=100000)&(df['deposit']<200000)].shape[0], df[df['deposit']>=200000].shape[0]]},
    "rent": {"mean": 1940, "median": 1400, "labels": ["0-100만", "100-200만", "200만이상"], "values": [df[df['monthlyRent']<100].shape[0], df[(df['monthlyRent']>=100)&(df['monthlyRent']<200)].shape[0], df[df['monthlyRent']>=200].shape[0]]}
}

# 3. 인사이트 (리포트 내용 반영)
content = {
    "deposit": {"insight": "보증금은 중앙값 2,000만원을 기준으로 시장의 핵심 진입 장벽이 형성되어 있습니다. 예비 창업자의 70%가 이 구간에 집중되어 있어, 중개 전략 수립 시 2,000만원 내외 매물 확보가 공실 리스크 방어의 핵심입니다.", "interp": "보증금 데이터의 롱테일 분포는 극단적 고가 매물에 의한 평균의 왜곡을 보여줍니다. 따라서 25%~75% 분위수(1,000~3,000만원)를 중심으로 시장을 해석하는 것이 통계적으로 유의미합니다."},
    "rent": {"insight": "월세 100~150만원 구간이 가장 빈번합니다. 전체의 75%가 222만원 이하로, 소규모 자영업자 타겟팅이 시장의 주류를 이룹니다. 500만원 이상 고가 매물은 브랜드 홍보가 중요한 역세권 메인 대로변에 집중되어 있습니다.", "interp": "월세의 표준편차가 1,997에 달한다는 것은 매물 간의 입지적 가치 격차가 매우 큼을 의미합니다. 단순히 평균 월세를 기준으로 삼지 말고, 업종별/층별 세분화된 임대료 기준을 적용해야 합니다."},
    "report": "본 분석 리포트는 총 387개 매물을 대상으로 상권의 자본 투입과 입지 효율성을 입체적으로 진단하였습니다. 특히 보증금-월세 간 0.89의 강력한 상관관계는 시장 가격 결정 기제가 매우 안정적으로 작동하고 있음을 증명합니다. 창업 전략 수립 시 1층 중심의 고비용 구조를 탈피하여, 2층 이상에서의 가성비 전략이 생존율을 높이는 핵심 동력이 될 수 있음을 시사합니다."
}

# 4. HTML 생성
html = f"""
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script></head>
<body class="bg-light"><div class="container py-4">
    <h2 class="mb-4">상가 매물 심층 분석 대시보드</h2>
    <div class="row">
        <div class="col-md-6"><div class="card p-3 shadow-sm"><h5>보증금 분석</h5><canvas id="dChart"></canvas><div class="mt-2 text-muted small">{content['deposit']['insight']}</div><div class="mt-1 text-primary small">해석: {content['deposit']['interp']}</div></div></div>
        <div class="col-md-6"><div class="card p-3 shadow-sm"><h5>월세 분석</h5><canvas id="rChart"></canvas><div class="mt-2 text-muted small">{content['rent']['insight']}</div><div class="mt-1 text-primary small">해석: {content['rent']['interp']}</div></div></div>
    </div>
    <div class="card mt-4 p-4 shadow-sm"><h5>종합 인사이트</h5><p>{content['report']}</p></div>
</div>
<script>
    new Chart(document.getElementById('dChart'), {{ type: 'pie', data: {{ labels: {json.dumps(stats['deposit']['labels'])}, datasets: [{{ data: {stats['deposit']['values']} }}] }} }});
    new Chart(document.getElementById('rChart'), {{ type: 'pie', data: {{ labels: {json.dumps(stats['rent']['labels'])}, datasets: [{{ data: {stats['rent']['values']} }}] }} }});
</script></body></html>
"""
with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
