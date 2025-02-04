import streamlit as st

# Streamlit Page Config
st.set_page_config(page_title="Power BI Dashboards", layout="wide")
st.title("Power BI Dashboards Portal")

# Power BI Embed URL (For your organization)
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=1ccfa4de-0885-4b06-8e13-80d2e4a448b8&autoAuth=true&ctid=d034c668-6714-4eea-b081-e28a7d712fac"  # Replace with your actual report ID

# Embed Power BI Report in an iframe
st.components.v1.iframe(power_bi_url, width=1200, height=600)
