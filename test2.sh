#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install stress-ng python3-psutil -y

# Define log file names and CPU methods
#LOGFILES=("cpu_usage_psi.csv" "cpu_usage_div8.csv" "cpu_usage_gcd.csv" "cpu_usage_union.csv" "cpu_usage_ackermann.csv")
LOGFILES=("cpu_usage_div8.csv" "cpu_usage_union.csv")

#CPU_METHODS=("psi" "div8" "gcd" "union" "ackermann")
CPU_METHODS=("div8" "union")

# Function to perform stress test
perform_stress_test() {
    for i in {0..2}; do
        LOGFILE=${LOGFILES[$i]}
        CPU_METHOD=${CPU_METHODS[$i]}

        echo "Starting main script with $LOGFILE ..."
        python pytest.py "$LOGFILE" -l 0.1 &
        SCRIPT_PID=$!

        echo "Stress testing with $CPU_METHOD ..."
        for LOAD in 10 20 30 40 50 60 70 80 90 100; do
            echo "Stressing at $LOAD%"
            stress-ng -c 0 -l $LOAD -t 1s --cpu-method "$CPU_METHOD"
            sleep 240
        done

        sleep 240

        kill $SCRIPT_PID
    done
}

# Run the stress test
perform_stress_test

echo "Main script finished."
