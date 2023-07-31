import pandas as pd

# Define time frame intervals
time_frames = {'1min': 1, '4min': 4, '15min': 15, '60min': 60, '240min': 240}

# Calculate "relative strength" for each time frame
for tf in time_frames:
    data[f'{tf}_RSI'] = pd.Series(data['Close']).rolling(time_frames[tf]).apply(lambda x: ((x[-1] - x.min()) / (x.max() - x.min())) * 100)
    
# Calculate "MACD strength" for each time frame
for tf in time_frames:
    data[f'{tf}_MACD'] = pd.Series(data['Close']).rolling(time_frames[tf]).apply(lambda x: ((x[-1] - x.min()) / (x.max() - x.min())) * 100)
    
# Calculate "ATR" for each time frame
for tf in time_frames:
    data[f'{tf}_ATR'] = pd.Series(data['Close']).rolling(time_frames[tf]).apply(lambda x: ((x[-1] - x.min()) / (x.max() - x.min())) * 100)
    
# Print the resulting DataFrame
print(data)

# Calculate "HeikinAshiDiff" for each time frame
for tf in time_frames:
    data[f'{tf}_HeikinAshiDiff'] = pd.Series(data['Close']).rolling(time_frames[tf]).apply(lambda x: ((x[-1] - x.min()) / (x.max() - x.min())) * 100)