import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_violin_at_breaks(power_file, output_file, palette):
    # Load the power consumption CSV data
    power_df = pd.read_csv(power_file)

    # Convert the Unix time column to datetime
    power_df['Unix time'] = pd.to_datetime(power_df['Unix time'], unit='s')

    # Calculate the relative time (seconds since the start)
    start_time_power = power_df['Unix time'].min()
    power_df['Relative Time (s)'] = (power_df['Unix time'] - start_time_power).dt.total_seconds()

    # Identify breaks in the data (e.g., time gaps larger than a threshold)
    threshold = 100  # Define your own threshold for a break in seconds
    power_breaks = power_df['Relative Time (s)'].diff().abs() > threshold

    # Create a figure and axis
    fig, ax1 = plt.subplots(figsize=(14, 8))

    # Plot Power (W) on the primary y-axis
    color1 = palette[0]
    ax1.set_xlabel('Relative Time (s)')
    ax1.set_ylabel('Power (W)', color=color1)
    sns.lineplot(x='Relative Time (s)', y='Power (W)', data=power_df, ax=ax1, color=color1, label='Power (W)')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True)
    ax1.set_ylim(0)  # Start the y-axis at 0 for Power (W)

    # Adding violin plots
    segment_indices = power_df[power_breaks].index

    for idx in segment_indices:
        start_idx = max(0, idx - 10)  # Adjust to include more data points before the break
        end_idx = min(len(power_df), idx + 10)  # Adjust to include more data points after the break
        segment_df = power_df.iloc[start_idx:end_idx]
        sns.violinplot(x='Relative Time (s)', y='Power (W)', data=segment_df, ax=ax1, color=color1, alpha=0.3)

    # Set the x-axis labels and rotate them for better readability
    fig.autofmt_xdate()

    # Set the title of the plot
    plt.title('Power Consumption Over Time with Breaks', fontsize=16)

    # Create a combined legend for both lines
    line1 = ax1.lines[0]
    ax1.legend([line1], ['Power (W)'], loc='upper left')

    # Save the plot to the specified file
    fig.tight_layout()
    plt.savefig(output_file)
    plt.close(fig)

def process_folders(base_path, palette):
    algos = ["ackermann", "div8", "gcd", "psi", "union"]
    for algo in algos: 
        folder_path = os.path.join(base_path, "ten_values_"+algo)
        if os.path.isdir(folder_path):
            power_file = os.path.join(folder_path, 'power_usage_'+algo+'.csv')
            output_file = os.path.join(folder_path, 'power_violin_'+algo+'.png')

            if os.path.exists(power_file):
                print(f"Processing {folder_path}...")
                plot_violin_at_breaks(power_file, output_file, palette)
            else:
                print(f"Skipping {folder_path}: missing required files.")

# Define the base path where your folders are located
base_path = 'single_test/rbpi5/ten_values'

# Define the color palette to use
palette = sns.color_palette("muted", 1)  # You can change "muted" to any other palette

# Process all folders in the base path
process_folders(base_path, palette)
