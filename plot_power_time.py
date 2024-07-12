import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('single_test/rbpi3/ten_values/pi3-work.csv')

# Convert the Unix time column to datetime
df['Unix time'] = pd.to_datetime(df['Unix time'], unit='s')

# Plot the data
plt.figure(figsize=(14, 7))
sns.lineplot(x='Unix time', y='Power (W)', data=df)
plt.title('Power Consumption Over Time')
plt.xlabel('Time')
plt.ylabel('Power (W)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
