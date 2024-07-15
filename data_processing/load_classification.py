import pandas as pd


def find_consecutive_zeros(file_path, output_path):
    df = pd.read_csv(file_path)

    zero_detected = False
    current_load = 10

    for i in range(len(df)):
        if i < len(df) - 2 and zero_detected == False and (df.iloc[i]['CPU (%)'] == 0.0 and df.iloc[i + 1]['CPU (%)'] == 0.0 and df.iloc[i + 2]['CPU (%)'] == 0.0):
            zero_detected = True
            current_load = current_load + 10
            print("Zero detected")
        if df.iloc[i]['CPU (%)'] < current_load + 5 and df.iloc[i]['CPU (%)'] > current_load - 5:
            zero_detected = False
        if zero_detected:
            df.loc[i, 'load'] = 0
        else:
            df.loc[i, 'load'] = current_load

    df.to_csv(output_path, index=False)


file_path = 'single_test/rbpi4/ten_values/ten_values_union/cpu_usage_union.csv'
output_path = 'single_test/rbpi4/ten_values/ten_values_union/cpu_usage_union_classified.csv'
find_consecutive_zeros(file_path, output_path)
