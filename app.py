import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df_staples = pd.read_csv('df_staples_simple.csv')
forecasts = pd.read_csv('forecasts.csv')

st.title("📈 Staple Food Price Trends & Forecasts")

# Select item
item = st.selectbox(
    "Select a food item:",
    df_staples['Items_Clean'].unique()
)





# Filter data
historical = df_staples[df_staples['Items_Clean'] == item]
future = forecasts[forecasts['Item'] == item]

# Convert date if needed
historical['Date'] = pd.to_datetime(historical[['Year', 'Month']].assign(DAY=1))
future['Date'] = pd.to_datetime(future[['Year', 'Month']].assign(DAY=1))

# Plot
fig = px.line(historical, x='Date', y='Price', title=f"{item} Historical Prices & Forecast")
fig.add_scatter(x=future['Date'], y=future['Price'], mode='lines+markers', name='Forecast')

st.plotly_chart(fig, use_container_width=True)

# Show raw data if user wants
if st.checkbox("Show raw data"):
    st.subheader("Historical Data")
    st.write(historical.tail())
    st.subheader("Forecasted Prices")
    st.write(future)
