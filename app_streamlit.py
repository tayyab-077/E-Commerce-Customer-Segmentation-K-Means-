import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('clustered_customers.csv')

st.title("Customer Segmentation Dashboard")

# Sidebar filter
cluster = st.sidebar.selectbox("Select Cluster", sorted(df['Cluster'].unique()))

# Show data
st.subheader(f"Cluster {cluster} Summary")
st.write(df[df['Cluster'] == cluster].describe())

# Plot
st.subheader("RFM Distribution by Cluster")
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
sns.histplot(df[df['Cluster'] == cluster]['Recency'], ax=ax[0])
sns.histplot(df[df['Cluster'] == cluster]['Frequency'], ax=ax[1])
sns.histplot(df[df['Cluster'] == cluster]['Monetary'], ax=ax[2])
st.pyplot(fig)