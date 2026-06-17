import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Crypto Tracker", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: white; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Real-Time Crypto Tracker")

if 'tokens' not in st.session_state:
    st.session_state.tokens = ['bitcoin', 'ethereum', 'solana']

def get_price(token_ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {'ids': ','.join(token_ids), 'vs_currencies': 'usd'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return None

col1, col2 = st.columns([1, 3])

with col1:
    new_token = st.text_input("Add Token ID").lower()
    if st.button("Add"):
        if new_token and new_token not in st.session_state.tokens:
            st.session_state.tokens.append(new_token)
    
    st.subheader("Tracking:")
    for t in st.session_state.tokens[:]:
        if st.button(f"Remove {t}", key=f"rm_{t}"):
            st.session_state.tokens.remove(t)
            st.rerun()

with col2:
    data = get_price(st.session_state.tokens)
    if data:
        df = pd.DataFrame.from_dict(data, orient='index')
        df.columns = ['Price (USD)']
        st.table(df)
    else:
        st.error("Data fetch fail.")

if st.button("Refresh"):
    st.rerun()
