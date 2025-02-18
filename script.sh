#!/bin/bash

# Number of times to run the command
num_iterations=1200  # Change as needed
number_of_pages=250
wait_time=15

for ((i=1; i<=num_iterations; i++))
do
    echo "Running iteration $i... running pages.py with $number_of_pages pages"
    python3 pages.py "$number_of_pages"
    
    echo -e "\tIteration $i complete. Waiting for $wait_time seconds..."
    sleep $wait_time
done
