
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(page_title="AI Demand Forecasting & Inventory Optimization", page_icon="📦", layout="wide")
ROOT = Path(__file__).resolve().parents[1] / "data"
sales = pd.read_csv(ROOT / "retail_inventory_sales.csv", parse_dates=["date"])
rec = pd.read_csv(ROOT / "forecast_inventory_recommendations.csv")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;700;800&family=JetBrains+Mono:wght@500&display=swap');
.stApp {background: linear-gradient(120deg,#042f2e 0%,#064e3b 45%,#111827 100%); color:#ecfdf5; font-family:Manrope,sans-serif;}
.supply {padding:2rem; border-radius:30px; background:rgba(236,253,245,.08); border:1px solid rgba(16,185,129,.35); position:relative; overflow:hidden;}
.supply:after {content:""; position:absolute; width:260px; height:260px; right:-80px; top:-80px; border-radius:50%; background:rgba(52,211,153,.18); animation:float 5s ease-in-out infinite;}
.supply h1 {font-size:3rem; margin:0; font-weight:800;}
.card {background:rgba(6,78,59,.72); border:1px solid rgba(167,243,208,.26); border-radius:22px; padding:1.1rem; transition:.25s ease;}
.card:hover {transform:scale(1.03); border-color:#6ee7b7;}
.label {font-family:'JetBrains Mono',monospace; color:#a7f3d0; font-size:.75rem; text-transform:uppercase;}
.val {font-size:1.95rem; font-weight:800; color:#fef3c7;}
@keyframes float {0%,100%{transform:translateY(0)}50%{transform:translateY(25px)}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='supply'>
<h1>AI-Powered Demand Forecasting & Inventory Optimization</h1>
<p>Operations-focused inventory cockpit for demand signals, reorder thresholds, stockout monitoring, and purchasing recommendations across stores and product categories.</p>
</div>
""", unsafe_allow_html=True)

region = st.multiselect("Region", sorted(sales.region.unique()), default=sorted(sales.region.unique()))
category = st.multiselect("Category", sorted(sales.category.unique()), default=sorted(sales.category.unique()))
f = sales[sales.region.isin(region) & sales.category.isin(category)]

metrics = [
    ("Sales Records", f"{len(f):,}"),
    ("Revenue", f"${f.revenue.sum()/1_000_000:.1f}M"),
    ("Units Sold", f"{f.units_sold.sum():,}"),
    ("Stockout Risk Rows", f"{int(f.stockout_risk_flag.sum()):,}"),
]
cols=st.columns(4)
for col,(label,val) in zip(cols, metrics): col.markdown(f"<div class='card'><div class='label'>{label}</div><div class='val'>{val}</div></div>", unsafe_allow_html=True)

left,right=st.columns([1.05,.95])
with left:
    st.subheader("Demand Trend")
    trend=f.assign(month=f.date.dt.to_period('M').astype(str)).groupby('month', as_index=False).agg(units=('units_sold','sum'), revenue=('revenue','sum'))
    st.altair_chart(alt.Chart(trend).mark_line(point=True).encode(x='month:T', y='units:Q', tooltip=['month','units','revenue']).properties(height=360), use_container_width=True)
with right:
    st.subheader("Category Reorder Exposure")
    cat=f.groupby('category', as_index=False).agg(reorder_qty=('recommended_reorder_qty','sum'), stockout_risk=('stockout_risk_flag','sum'))
    st.altair_chart(alt.Chart(cat).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(x='category:N', y='reorder_qty:Q', color='category:N', tooltip=['category','reorder_qty','stockout_risk']).properties(height=360), use_container_width=True)

st.subheader("Store-Level Inventory Risk")
store=f.groupby(['store_id','region'], as_index=False).agg(on_hand=('on_hand_units','mean'), reorder=('recommended_reorder_qty','sum'), risk=('stockout_risk_flag','sum'))
st.altair_chart(alt.Chart(store).mark_circle(size=300).encode(x='on_hand:Q', y='reorder:Q', color='region:N', size='risk:Q', tooltip=['store_id','region','on_hand','reorder','risk']).properties(height=340), use_container_width=True)

st.subheader("AI Inventory Recommendation")
top_cat = cat.sort_values('reorder_qty', ascending=False).head(1).iloc[0]
st.success(f"Highest reorder exposure is in {top_cat.category}. Purchasing should prioritize items with low on-hand units, longer lead times, and repeated stockout-risk flags before the next demand cycle.")
with st.expander("Preview inventory data"):
    st.dataframe(f.head(500), use_container_width=True)
