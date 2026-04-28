import sqlite3
import pandas as pd
import json

# 데이터 로드
conn = sqlite3.connect('data/nemo_stores.db')
df = pd.read_sql('SELECT * FROM stores', conn)
conn.close()

# 섹션별 분석 데이터 및 인사이트
sections = [
    {"id": "premium", "title": "업종별 권리금 분포", "img": "images/premium_by_industry.png", "insight": "일반음식점과 주류점의 이상치(Outlier)는 시설/바닥 권리금이 복합적으로 작용함을 보여줍니다. 창업자에게는 초기 투자비 회수 가능성을 판단하는 핵심 지표입니다.", "interp": "박스플롯을 통해 각 업종의 중앙값과 이상치를 확인하십시오. 중앙값이 낮고 이상치가 많은 업종은 진입 장벽이 낮으나 성공 시 수익성이 높은 '고위험-고수익' 구조를 띠고 있습니다."},
    {"id": "size", "title": "면적-임대료 효율", "img": "images/size_rent_efficiency.png", "insight": "소형 평수(50㎡ 미만) 매물에서 가격 편차가 심합니다. 이는 면적보다 초역세권 등 입지 조건이 가격 결정력을 압도함을 의미합니다.", "interp": "산점도 회귀선에서 크게 벗어난 매물들은 면적 효율이 떨어지거나 입지 가치가 과대평가된 매물이므로 꼼꼼한 비교 분석이 필요합니다."},
    {"id": "floor", "title": "층별 임대료 및 권리금 추이", "img": "images/floor_premium_trend.png", "insight": "1층이 시장을 주도하나, 고층부로 갈수록 권리금이 급격히 하락합니다. 마케팅 의존도가 높은 사업은 고층부 가성비 입지가 생존율을 높입니다.", "interp": "단위 면적당 임대료를 비교하십시오. 1층의 광고 효과와 고층부의 비용 절감 효과를 사업 모델의 성격(로드샵 vs 목적형)에 맞춰 대조해 보는 것이 핵심입니다."}
]

# HTML 생성
html = f"""
<!DOCTYPE html><html lang='ko'><head><meta charset='UTF-8'>
<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
<style>
    body {{ background: #f8f9fa; }}
    .card {{ border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.08); margin-bottom: 30px; }}
    .insight {{ background: #f8f9fa; border-left: 4px solid #0d6efd; padding: 15px; }}
</style>
</head><body><div class='container py-5'>
    <h1 class='mb-5'>상가 매물 전략적 EDA 분석 리포트</h1>
    {"".join([f'''
    <div class='card p-4'>
        <h3>{s['title']}</h3>
        <div class='row'><div class='col-lg-6'><img src='{s['img']}' class='img-fluid rounded'></div>
        <div class='col-lg-6'><div class='insight'>
            <p><strong>💡 Biz Insight:</strong> {s['insight']}</p>
            <p class='text-primary'><strong>🔍 해석 방법:</strong> {s['interp']}</p>
        </div></div></div>
    </div>''' for s in sections])}
</div></body></html>
"""
with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
