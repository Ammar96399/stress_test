import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_violin_from_csv(csv_file_path):
    # Read the data from the CSV file
    df = pd.read_csv(csv_file_path)

    # Create a violin plot for CPU percentage using the 'load' field
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='load', y='CPU (%)', data=df)
    plt.title('Violin Plot of CPU Percentage by Load')
    plt.xlabel('Load')
    plt.ylabel('CPU (%)')
    plt.grid(True)

    plt.savefig('test.png')
    plt.close()

# Example usage
csv_file_path = 'single_test/rbpi4/ten_values/ten_values_union/cpu_usage_union_classified.csv'
plot_violin_from_csv(csv_file_path)
