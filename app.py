import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.title("E-commerce Customer Intelligence & Sales Forecasting")

# ---- Load and clean dataset ----
df = pd.read_csv("E-COMMERCE.csv")
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]  # remove canceled orders
df = df.dropna(subset=['CustomerID'])
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# ---- RFM Analysis ----
today = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (today - x.max()).days,
    'InvoiceNo': 'count',
    'TotalPrice': 'sum'
}).rename(columns={'InvoiceDate':'Recency',
                   'InvoiceNo':'Frequency',
                   'TotalPrice':'Monetary'})

# RFM Scoring
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'], 5, labels=[1,2,3,4,5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

# Customer Segments
def segment_customer(row):
    if row['RFM_Score'] >= '455':
        return 'Champion'
    elif row['F_Score'] >= 4:
        return 'Loyal'
    elif row['R_Score'] <= 2:
        return 'At Risk'
    else:
        return 'Low Value'
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# Display RFM Table
st.subheader("RFM Table with Segments")
st.dataframe(rfm)

# ---- RFM Scatter Plot ----
st.subheader("RFM Scatter Plot")
fig = px.scatter(rfm, x='Recency', y='Monetary', color='Segment', size='Frequency', hover_data=['RFM_Score'])
st.plotly_chart(fig)

# Features & target
X = df[['Quantity']]
y = df['TotalPrice']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)


# Aggregate daily sales
sales = df.groupby('InvoiceDate')['TotalPrice'].sum().reset_index()
sales.set_index('InvoiceDate', inplace=True)

# Create lag features
sales['Lag1'] = sales['TotalPrice'].shift(1)
sales['Lag7'] = sales['TotalPrice'].shift(7)
sales = sales.dropna()

# Train Random Forest on lag features
X_forecast = sales[['Lag1','Lag7']]
y_forecast = sales['TotalPrice']
X_train_f, X_test_f, y_train_f, y_test_f = train_test_split(X_forecast, y_forecast, test_size=0.2, shuffle=False)
model_forecast = RandomForestRegressor(n_estimators=100, random_state=42)
model_forecast.fit(X_train_f, y_train_f)
predictions = model_forecast.predict(X_test_f)

# Plot Actual vs Predicted
plt.figure(figsize=(10,5))
plt.plot(y_test_f.index, y_test_f, label='Actual Sales')
plt.plot(y_test_f.index, predictions, label='Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Sales Forecasting')
plt.legend()
st.pyplot(plt)

# ---- Sales Prediction (based on Quantity) ----
st.subheader("Sales Prediction")

# User input
quantity = st.number_input("Enter Quantity", 1)

# Predict on button click
if st.button("Predict"):
    prediction = model.predict([[quantity]])
    st.write(f"Predicted Sales: ${prediction[0]:.2f}")