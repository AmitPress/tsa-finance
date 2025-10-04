import gradio as gr
import yfinance as yf
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
# Load your pre-trained Keras model
model = tf.keras.models.load_model("./best.keras")

# scale the data
def create_scaler(df):
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_df = scaler.fit_transform(df['Close'].values.reshape(-1, 1))
    return scaler, scaled_df
# create input output sequence
def create_sequence(scaled_df):
    X, y = [], []
    window = 60
    n_future = 1
    for i in range(len(scaled_df) - window - n_future - 1):
        X.append(scaled_df[i:i+window])
        y.append(scaled_df[i+window+n_future])
    X = np.array(X)
    y = np.array(y)
    return X, y

def fetch_and_predict(ticker, period):
    # Fetch historical stock data using yfinance
    try:
        df = yf.download(ticker, period=period)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
    except Exception as e:
        print("check 2")
        return f"Error downloading data: {e}"
    
    # Check if we have enough data for predictions

    if df.shape[0] < 60:
        return "Not enough data for predictions. Please select a longer period."
    
    # prepare data
    scaler, df = create_scaler(df)
    X, y = create_sequence(df)
    # Predicting stock prices
    try:
        print("fine")
        yhat = model.predict(X)
    except Exception as e:
        return f"Error during prediction: {e}"
    # Plot the predicted prices
    plt.figure(figsize=(14, 7))
    plt.plot(y, label='Actual Prices')
    plt.plot(yhat, label='Predicted Prices')
    plt.title(f'Stock Price Prediction (LSTM) - [{str(ticker)}]')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.xticks(rotation=45)
    return plt.gcf()

interface = gr.Interface(
    fn=fetch_and_predict,
    inputs=[
        gr.Textbox(label="Stock Ticker", placeholder="Enter stock ticker (e.g., DAL, AAPL)"),
        gr.Textbox(label="Period", placeholder="Enter period (e.g., '1y')")
    ],
    outputs=gr.Plot(),
    live=False,
    allow_flagging="never",
    title="Stock Price Prediction",
    description="Enter the stock ticker and period, then click the button to fetch data and predict prices.",
    theme="huggingface",
)

interface.launch()
