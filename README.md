# E-commerce-Analytics-RFM-Segmentation-Sales-Forecasting
E-commerce Customer Intelligence &amp; Sales Forecasting App using Python, Streamlit, and ML

# E-commerce Customer Intelligence & Sales Forecasting

## Overview
This project is a **Streamlit web application** that provides insights into customer behavior for an e-commerce business and predicts sales based on historical data.
It combines **RFM (Recency, Frequency, Monetary) analysis**, visualizations, and machine learning for **sales prediction**.

---

## Features
1. **RFM Analysis**
   - Segment customers into categories like **Champion, Loyal, At Risk, Low Value** based on purchasing behavior.
   - Helps identify **high-value customers** for targeted marketing.

2. **RFM Scatter Plot**
   - Interactive Plotly chart to visualize **Recency vs Monetary value** with customer segments and frequency size.

3. **Sales Prediction**
   - Enter product **Quantity** to predict **Total Sales** using a **Random Forest Regressor** model.
   - Interactive input with **Streamlit button**.

4. **Sales Forecasting**
   - Uses **lag features** (previous day/week sales) to predict trends.
   - Plots **Actual vs Predicted Sales** to visualize forecast accuracy.

---

## Dataset
- The dataset used is a simulated **e-commerce transactional dataset** with columns:
  - `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`
- Cleaned to remove canceled orders and missing Customer IDs.
- Target column created: `TotalPrice = Quantity * UnitPrice`

---

## Technologies Used
- **Python 3.x**
- **Streamlit**: For interactive web UI
- **Pandas**: Data cleaning and manipulation
- **Plotly & Matplotlib**: Data visualization
- **Scikit-learn**: Machine learning (Random Forest Regressor)

---
## How to Run Locally
1. Clone the repository: https://github.com/shivamkadam-8/E-commerce-Analytics-RFM-Segmentation-Sales-Forecasting

2. 2. Install required libraries:
  
3. Run the app:


---

## Key Learning
- Conducted **customer segmentation** using RFM analysis.  
- Built a **Random Forest model** for predicting sales based on historical data.  
- Developed a **fully interactive web application** for real-time insights.  
- Gained experience in **data cleaning, visualization, and ML deployment**.

---

## Future Improvements
- Add **monthly/seasonal sales forecasting**.   
- Include additional **predictive features** like promotions, discounts, or ad budgets.

---

