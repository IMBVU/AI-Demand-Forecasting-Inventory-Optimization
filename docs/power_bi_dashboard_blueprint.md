# Power BI Dashboard Blueprint

Pages:
1. Demand Forecast Overview: units sold, revenue, 30-day forecast, category trend.
2. Inventory Risk: stockout risk count, safety stock, reorder point, recommended reorder quantity.
3. Store & Region Performance: region/store drilldown, sales velocity, revenue by category.
4. Purchasing Recommendations: products flagged as Reorder, estimated reorder value, ABC priority.

Core DAX Measures:
Total Revenue = SUM(retail_inventory_sales[revenue])
Units Sold = SUM(retail_inventory_sales[units_sold])
Stockout Risk Count = COUNTROWS(FILTER(retail_inventory_sales, retail_inventory_sales[stockout_risk_flag] = TRUE()))
Recommended Reorder Units = SUM(retail_inventory_sales[recommended_reorder_qty])
Forecasted Units 30D = SUM(forecast_inventory_recommendations[forecast_30_day_units])
Estimated Reorder Value = SUMX(forecast_inventory_recommendations, forecast_inventory_recommendations[reorder_point] * forecast_inventory_recommendations[avg_price])
