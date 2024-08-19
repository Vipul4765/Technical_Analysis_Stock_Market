import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("D:\\Sorted_data_stock_data\\RELIANCE.csv")

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Ensure columns are in the correct order
df = df[['Open', 'High', 'Low', 'Close']]  # Ensure these columns are present

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='Candlestick'
)])

# Update layout for better presentation
fig.update_layout(
    title='Reliance Candlestick Chart',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False,
    template='plotly_dark'  # Choose a template for styling
)

# Show the plot
fig.show()
