import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import json

conn = sqlite3.connect('data/nemo_stores.db')
df = pd.read_sql('SELECT * FROM stores', conn)
conn.close()

# 키워드 추출
texts = df['title'].fillna('').tolist()
tfidf = TfidfVectorizer(max_features=10).fit(texts)
keywords = sorted(tfidf.get_feature_names_out())

# 섹션 구성
sections = [
    {"icon": "briefcase", "title": "업종 분석", "items": [
        {"img": "images/top_business_large.png", "title": "전체 업종 분포", "text": "검증된 모델을 파악해 틈새 전략을 세우세요."},
        {"img": "images/dist_1.png", "title": "지역별 업종 분포", "text": "역세권 우위 기반의 전략적 포지셔닝이 필수입니다."}
    ]},
    {"icon": "map", "title": "상권 밀집도", "items": [
        {"img": "images/hist_0.png", "title": "보증금 분포", "text": "중앙값 2,000만원이 핵심 진입 장벽입니다."},
        {"img": "images/hist_1.png", "title": "월세 분포", "text": "100~150만원 구간의 공실 방어 전략을 적용하세요."}
    ]},
    {"icon": "map-pin", "title": "입지/트렌드", "items": [
        {"img": "images/corr.png", "title": "가격 상관관계", "text": "보증금-월세 상관관계를 이용해 협상력을 확보하세요."},
        {"img": "images/floor_premium_trend.png", "title": "층별 트렌드", "text": "고층부 가성비 입지가 생존율을 높입니다."}
    ]}
]

# HTML 생성 (아이템 내부 가로 정렬 추가)
items_html = ""
for g in sections:
    items_html += f"<div class='glass p-6 mb-8'><h2 class='text-2xl font-bold mb-6 flex items-center gap-3'><i data-lucide='{g['icon']}'></i>{g['title']}</h2><div class='grid grid-cols-1 gap-6'>"
    for i in g['items']:
        items_html += f"<div class='bg-slate-900/50 p-4 rounded-lg flex items-center gap-6'><img src='{i['img']}' class='w-1/3 rounded'><div class='w-2/3'><h4 class='text-sky-300 font-bold mb-2'>{i['title']}</h4><p class='text-sm'>{i['text']}</p></div></div>"
    items_html += "</div></div>"

html = f"""
<!DOCTYPE html><html lang='ko'><head><script src='https://cdn.tailwindcss.com'></script><script src='https://unpkg.com/lucide@latest'></script>
<style>body{{background:#0f172a;color:#f1f5f9;}} .glass{{background:rgba(30,41,59,0.7);backdrop-filter:blur(12px);border-radius:1rem;}}</style>
</head><body class='p-8'><div class='max-w-7xl mx-auto'>
    <h1 class='text-4xl font-bold text-sky-400 mb-8'>종합 상가 데이터 대시보드</h1>
    {items_html}
    <div class='glass p-8'><h2 class='text-2xl font-bold mb-6'>핵심 키워드 TOP 10</h2>
        <div class='flex flex-wrap gap-3'>{"".join([f"<span class='bg-sky-900 text-sky-200 px-4 py-2 rounded-full text-sm font-bold border border-sky-700'>{k}</span>" for k in keywords])}</div>
    </div>
    <script>lucide.createIcons();</script>
</div></body></html>
"""
with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
