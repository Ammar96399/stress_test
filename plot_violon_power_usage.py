import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm

def plot_violin_from_csv(csv_file_path, output_file):
    # Read the data from the CSV file
    df = pd.read_csv(csv_file_path)

    # Create a violin plot for CPU percentage using the 'load' field
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='load', y='CPU (%)', data=df)
    plt.title('Violin Plot of CPU Percentage by Load')
    plt.xlabel('Load')
    plt.ylabel('CPU (%)')
    plt.grid(True)

    plt.savefig(output_file)
    plt.close()


def process_folders(base_path):
    algos = ["ackermann", "div8", "gcd", "psi", "union"]
    for i in tqdm(range(len(algos)), desc="Processing algos"):
        folder_path = os.path.join(base_path, "ten_values_"+algos[i])
        if os.path.isdir(folder_path):
            if os.path.exists(os.path.join(folder_path, 'cpu_usage_'+algos[i]+'_manually_classified.csv')):
                power_file = os.path.join(folder_path, 'cpu_usage_'+algos[i]+'_manually_classified.csv')
            else:
                power_file = os.path.join(folder_path, 'cpu_usage_'+algos[i]+'_classified.csv')

            output_file = os.path.join(folder_path, 'violon_cpu_'+algos[i]+'.png')

            if os.path.exists(power_file):
                plot_violin_from_csv(power_file, output_file)
            else:
                print(f"Skipping {folder_path}: missing required files.")


# Define the base path where your folders are located
base_path = 'single_test/rbpi3/ten_values'

# Process all folders in the base path
process_folders(base_path)
