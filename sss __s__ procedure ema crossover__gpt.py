import pandas as pd
import numpy as np

# Load data into a DataFrame
df = pd.read_csv('nq_price_history.csv')

# Calculate exponential moving averages for multiple time frames
df['nq_ema_1'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_2'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_4'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_14'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_800'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_1600'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_3200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_6400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_12800'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_25600'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_51200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_102400'] = df['nq_close'].ewm(span=100).mean()


##############################################################
#   Structure 1
##############################################################

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_50'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_200'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_800'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_3200'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_12800'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_51200'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_204800'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_819200'], 1, 0)

# Print the DataFrame
print(df)

##############################################################
#   Structure 2
##############################################################

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_50'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_100'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_200'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_400'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_800'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_1600'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_3200'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_6400'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_12800'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_25600'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_51200'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_102400'], 1, 0)

# Print the DataFrame
print(df)

##############################################################
#   Structure 3
##############################################################

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_4'] > df['nq_ema_25'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'] > df['nq_ema_200'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_200'] > df['nq_ema_1600'], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_1600'] > df['nq_ema_12800'], 1, 0)

# Print the DataFrame
print(df)

##############################################################
#   Structure 4 (special)
##############################################################

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_4'][0] > df['nq_ema_4'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'][0] > df['nq_ema_25'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_200'][0] > df['nq_ema_200'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_1600'][0] > df['nq_ema_1600'][1], 1, 0)

# Print the DataFrame (Timeframe 1m)
print(df)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_4'][0] > df['nq_ema_4'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'][0] > df['nq_ema_25'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_200'][0] > df['nq_ema_200'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_1600'][0] > df['nq_ema_1600'][1], 1, 0)

# Print the DataFrame (Timeframe 4m)
print(df)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_4'][0] > df['nq_ema_4'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'][0] > df['nq_ema_25'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_200'][0] > df['nq_ema_200'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_1600'][0] > df['nq_ema_1600'][1], 1, 0)

# Print the DataFrame (Timeframe 15m)
print(df)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_4'][0] > df['nq_ema_4'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_25'][0] > df['nq_ema_25'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_200'][0] > df['nq_ema_200'][1], 1, 0)

# Create a column to track when a crossover occurs
df['crossover'] = np.where(df['nq_ema_1600'][0] > df['nq_ema_1600'][1], 1, 0)

# Print the DataFrame (Timeframe 60m)
print(df)


##############################################################
#   Structure 
##############################################################
#   Structure 
##############################################################
#   Structure 
##############################################################
#   Structure 
##############################################################
#   Structure 
##############################################################
#   Structure 
##############################################################


##############################################################
#   Structure 6 (special)
##############################################################
df['nq_ema_1'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_2'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_4'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()

df['nq_ema_2'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_4'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_4'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()

##############################################################
#   Structure 4444 (Special)
##############################################################
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_800'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_800'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_1600'] = df['nq_close'].ewm(span=100).mean()

##############################################################
#   Structure 6 (special)
##############################################################
df['nq_ema_1'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_2'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_4'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()

df['nq_ema_2'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_4'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_4'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_800'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_800'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_1600'] = df['nq_close'].ewm(span=100).mean()

##############################################################
#   Structure 6 (special)
##############################################################
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_800'] = df['nq_close'].ewm(span=100).mean()

df['nq_ema_6'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_8'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_16'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_25'] = df['nq_close'].ewm(span=25).mean()
df['nq_ema_50'] = df['nq_close'].ewm(span=50).mean()
df['nq_ema_100'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_400'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_800'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_1600'] = df['nq_close'].ewm(span=100).mean()

##############################################################
#   Structure 8 (special)
##############################################################
df['nq_ema_3200'] = df['nq_close'].ewm(span=100).mean()
df['nq_ema_6400'] = df['nq_close'].ewm(span=100).mean()