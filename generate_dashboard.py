import sqlite3
import pandas as pd
import json

# 1. 데이터 로드
conn = sqlite3.connect('data/nemo_stores.db')
df = pd.read_sql('SELECT * FROM stores', conn)
conn.close()

# 2. KPI 계산
kpi = {
    "total": len(df),
    "avg_deposit": int(df['deposit'].mean()),
    "avg_rent": int(df['monthlyRent'].mean()),
    "avg_size": round(df['size'].mean(), 1),
    "top_biz": df['businessLargeCodeName'].mode()[0]
}

# 3. 차트 섹션 (성격별 그룹화)
groups = [
    {"title": "비용 구조 및 효율성", "items": ["premium", "size"]},
    {"title": "상권 밀집도", "items": ["deposit", "rent"]},
    {"title": "입지 및 트렌드", "items": ["corr", "floor"]}
]

# 4. HTML 생성
html = f"""
<!DOCTYPE html><html lang='ko'><head><meta charset='UTF-8'>
<script src='https://cdn.tailwindcss.com'></script>
<style>
    body {{ background-color: #0f172a; color: #f1f5f9; font-family: 'Pretendard', sans-serif; }}
    .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 1rem; }}
</style>
</head><body class='p-8'><div class='max-w-7xl mx-auto'>
    <header class='mb-10'>
        <h1 class='text-4xl font-bold text-sky-400 mb-6'>상가 매물 분석 대시보드</h1>
        <div class='grid grid-cols-2 md:grid-cols-5 gap-4'>
            {[f"<div class='glass p-4 text-center'><div class='text-slate-400 text-xs'>{t}</div><div class='text-xl font-bold text-sky-300'>{v}</div></div>" for t, v in [("전체 매물", f"{kpi['total']}건"), ("평균 보증금", f"{kpi['avg_deposit']:,}만"), ("평균 월세", f"{kpi['avg_rent']:,}만"), ("평균 면적", f"{kpi['avg_size']}㎡"), ("최다 업종", kpi['top_biz'])]]}
        </div>
    </header>
    
    {"".join([f'''
    <div class='glass p-6 mb-8'>
        <h2 class='text-2xl font-bold text-white mb-6'>{g['title']}</h2>
        <div class='grid grid-cols-1 md:grid-cols-2 gap-6'>
            <!-- 그래프 아이템들 추가 로직 생략 -->
        </div>
    </div>''' for g in groups])}
</div></body></html>
"""
with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
