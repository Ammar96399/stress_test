#!/bin/sh
sudo apt update
echo "Upgrading ..."
sudo apt upgrade -y
echo "Installing stress ng"
sudo apt install stress-ng -y
echo "Installing psutil"
sudo apt install python3-psutil -y

# Log file for CPU usage
LOGFILE_1="cpu_usage_psi.csv"

# Main script logic
echo "Starting main script..."

# Log CPU usage every INTERVAL seconds
python pytest.py $LOGFILE_1 -l 0.1 &

SCRIPT_PID=$!

echo "Stress testing with PSI ..."

echo "Stressing at 20%"
stress-ng -c 0 -l 20 -t 180s --cpu-method psi & sleep 200;

echo "Stressing at 40%"
stress-ng -c 0 -l 40 -t 180s --cpu-method psi & sleep 200;

echo "Stressing at 60%"
stress-ng -c 0 -l 60 -t 180s --cpu-method psi & sleep 200;

echo "Stressing at 80%"
stress-ng -c 0 -l 80 -t 180s --cpu-method psi & sleep 200;

echo "Stressing at 100%"
stress-ng -c 0 -l 100 -t 180s --cpu-method psi & sleep 200;

kill $SCRIPT_PID

# Log CPU usage every INTERVAL seconds
python pytest.py $LOGFILE_1 -l 0.1 &

SCRIPT_PID=$!

echo "Stress testing with DIV8 ..."

echo "Stressing at 20%"
stress-ng -c 0 -l 20 -t 180s --cpu-method div8 & sleep 200;

echo "Stressing at 40%"
stress-ng -c 0 -l 40 -t 180s --cpu-method div8 & sleep 200;

echo "Stressing at 60%"
stress-ng -c 0 -l 60 -t 180s --cpu-method div8 & sleep 200;

echo "Stressing at 80%"
stress-ng -c 0 -l 80 -t 180s --cpu-method div8 & sleep 200;

echo "Stressing at 100%"
stress-ng -c 0 -l 100 -t 180s --cpu-method div8 & sleep 200;

kill $SCRIPT_PID

# Log CPU usage every INTERVAL seconds
python pytest.py $LOGFILE_1 -l 0.1 &

SCRIPT_PID=$!

echo "Stress testing with GCD ..."

echo "Stressing at 20%"
stress-ng -c 0 -l 20 -t 180s --cpu-method gcd & sleep 200;

echo "Stressing at 40%"
stress-ng -c 0 -l 40 -t 180s --cpu-method gcd & sleep 200;

echo "Stressing at 60%"
stress-ng -c 0 -l 60 -t 180s --cpu-method gcd & sleep 200;

echo "Stressing at 80%"
stress-ng -c 0 -l 80 -t 180s --cpu-method gcd & sleep 200;

echo "Stressing at 100%"
stress-ng -c 0 -l 100 -t 180s --cpu-method gcd & sleep 200;

kill $SCRIPT_PID

# Log CPU usage every INTERVAL seconds
python pytest.py $LOGFILE_1 -l 0.1 &

SCRIPT_PID=$!

echo "Stress testing with UNION ..."

echo "Stressing at 20%"
stress-ng -c 0 -l 20 -t 180s --cpu-method union & sleep 200;

echo "Stressing at 40%"
stress-ng -c 0 -l 40 -t 180s --cpu-method union & sleep 200;

echo "Stressing at 60%"
stress-ng -c 0 -l 60 -t 180s --cpu-method union & sleep 200;

echo "Stressing at 80%"
stress-ng -c 0 -l 80 -t 180s --cpu-method union & sleep 200;

echo "Stressing at 100%"
stress-ng -c 0 -l 100 -t 180s --cpu-method union & sleep 200;

kill $SCRIPT_PID

# Log CPU usage every INTERVAL seconds
python pytest.py $LOGFILE_1 -l 0.1 &

SCRIPT_PID=$!

echo "Stress testing with QUEENS ..."

echo "Stressing at 20%"
stress-ng -c 0 -l 20 -t 180s --cpu-method queens & sleep 200;

echo "Stressing at 40%"
stress-ng -c 0 -l 40 -t 180s --cpu-method queens & sleep 200;

echo "Stressing at 60%"
stress-ng -c 0 -l 60 -t 180s --cpu-method queens & sleep 200;

echo "Stressing at 80%"
stress-ng -c 0 -l 80 -t 180s --cpu-method queens & sleep 200;

echo "Stressing at 100%"
stress-ng -c 0 -l 100 -t 180s --cpu-method queens & sleep 200;

kill $SCRIPT_PID

echo "Main script finished."

sudo shutdown