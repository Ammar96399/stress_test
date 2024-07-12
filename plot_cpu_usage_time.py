import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
cpu_df = pd.read_csv('single_test/rbpi3/five_values_psi/cpu_usage.csv')

# Convert the Timestamp (s) column to datetime
cpu_df['Timestamp (s)'] = pd.to_datetime(cpu_df['Timestamp (s)'], unit='s')

# Plot the data
plt.figure(figsize=(14, 7))
sns.lineplot(x='Timestamp (s)', y='CPU (%)', data=cpu_df)
plt.title('CPU Usage Over Time')
plt.xlabel('Time')
plt.ylabel('CPU Usage (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
