import pandas_ta as ta

def generate_signals(df):
    df['RSI'] = ta.rsi(df['Close'], length=14)
    macd = ta.macd(df['Close'])
    df = df.join(macd)
    latest = df.iloc[-1]
    prev = df.iloc[-2]
    if latest['RSI'] < 30 and prev['MACD_12_26_9'] < prev['MACDs_12_26_9'] and latest['MACD_12_26_9'] > latest['MACDs_12_26_9']:
        entry = latest['Close']
        return {
            "entry_price": round(entry, 2),
            "target_price": round(entry * 1.05, 2),
            "holding_days": 5,
            "confidence_score": 0.85
        }
    return None