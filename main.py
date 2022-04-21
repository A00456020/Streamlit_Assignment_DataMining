import pandas as pd
import requests
import datetime
import streamlit as st
st.title('Bitcoin prices in various currencies over last few days')
st.text('App Created by Parth Tarak Vaidya, A00456020, MCDA, SMU, Halifax, NS')
num_days = st.slider(label="Number of Days", min_value=1, max_value=365, step=1, value=14)