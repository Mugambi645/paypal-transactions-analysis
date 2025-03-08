import altair as alt
import pandas as pd
import streamlit as st
from datetime import date, timedelta

# Streamlit Page Config
st.set_page_config(page_title="Charts", page_icon="📈")

# Title
st.title("📊 Chart Maker")

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")

PaymentStatus = st.sidebar.selectbox(
    "Select Payment Status", ["All", "Charge", "Refund", "Chargeback"]
)

PaymentMethod = st.sidebar.selectbox(
    "Select Payment Method", ["All", "Goods and Services", "Friends & Family"]
)

PaymentApplication = st.sidebar.selectbox(
    "Select Payment Application", ["All", "Desktop", "Tablet", "Phone"]
)

PaymentCountry = st.sidebar.selectbox(
    "Select Payment Country", ["All", "US", "UK", "AU"]
)

# Date Range Selection
today = date.today()
days_ago = today - timedelta(days=180)

StartDate = st.sidebar.date_input("Start Date", days_ago)
EndDate = st.sidebar.date_input("End Date", today)

# File Upload
df_file = st.file_uploader("📂 Upload Transactions CSV", type=["csv"])
if df_file is None:
    st.warning("⚠️ Please upload a CSV file to continue.")
    st.stop()

# Load Data
df = pd.read_csv(df_file)

# Data Preprocessing
required_columns = ["Total", "Transaction_Type", "Type", "Country", "Source", "Day", "Success", "Customer_Name", "Transaction_Notes"]
if not set(required_columns).issubset(df.columns):
    st.error("❌ Uploaded file is missing required columns.")
    st.stop()

df = df[df["Success"] == 1]  # Filter successful transactions
df["Day"] = pd.to_datetime(df["Day"])  # Ensure correct datetime format
df["Transaction_Notes"].fillna("N/A", inplace=True)  # Fill missing notes
df["Total"] = pd.to_numeric(df["Total"], errors="coerce")  # Convert Total to numeric
df["int_created_date"] = df["Day"].dt.strftime("%Y-%m")  # Format month-year

# Apply Filters
filters = {
    "Type": PaymentStatus if PaymentStatus != "All" else None,
    "Transaction_Type": PaymentMethod if PaymentMethod != "All" else None,
    "Source": PaymentApplication if PaymentApplication != "All" else None,
    "Country": PaymentCountry if PaymentCountry != "All" else None,
}

for col, value in filters.items():
    if value:
        df = df[df[col] == value]

df = df[(df["Day"] >= pd.to_datetime(StartDate)) & (df["Day"] <= pd.to_datetime(EndDate))]

# Debugging - Show Filtered Data
st.write("📌 **Filtered Data Preview:**", df)

# Ensure Data is Not Empty
if df.empty:
    st.warning("⚠️ No data available for the selected filters.")
    st.stop()

# Disable Altair Row Limit
alt.data_transformers.disable_max_rows()

# Charts
chart1 = alt.Chart(df).mark_bar().encode(
    alt.X("Total:Q", bin=True),
    alt.Y("count()"),
).properties(
    title="📊 Count of Transactions",
    width=800,
    height=500,
)

chart2 = alt.Chart(df).mark_boxplot().encode(
    x=alt.X("int_created_date:N", title="Month"),
    y=alt.Y("Total:Q", title="Transaction Amount"),
).properties(
    title="📈 Box & Whisker Plot by Month",
    width=800,
    height=500,
)

chart3 = alt.Chart(df).mark_bar().encode(
    x=alt.X("int_created_date:N", title="Month"),
    y=alt.Y("sum(Total):Q", title="Total Amount"),
    color=alt.Color("Type:N", title="Payment Type"),
).properties(
    title="💰 Monthly Transaction Sum",
    width=800,
    height=500,
)

chart4 = alt.Chart(df).mark_bar().encode(
    x=alt.X("int_created_date:N", title="Month"),
    y=alt.Y("count(Total):Q", title="Transaction Count"),
    color=alt.Color("Type:N", title="Payment Type"),
).properties(
    title="📈 Monthly Transaction Count",
    width=800,
    height=500,
)

# Display Charts in Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Histogram", "Box & Whiskers", "Monthly Sum", "Monthly Count"])

with tab1:
    st.altair_chart(chart1, use_container_width=True)
with tab2:
    st.altair_chart(chart2, use_container_width=True)
with tab3:
    st.altair_chart(chart3, use_container_width=True)
with tab4:
    st.altair_chart(chart4, use_container_width=True)
