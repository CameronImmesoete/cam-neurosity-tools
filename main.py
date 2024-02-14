from neurosity import NeurositySDK
from dotenv import load_dotenv
import os
import numpy as np
import time

load_dotenv()

neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
})

neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

def record_and_aggregate_data(num_captures, num_seconds, raw_file_name, agg_file_name):
    # Initialize lists to store raw data and aggregated data
    raw_data = []
    aggregated_data = {"average": [], "median": [], "high": [], "low": []}
    
    # Define callback function to collect raw data
    def raw_callback(data):
        raw_data.append(data)
    
    # Subscribe to raw brainwaves
    unsubscribe_pbb = neurosity.brainwaves_power_by_band(raw_callback)
    
    # Wait for a short time to ensure data collection starts
    time.sleep(2)
    
    # Loop through each second
    for _ in range(num_seconds):
        # Loop to capture data for each second
        captures_this_second = []
        for _ in range(num_captures):
            captures_this_second.append(raw_data.pop(0))
            time.sleep(1 / num_captures)
        
        # Calculate average, median, high, and low values for each band
        averages = np.mean(captures_this_second, axis=0)
        medians = np.median(captures_this_second, axis=0)
        highs = np.max(captures_this_second, axis=0)
        lows = np.min(captures_this_second, axis=0)
        
        # Append aggregated data to the list
        aggregated_data["average"].append(averages)
        aggregated_data["median"].append(medians)
        aggregated_data["high"].append(highs)
        aggregated_data["low"].append(lows)
        
    # Unsubscribe from raw brainwaves
    unsubscribe_pbb()
    
    # Write raw data to a file
    with open(raw_file_name, 'w') as f:
        for epoch in raw_data:
            f.write(str(epoch) + '\n')
    
    # Write aggregated data to a file
    with open(agg_file_name, 'w') as f:
        for key, values in aggregated_data.items():
            f.write(key + '\n')
            for value in values:
                f.write(str(value) + '\n')

# Example usage
# record_and_aggregate_data(4, 10, "raw_data.txt", "aggregated_data.txt")
