# 🛍️ Customer Segmentation with RFM & KMeans

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

🎯 **Goal:** To segment customers into distinct groups using their purchasing behavior, enabling businesses to personalize marketing and improve customer engagement.

---

## 🧠 What This Project Does

This project analyzes customer transactions and segments them into **behavioral clusters** based on:

- 🕒 **Recency** — How recently a customer made a purchase  
- 🔁 **Frequency** — How often they purchase  
- 💰 **Monetary** — How much they spend

We then apply **KMeans Clustering** to identify groups like:
- ✅ Loyal Customers
- ⚠️ At-risk Customers
- 🆕 New Shoppers
- 💸 High Spenders

---

## 🚀 How It Works

### 1. 📂 Data Cleaning
- Removed canceled orders (`InvoiceNo` starting with "C")
- Handled missing values
- Calculated total spending per invoice

### 2. 📊 RFM Analysis
```python
Recency = snapshot_date - customer's last purchase  
Frequency = total number of invoices per customer  
Monetary = total spending by the customer

# 🛍️ Customer Segmentation with RFM & KMeans

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

🎯 **Goal:** To segment customers into distinct groups using their purchasing behavior, enabling businesses to personalize marketing and improve customer engagement.

---

## 🧠 What This Project Does

This project analyzes customer transactions and segments them into **behavioral clusters** based on:

- 🕒 **Recency** — How recently a customer made a purchase  
- 🔁 **Frequency** — How often they purchase  
- 💰 **Monetary** — How much they spend

We then apply **KMeans Clustering** to identify groups like:
- ✅ Loyal Customers
- ⚠️ At-risk Customers
- 🆕 New Shoppers
- 💸 High Spenders

---

## 🚀 How It Works

📂 Data Cleaning
- Removed canceled orders (`InvoiceNo` starting with "C")
- Handled missing values
- Calculated total spending per invoice

📊 RFM Analysis

Recency = snapshot_date - customer's last purchase  
Frequency = total number of invoices per customer  
Monetary = total spending by the customer


📊 Feature Scaling

Scaler Used: StandardScaler
Why: To normalize Recency, Frequency, and Monetary columns.
Benefit: Ensures that all features contribute equally to the clustering process.


🔍 KMeans Clustering
1. Elbow Method: Ran KMeans for cluster counts 1–10 to determine the optimal number.
2. Optimal Clusters: Chose n_clusters = 4 based on the elbow curve.
3. Fit the Model: Applied KMeans on scaled RFM data.
4. Cluster Labels: Assigned each customer to a cluster.
5. Evaluation: Used Silhouette Score to assess cluster quality.

📈 Visualizations

Tool: Seaborn
Chart: pairplo
Purpose: Compare how clusters differ across RFM dimensions visually.

🧩 Cluster Interpretation

Cluster Description

0 High-value, loyal customers
1 At-risk customers
2 New or one-time buyers
3 Low-value or inactive customers


📦 Outputs Delivered

✅ Clustered Dataset: Contains CustomerID, Recency, Frequency, Monetary, and Cluster

📊 Visuals: RFM distribution via pairplots

🧮 Silhouette Score: Quantifies cluster performance


🎯 Business Impact
With this model, businesses can:

💎 Retain high-value customers
🔁 Re-engage at-risk users\
🆕 Identify and nurture new buyers


💰 Optimize marketing efforts through segmentation
🏁 Conclusion

Customer segmentation enables data-driven marketing strategies tailored to different customer types, improving overall engagement, satisfaction, and revenue.
