import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="10y")
    return df

def calculate_moving_average(df, window):
    return df['Close'].rolling(window=window).mean()

def identify_stage(df):
    df['200_MA'] = calculate_moving_average(df, 200)
    df['50_MA'] = calculate_moving_average(df, 50)
    df['Volume_Avg'] = df['Volume'].rolling(window=50).mean()

    # Conditions for each stage
    stage_2 = (df['Close'] > df['200_MA']) & (df['50_MA'] > df['200_MA'])
    stage_4 = (df['Close'] < df['200_MA']) & (df['50_MA'] < df['200_MA'])
    stage_1 = (df['Close'] < df['200_MA']) & (df['50_MA'] > df['200_MA'])
    stage_3 = (df['Close'] > df['200_MA']) & (df['50_MA'] < df['200_MA'])

    conditions = [stage_2, stage_4, stage_1, stage_3]
    stages = [2, 4, 1, 3]

    df['Stage'] = np.select(conditions, stages, default=0)
    
    return df

def analyze_stock(ticker):
    df = get_stock_data(ticker)
    df = identify_stage(df)

    # Find the duration of the current stage
    current_stage = df['Stage'].iloc[-1]
    
    if current_stage == 0:
        return {
            'Ticker': ticker,
            'Current Stage': current_stage,
            'Duration in Current Stage (days)': None
        }, df
    
    df['Stage_Change'] = df['Stage'].diff().fillna(0) != 0
    stage_change_indices = df[df['Stage_Change']].index

    # If there was no stage change in the historical data, consider the entire period as the duration
    if stage_change_indices.empty:
        stage_duration = len(df)
    else:
        # Find the index of the last stage change
        last_stage_change_index = stage_change_indices[-1]
        stage_duration = (df.index[-1] - last_stage_change_index).days
    
    stage_info = {
        'Ticker': ticker,
        'Current Stage': current_stage,
        'Duration in Current Stage (days)': stage_duration
    }
    
    return stage_info, df

# Example usage
ticker = input("Enter stock ticker: ")
stage_info, stock_data = analyze_stock(ticker)

print(f"Ticker: {stage_info['Ticker']}")
print(f"Current Stage: {stage_info['Current Stage']}")
print(f"Duration in Current Stage (days): {stage_info['Duration in Current Stage (days)']}")
