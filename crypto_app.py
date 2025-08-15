import streamlit as st
import requests
from datetime import datetime

# Cấu hình trang
st.set_page_config(page_title="Crypto Giá Real-Time", layout="wide")
st.title("📈 Giá BTC & ETH (USD) – Cập nhật thời gian thực")

# Hàm lấy giá từ API
@st.cache_data(ttl=10)
def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
    resp = requests.get(url, params=params, timeout=10)
    data = resp.json()
    return data.get("bitcoin", {}).get("usd"), data.get("ethereum", {}).get("usd")

# Lấy dữ liệu
btc_price, eth_price = get_prices()
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Hiển thị
col1, col2 = st.columns(2)
col1.metric("BTC (USD)", f"{btc_price:,}")
col2.metric("ETH (USD)", f"{eth_price:,}")
st.caption(f"Cập nhật lúc: {now}")
