import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm

def calculate_stddev_for_algo(csv_file_path, algo):
    # Read the data from the CSV file
    df = pd.read_csv(csv_file_path)

    # Calculate standard deviation for each load
    stddev_data = df.groupby('load')['CPU (%)'].std().reset_index()
    stddev_data['Algorithm'] = algo
    return stddev_data

def plot_combined_stddev(base_path, output_file):
    algos = ["ackermann", "div8", "gcd", "psi", "union"]
    combined_data = pd.DataFrame()

    for algo in tqdm(algos, desc="Processing algos"):
        folder_path = os.path.join(base_path, "ten_values_"+algo)
        if os.path.isdir(folder_path):
            csv_file = os.path.join(folder_path, 'cpu_usage_'+algo+'_manually_classified.csv')
            if not os.path.exists(csv_file):
                csv_file = os.path.join(folder_path, 'cpu_usage_'+algo+'_classified.csv')

            if os.path.exists(csv_file):
                stddev_data = calculate_stddev_for_algo(csv_file, algo)
                combined_data = pd.concat([combined_data, stddev_data], ignore_index=True)
            else:
                print(f"Skipping {folder_path}: missing required files.")

    # Create a figure and a primary axis
    plt.figure(figsize=(14, 8))

    # Plot the combined standard deviation data
    sns.barplot(x='load', y='CPU (%)', hue='Algorithm', data=combined_data)
    plt.title('Standard Deviation of CPU Percentage by Load for Different Algorithms')
    plt.xlabel('Load')
    plt.ylabel('Standard Deviation of CPU (%)')
    plt.grid(True)

    # Save the plot to the specified file
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

# Define the base path where your folders are located
base_path = 'single_test/rbpi5/ten_values'
output_file = 'combined_stddev_plot.png'

# Process all folders in the base path and plot combined standard deviation
plot_combined_stddev(base_path, output_file)
