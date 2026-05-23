-- Snowflake schema for AI-Powered Demand Forecasting & Inventory Optimization
CREATE OR REPLACE TABLE products (product_id STRING, category STRING, product_name STRING, unit_cost FLOAT, unit_price FLOAT, abc_class STRING);
CREATE OR REPLACE TABLE retail_inventory_sales (sale_id STRING, date DATE, store_id STRING, region STRING, product_id STRING, category STRING, units_sold NUMBER, unit_price FLOAT, revenue FLOAT, promotion_flag BOOLEAN, on_hand_units NUMBER, lead_time_days NUMBER, safety_stock NUMBER, recommended_reorder_qty NUMBER, stockout_risk_flag BOOLEAN);
CREATE OR REPLACE TABLE forecast_inventory_recommendations (store_id STRING, product_id STRING, category STRING, avg_daily_units FLOAT, avg_on_hand FLOAT, avg_lead_time FLOAT, avg_price FLOAT, forecast_30_day_units NUMBER, reorder_point NUMBER, inventory_action STRING);

CREATE OR REPLACE VIEW inventory_kpis AS
SELECT region, category, SUM(units_sold) AS units_sold, SUM(revenue) AS revenue, SUM(CASE WHEN stockout_risk_flag THEN 1 ELSE 0 END) AS stockout_risk_count, SUM(recommended_reorder_qty) AS recommended_reorder_units
FROM retail_inventory_sales
GROUP BY region, category;
