import sqlite3
import pandas as pd
import json

conn = sqlite3.connect('data/nemo_stores.db')
df = pd.read_sql('SELECT * FROM stores', conn)
conn.close()

kpi = [("전체 매물", f"{len(df):,}건"), ("평균 보증금", f"{int(df['deposit'].mean()):,}만"), ("평균 월세", f"{int(df['monthlyRent'].mean()):,}만"), ("평균 면적", f"{round(df['size'].mean(), 1)}㎡"), ("최다 업종", df['businessLargeCodeName'].mode()[0])]

sections = [
    {"title": "비용 및 효율성", "items": [{"img": "images/premium_by_industry.png", "title": "업종별 권리금", "text": "주류점 등은 고위험-고수익 구조입니다. 투자비 회수 지표로 권리금을 확인하세요."}, {"img": "images/size_rent_efficiency.png", "title": "면적 대비 임대료", "text": "소형 평수는 입지에 따라 가격 편차가 큽니다. 입지가 과대평가된 매물을 가려내는 것이 핵심입니다."}]},
    {"title": "상권 밀집도", "items": [{"img": "images/hist_0.png", "title": "보증금 분포", "text": "중앙값 2,000만원이 핵심 진입 장벽입니다. 예비 창업자의 70%가 집중된 구간을 공략하세요."}, {"img": "images/hist_1.png", "title": "월세 분포", "text": "100~150만원 구간이 가장 빈번합니다. 업종별로 세분화된 고정비 기준을 적용하는 것이 필수입니다."}]},
    {"title": "입지 및 트렌드", "items": [{"img": "images/corr.png", "title": "가격 상관관계", "text": "보증금과 월세는 0.89의 강한 상관관계를 가집니다. 회귀선에서 벗어난 매물은 협상 대상입니다."}, {"img": "images/floor_premium_trend.png", "title": "층별 트렌드", "text": "1층이 시장 주도하나, 마케팅형 사업은 고층부 가성비 입지가 생존율을 높입니다."}]}
]

html = f"""
<!DOCTYPE html><html lang='ko'><head><meta charset='UTF-8'>
<script src='https://cdn.tailwindcss.com'></script>
<style>
    body {{ background-color: #0f172a; color: #f1f5f9; font-family: 'Pretendard', sans-serif; }}
    .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 1rem; }}
</style></head><body class='p-8'><div class='max-w-7xl mx-auto'>
    <header class='mb-10'>
        <h1 class='text-4xl font-bold text-sky-400 mb-6'>상가 매물 종합 분석</h1>
        <div class='grid grid-cols-2 md:grid-cols-5 gap-4'>
            {"".join([f"<div class='glass p-4 text-center'><div class='text-slate-400 text-xs'>{t}</div><div class='text-lg font-bold text-sky-300'>{v}</div></div>" for t, v in kpi])}
        </div>
    </header>
    {"".join([f'''
    <div class='glass p-6 mb-8'>
        <h2 class='text-2xl font-bold text-white mb-6'>{g['title']}</h2>
        <div class='grid grid-cols-1 md:grid-cols-2 gap-6'>
            {"".join([f"<div class='bg-slate-900/50 p-4 rounded-lg'><img src='{i['img']}' class='w-full rounded mb-3'><h4 class='text-sky-300 font-bold'>{i['title']}</h4><p class='text-sm text-slate-300'>{i['text']}</p></div>" for i in g['items']])}
        </div>
    </div>''' for g in sections])}
    <div class='glass p-8'><h2 class='text-2xl font-bold text-white mb-4'>핵심 키워드 분석</h2>
        <img src='images/keyword_strategy_tfidf.png' class='w-full rounded-lg'>
    </div>
</div></body></html>
"""
with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
