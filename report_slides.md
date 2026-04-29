---
marp: true
theme: default
paginate: true
header: '종합 상가 데이터 분석 리포트'
footer: '© 2026 Wiset-Nemo'
style: |
  section {
    font-family: 'Courier New', monospace;
    background-color: #ffccff;
    color: #330066;
    padding: 40px;
    border: 4px dashed #6600ff;
  }
  h1, h2 {
    color: #ff00ff;
    text-transform: uppercase;
    text-shadow: 2px 2px #ffff00;
    margin-bottom: 20px;
  }
  table {
    border: 2px solid #330066;
    background-color: #ccffff;
  }
  th, td {
    border: 1px solid #330066;
    padding: 8px;
  }
  img {
    border: 4px double #ff00ff;
    background-color: #fff;
  }
---

# 종합 상가 데이터 대시보드
## 분석 결과 보고서

<!-- note: 안녕하세요. Y2K 빈티지 감성을 담아 분석 결과를 보고하겠습니다. 이번 발표에서는 최근 수집된 상가 데이터를 바탕으로 핵심 지표를 분석하고, 향후 전략 수립을 위한 인사이트를 도출하고자 합니다. 보증금, 월세 등 상권의 핵심 요소를 팝한 스타일로 다룰 예정이니 끝까지 함께해 주시기 바랍니다. -->

---

# 1. 핵심 성과 지표 (KPI)

| 지표 | 값 |
| :--- | :--- |
| **전체 매물** | 387건 |
| **평균 보증금** | 2,889만 |
| **평균 월세** | 194만 |
| **평균 면적** | 95.4㎡ |
| **최다 업종** | 일반음식점 |

![w:400](./images/price_type_share.png)

<!-- note: 핵심 성과 지표입니다. 총 387건의 매물을 분석했습니다. 일반음식점이 압도적으로 많네요. 이 데이터는 분석의 기초 자료로 활용될 것이며, 앞으로 나올 시각화 그래프들과 함께 보면서 시장 상황을 파악해 보겠습니다. -->

---

# 2. 업종 분석

## 업종 분포 및 지역별 분포
![w:400](./images/top_business_large.png)
![w:400](./images/dist_1.png)

<!-- note: 업종 분포를 보면 특정 지역과 업종 간의 상관관계가 보입니다. 틈새 시장을 파악하고 전략적 포지셔닝을 하는 것이 매우 중요합니다. 역세권에서의 우위가 수익성에 큰 영향을 미치니 데이터 기반으로 전략을 짜야 합니다. -->

---

# 3. 상권 밀집도

## 보증금 및 월세 분포
![w:400](./images/hist_0.png)
![w:400](./images/hist_1.png)

<!-- note: 보증금 중앙값이 2,000만원입니다. 월세는 100~150만원 구간에 몰려있고요. 입지별로 세분화된 전략이 필요하며, 이 데이터들은 임대차 협상 시 아주 강력한 자료로 쓰일 수 있습니다. -->

---

# 4. 입지 및 트렌드

## 가격 상관관계 및 층별 트렌드
![w:400](./images/corr.png)
![w:400](./images/floor_premium_trend.png)

<!-- note: 입지 및 트렌드입니다. 보증금과 월세 상관관계를 잘 활용하면 협상력 확보가 가능합니다. 고층부 가성비 입지를 공략하는 전략을 제안합니다. 시장 상황을 꾸준히 트래킹하는 것도 필수입니다. -->

---

# 5. 핵심 키워드 TOP 10

![w:600](./images/top_keywords.png)

<!-- note: 키워드 TOP 10을 뽑아봤습니다. 1층, 대로변, 역세권 등 여전히 강력한 키워드들이고요. 수유동, 번동이 주요 상권이네요. 이 키워드들을 마케팅에 적절히 섞으면 홍보 효과가 매우 좋을 것입니다. -->

---

# 감사합니다.

<!-- note: 이상으로 보고를 마칩니다. 데이터를 통해 시장의 흐름을 읽는 것이 핵심이었습니다. 질문 있으시면 편하게 말씀해 주세요. 감사합니다! -->
