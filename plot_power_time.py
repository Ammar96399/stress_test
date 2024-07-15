import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_power_usage(power_file, output_file):

    # Load the power consumption CSV data
    power_df = pd.read_csv(power_file)

    # Convert the Unix time columns to datetime
    power_df['Unix time'] = pd.to_datetime(power_df['Unix time'], unit='s')

    # Create a figure and a primary axis
    fig, ax1 = plt.subplots(figsize=(14, 8))

    # Plot Power (W) on the primary y-axis
    color = sns.color_palette("Set2")[0]
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Power (W)', color=color)
    line1 = sns.lineplot(x='Unix time', y='Power (W)', data=power_df, ax=ax1, color=color, label='Power (W)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True)
    ax1.set_ylim(0)
    ax1.get_legend().remove()

    # Set the x-axis labels and rotate them for better readability
    ax1.set_xlabel('Time')
    fig.autofmt_xdate()

    # Set the title of the plot
    plt.title('CPU Usage Over Time')

    # Save the plot to the specified file
    fig.tight_layout()
    plt.savefig(output_file)
    plt.close(fig)


def process_folders(base_path):
    algos = ["ackermann", "div8", "gcd", "psi", "union"]
    for algo in algos:
        folder_path = os.path.join(base_path, "ten_values_"+algo)
        if os.path.isdir(folder_path):
            power_file = os.path.join(folder_path, 'power_usage_'+algo+'.csv')
            output_file = os.path.join(folder_path, 'power_'+algo+'.png')

            if os.path.exists(power_file):
                print(f"Processing {folder_path}...")
                plot_power_usage(power_file, output_file)
            else:
                print(f"Skipping {folder_path}: missing required files.")


# Define the base path where your folders are located
base_path = 'single_test/rbpi3/ten_values'

# Process all folders in the base path
process_folders(base_path)
