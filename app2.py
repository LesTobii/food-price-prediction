import streamlit as st
import altair as alt
import pandas as pd
st.title("Food Price 1 Year Forecast")

st.warning("""
⚠️ Disclaimer: Predictions are based solely on the historical price data provided. 
External factors such as inflation, policy changes, or market shocks are NOT captured. 
Forecasts reflect trends observed in the available data only.
""")

df = pd.read_csv('df_engineered.csv')
forecasts = pd.read_csv('forecasts.csv')

# Item selector
item_choice = st.selectbox('Select Item', forecasts['Item'].unique())

# Filter for selected item
historical = df[df['Item'] == item_choice]
item_forecast = forecasts[forecasts['Item']==item_choice]

# Show table
st.write(item_forecast[['Date','Price']])

# Show chart
chart = alt.Chart(item_forecast).mark_line(point=True).encode(
    x='Date:T',
    y='Price:Q'
).properties(title=f'{item_choice} Price Forecast')

st.altair_chart(chart, use_container_width=True)


# Show raw data if user wants
if st.checkbox("Show past data"):
    st.subheader("Past Data")
    st.write(historical[['Date','Price']])
    # st.subheader("Forecasted Prices")
    # st.write(item_forecast)
