import datetime

import pandas as pd 
import streamlit as st 
import yfinance as yt 




st.write(
    """
    # Stock Price Analyser

    Shown are the stock price of Apple Company

    """
)
ticker_symbol = st.text_input(
                        'Enter  Stock Symbol', 
                        'AAPL',
                        key="placeholder")



ticker_data = yt.Ticker(ticker_symbol)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(
                                "Starting Date",
                                datetime.date(2019, 1, 1)
                            )

with col2:
    end_date = st.date_input(
                                "Ending Date",
                                datetime.date(2023, 2, 14)
                            )


ticket_df = ticker_data.history(period="1d", 
                                start=f"{start_date}",
                                end=f"{end_date}")

st.write(
    f"""
    ### {ticker_symbol}'s Stock Price Info
    """
)                 

st.dataframe(ticket_df.head(10))


col1, col2 = st.columns(2)

with col1:
    st.write(
    """
    #### Daily Closing Prices:
    """
    )

    st.line_chart(ticket_df.Close)

with col2:
    st.write(
        """
        #### Daily Volume Prices:
        """
    )

    st.line_chart(ticket_df.Volume)


## showcassing line chart




