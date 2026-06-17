import streamlit as st
import requests

st.title('📊 Hermes Agent Token Usage')
GIST_URL = 'https://gist.githubusercontent.com/dinh1809/175307aff614b51a356f8d1eaca4f826/raw/usage.json'

def get_usage():
    try:
        response = requests.get(GIST_URL)
        return response.json()
    except:
        return {'input': 0, 'output': 0, 'total': 0}

data = get_usage()
col1, col2, col3 = st.columns(3)
col1.metric('Input', data.get('input', 0))
col2.metric('Output', data.get('output', 0))
col3.metric('Total', data.get('total', 0))
