import numpy as np
import talib

def calculate_ema(data, period):
    return talib.EMA(data, timeperiod=period)

def calculate_macd(data):
    macd_line, signal_line, _ = talib.MACD(data)
    return macd_line, signal_line

def calculate_atr(high, low, close, period):
    return talib.ATR(high, low, close, timeperiod=period)

def calculate_rsi(data, period):
    return talib.RSI(data, timeperiod=period)

def calculate_ema_slope(ema_data):
    x = np.arange(len(ema_data))
    coeffs = np.polyfit(x, ema_data, 1)
    slope = coeffs[0]
    return slope

def trading_strategy(data, high, low, close):
    # Calculate indicators
    macd_line, signal_line = calculate_macd(data)
    atr = calculate_atr(high, low, close, period=14)
    rsi = calculate_rsi(close, period=14)
    ema_20 = calculate_ema(data, period=20)
    ema_50 = calculate_ema(data, period=50)

    # Calculate EMA position and slope
    ema_20_slope = calculate_ema_slope(ema_20)
    ema_50_slope = calculate_ema_slope(ema_50)

    # Implement your trading strategy logic
    if macd_line[-1] > signal_line[-1] and rsi[-1] > 50 and ema_20_slope > 0 and ema_50_slope > 0:
        # Place a buy order
        print("Buy signal")
    elif macd_line[-1] < signal_line[-1] and rsi[-1] < 50 and ema_20_slope < 0 and ema_50_slope < 0:
        # Place a sell order
        print("Sell signal")
    else:
        # No action
        print("No action")

# Example usage
data = [...]  # Your price data
high = [...]  # High price data
low = [...]   # Low price data
close = [...] # Close price data

trading_strategy(data, high, low, close)