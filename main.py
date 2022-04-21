import pandas as pd
import requests
import datetime
import streamlit as st
st.title('Bitcoin prices in various currencies over last few days')
st.text('App Created by Parth Tarak Vaidya, A00456020, MCDA, SMU, Halifax, NS')
num_days = st.slider(label="Number of Days", min_value=1, max_value=365, step=1, value=14)
currency = st.radio(label="Currency", options=('CAD', 'USD', 'INR', 'AUD', 'GBP'))
API_URL = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency={str.lower(currency)}&days={num_days}&interval=daily'
req = requests.get(API_URL)
if req.status_code == 200:
    data = req.json()
clean_data = list()
for row in data['prices']:
    timestamp = datetime.datetime.fromtimestamp(row[0] / 1000)
    row[0] = timestamp.strftime('%Y-%m-%d')
    clean_data.append(row)
print(clean_data)