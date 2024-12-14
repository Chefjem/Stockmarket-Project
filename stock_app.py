import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit settings
st.set_page_config(page_title="Stock Search", layout="wide")

# Title
st.title("📈 Stock Search and Chart Visualization")

# User input
ticker = st.text_input("Stock Ticker (e.g., AAPL, TSLA):", "").upper()

# Date range selection
start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

if ticker:
    try:
        # Fetch stock data
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)

        if hist.empty:
            st.warning("No data found for this date range. Please check the dates.")
        else:
            # Create tabs
            tab1, tab2 = st.tabs(["📊 Price Chart", "📉 Statistics"])

            # Tab 1: Price Chart
            with tab1:
                st.subheader(f"{ticker} Stock Price Chart")
                fig, ax = plt.subplots(figsize=(12, 6))
                ax.plot(hist.index, hist['Close'], label="Closing Price", color='blue')
                ax.set_title(f"{ticker} Stock Closing Price", fontsize=16)
                ax.set_xlabel("Date", fontsize=12)
                ax.set_ylabel("Price (USD)", fontsize=12)
                ax.legend()
                ax.grid()
                st.pyplot(fig)

            # Tab 2: Statistics
            with tab2:
                st.subheader("📊 Statistical Information")
                hist['% Change'] = hist['Close'].pct_change() * 100
                hist['50-Day Moving Average'] = hist['Close'].rolling(window=50).mean()

                st.write("Last 10 Days Data:")
                st.dataframe(hist[['Close', '% Change', '50-Day Moving Average']].tail(10))

                # Moving Average Chart
                st.subheader("50-Day Moving Average Chart")
                fig, ax = plt.subplots(figsize=(12, 6))
                ax.plot(hist.index, hist['Close'], label="Closing Price", color='blue')
                ax.plot(hist.index, hist['50-Day Moving Average'], label="50-Day Moving Average", color='orange')
                ax.set_title(f"{ticker} Moving Average Chart", fontsize=16)
                ax.set_xlabel("Date", fontsize=12)
                ax.set_ylabel("Price (USD)", fontsize=12)
                ax.legend()
                ax.grid()
                st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter a stock ticker and select a date range.")

