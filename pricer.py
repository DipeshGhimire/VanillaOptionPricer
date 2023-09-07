# import necessary packages
from scipy.stats import norm
import numpy as np
import streamlit as st

# streamlit app title
st.set_page_config(layout="wide")
st.title("Vanilla Option Pricer")

# function to calulate the price of a vanilla call option
def vanilla_call_price(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price = S * np.exp(-r * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return price

# function to calulate the price of a vanilla put option
def vanilla_put_price(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-r * T) * norm.cdf(-d1)
    return price

# take inputs from the user in streamlit
S = st.sidebar.number_input("Stock Price", min_value=1., max_value=10000., value=100.)
K = st.sidebar.number_input("Strike Price", min_value=1., max_value=10000., value=100.)
T = st.sidebar.number_input("Time to Maturity", min_value=1., max_value=10., value=1.)
r = st.sidebar.number_input("Interest Rate", min_value=0., max_value=1., value=0.05)
sigma = st.sidebar.number_input("Volatility", min_value=0., max_value=10., value=0.12)

# calculate the price of the option
call_price = vanilla_call_price(S, K, T, r, sigma)
put_price = vanilla_put_price(S, K, T, r, sigma)

# display the results
st.subheader("Vanilla Call Option")
st.write(f"Price: ${call_price:.2f}")

st.subheader("Vanilla Put Option")
st.write(f"Price: ${put_price:.2f}")