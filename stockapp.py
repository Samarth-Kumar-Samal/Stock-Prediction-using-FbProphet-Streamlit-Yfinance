import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = '2014-01-01'
END = date.today().strftime('%Y-%m-%d')


# Setting up the Page Configuration
st.set_page_config(
    page_title='Stock Price Prediction Application',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='auto'
)

# Setting up the Page title and summary as animated text
st.header('Stock Prediction Web Application')
st.write('Stock prediction app leverages advanced algorithms to forecast market trends, empowering users with real-time insights for informed investment decisions.')

# Add space before the columns
st.markdown("<br>", unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns(2)

# Inside the first column
with col1:
    start_date = st.date_input("Select the Start Date:", value=date(2015, 1, 1))

# Inside the second column
with col2:
    end_date = st.date_input("Select the End Date:", value=date.today())


# Add space before the columns
st.markdown("<br>", unsafe_allow_html=True)

# Fetch the top 50 tickers by market capitalization
top_tickers = yf.Tickers(' '.join(['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'NVDA', 'V', 'PYPL', 'GS', 'INTC', 'CSCO', 'DIS', 'IBM', 'PFE', 'JNJ', 'MRK', 'VZ', 'T', 'NFLX', 'C', 'WMT', 'BA', 'PG', 'KO', 'PEP', 'MMM', 'HD', 'GS', 'AXP', 'JPM', 'UNH', 'CVX', 'XOM', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'NVDA', 'V', 'PYPL', 'GS', 'INTC', 'CSCO', 'DIS', 'IBM', 'PFE', 'JNJ']))

# Extract the list of top 50 tickers
top_tickers_list = [ticker for ticker in top_tickers.tickers]

# Allow the user to select a ticker from the drop-down list
selected_stock = st.selectbox('Select a Ticker', top_tickers_list)

# Sidebar with user input for prediction period
n_years = st.slider('Years of prediction:', 1, 10)
period = n_years * 365

# Display the selected period
st.write('Prediction period in days:', period)


# Function to load data using yfinance
@st.cache_data
def load_data(ticker, start, end):
    # Download historical stock data using yfinance with dynamic start and end dates
    data = yf.download(ticker, start, end)
    # Reset index to have the date as a column
    data.reset_index(inplace=True)
    return data

data = load_data(selected_stock, start_date, end_date)


st.subheader('Raw data for {}'.format(selected_stock))
st.write(data)

# Plot raw data
def plot_raw_data():
    fig = go.Figure()

    # Add trace for 'stock_open' with a specified color
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open", line=dict(color='blue')))

    # Add trace for 'stock_close' with a different color
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close", line=dict(color='orange')))

    # Update layout for better visualization
    fig.update_layout(title_text='Time Series Data for {}'.format(selected_stock), xaxis_rangeslider_visible=True)

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig)

# Call the function to plot raw data
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})


# m is the Prophet model
m = Prophet()

# Fit the model on the training data
m.fit(df_train)

# Create a dataframe for the future period for prediction
future = m.make_future_dataframe(periods=period)

# Generate the forecast based on the fitted model
forecast = m.predict(future)

# Display the forecast data
st.subheader('Forecast data')
st.write(forecast.tail())

# Display and plot the forecast for the specified period
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)  # Assuming plot_plotly is a custom function for plotting
st.plotly_chart(fig1)

# Display the forecast components
st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)
