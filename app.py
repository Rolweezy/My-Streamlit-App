import streamlit as st
#import pandas as pd
#from skops import io as sio
#import pickle
#import numpy as np

#import cloudpickle
#import joblib


# Page config
st.set_page_config(page_title="Smart Predictor", page_icon="🤖", layout="wide")

# Home page content
st.title("🤖 Smart Predictor Dashboard")
st.markdown("""
Welcome to **Smart Predictor** — a machine learning-powered prediction tool.  

**How to Use:**
1. Go to the **Predict** page in the sidebar.
2. Upload your dataset or enter values manually.
3. View results instantly and explore **Model Insights** for explanations.
""")

# Download sample CSV
with open("WA_Fn-UseC_-Telco-Customer-Churn.csv", "rb") as f:
    st.download_button(
        label="📥 Download Sample Data",
        data=f,
        file_name="WA_Fn-UseC_-Telco-Customer-Churn.csv",
        mime="text/csv"
    )

st.markdown("---")
st.markdown("© 2025 Smart Predictor | Built with Streamlit 🚀, developed by Ronald O. Otieno")








