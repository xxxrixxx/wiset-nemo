import sqlite3
import pandas as pd
import json

conn = sqlite3.connect('data/nemo_stores.db')
df = pd.read_sql('SELECT * FROM stores', conn)
conn.close()

# KPI 데이터
kpi = [("전체 매물", f"{len(df):,}건"), ("평균 보증금", f"{int(df['deposit'].mean()):,}만"), ("평균 월세", f"{int(df['monthlyRent'].mean()):,}만"), ("평균 면적", f"{round(df['size'].mean(), 1)}㎡"), ("최다 업종", df['businessLargeCodeName'].mode()[0])]

# 전체 분석 섹션 (누락된 섹션 복구)
sections = [
    {"icon": "briefcase", "title": "업종 분석", "items": [
        {"img": "images/top_business_large.png", "title": "업종별 분포", "text": "검증된 비즈니스 모델을 파악하여 틈새 전략을 세우세요."},
        {"img": "images/region_industry_stacked.png", "title": "지역별 업종 분포", "text": "역세권의 F&B 우위를 기반으로 한 입지 포지셔닝이 필수입니다."}
    ]},
    {"icon": "dollar-sign", "title": "비용 및 효율성", "items": [
        {"img": "images/premium_by_industry.png", "title": "업종별 권리금", "text": "시설/영업가치가 반영된 권리금을 통해 투자 회수 전략을 수립하세요."},
        {"img": "images/size_rent_efficiency.png", "title": "면적 대비 임대료", "text": "소형 평수는 입지 가치가 가격을 결정하므로 효율적인 선택이 필요합니다."}
    ]},
    {"icon": "map", "title": "상권 밀집도", "items": [
        {"img": "images/hist_0.png", "title": "보증금 분포", "text": "중앙값 2,000만원 중심의 시장 진입 전략이 필요합니다."},
        {"img": "images/hist_1.png", "title": "월세 분포", "text": "100~150만원 구간의 공실 방어 전략을 적용하세요."}
    ]},
    {"icon": "map-pin", "title": "입지 및 트렌드", "items": [
        {"img": "images/corr.png", "title": "가격 상관관계", "text": "보증금과 월세의 상관관계를 이용해 협상력을 확보하십시오."},
        {"img": "images/floor_premium_trend.png", "title": "층별 트렌드", "text": "로드샵 vs 목적형 사업 성격에 따른 층별 전략을 대조하십시오."}
    ]}
]

# HTML 생성
html = f"""
<!DOCTYPE html><html lang='ko'><head><meta charset='UTF-8'>
<script src='https://cdn.tailwindcss.com'></script>
<script src='https://unpkg.com/lucide@latest'></script>
<style>
    body {{ background-color: #0f172a; color: #f1f5f9; font-family: 'Pretendard', sans-serif; }}
    .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 1rem; }}
</style></head><body class='p-8'><div class='max-w-7xl mx-auto'>
    <header class='mb-10'>
        <h1 class='text-4xl font-bold text-sky-400 mb-6'>상가 매물 종합 분석 대시보드</h1>
        <div class='grid grid-cols-2 md:grid-cols-5 gap-4'>
            {"".join([f"<div class='glass p-4 text-center'><div class='text-slate-400 text-xs'>{t}</div><div class='text-lg font-bold text-sky-300'>{v}</div></div>" for t, v in kpi])}
        </div>
    </header>
    {"".join([f'''
    <div class='glass p-6 mb-8'>
        <h2 class='text-2xl font-bold text-white mb-6 flex items-center gap-3'><i data-lucide='{g['icon']}'></i>{g['title']}</h2>
        <div class='grid grid-cols-1 md:grid-cols-2 gap-6'>
            {"".join([f"<div class='bg-slate-900/50 p-4 rounded-lg'><img src='{i['img']}' class='w-full rounded mb-3'><h4 class='text-sky-300 font-bold'>{i['title']}</h4><p class='text-sm text-slate-300'>{i['text']}</p></div>" for i in g['items']])}
        </div>
    </div>''' for g in sections])}
    <div class='glass p-8'><h2 class='text-2xl font-bold text-white mb-4'>핵심 키워드 전략 분석</h2>
        <img src='images/keyword_strategy_tfidf.png' class='w-full rounded-lg'>
    </div>
    <script>lucide.createIcons();</script>
</div></body></html>
"""
with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
