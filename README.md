
---

# AI Demand Forecasting & Inventory Optimization

AI-driven supply chain analytics platform built to forecast inventory demand, monitor stockout risk, optimize reorder planning, and improve operational visibility through automated dashboards and forecasting workflows.

---

## Tech Stack

Python | Streamlit | SQL | Snowflake | Power BI | Airbyte | Plotly

---

## Dashboard Preview

<img width="1512" height="982" alt="Inventory SS" src="https://github.com/user-attachments/assets/88d67539-b208-44c0-a62f-43de4a796043" />

---

## Business Problem

Retail and supply chain teams often face limited visibility into demand fluctuations, inventory exposure, and stockout risk due to disconnected operational datasets and manual reporting processes.

---

## Solution

Developed an AI-powered inventory intelligence platform integrating synthetic retail and operational datasets into forecasting workflows, centralized dashboards, and automated reporting systems for supply chain decision-making.

---

## Key Features

- Demand forecasting workflows
- Inventory optimization analytics
- Automated ETL pipelines
- Reorder threshold monitoring
- Stockout risk analysis
- Regional sales performance tracking
- Executive operational dashboards

---

## Architecture Overview

Retail Sales Data
      ↓
Python ETL Pipelines
      ↓
Snowflake Warehouse
      ↓
Power BI / Streamlit Dashboards
      ↓
AI Forecasting Insights

---

## KPI Metrics

- Forecast Accuracy
- Inventory Turnover
- Reorder Thresholds
- Stockout Risk
- Regional Product Demand
- Sales Trend Analysis

---

## Repository Structure

/data
/dashboard_app
/sql
/etl
/assets
/docs

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Demand-Forecasting-Inventory-Optimization.git
cd AI-Demand-Forecasting-Inventory-Optimization

Create Virtual Environment

Mac/Linux:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Dashboard
streamlit run app.py
