import random
import time

def read_temp_simulated():
    # Simulate temperature readings in Celsius
    temp_c = random.uniform(20.0, 30.0)  # Random temperature between 20°C and 30°C
    temp_f = temp_c * 9.0 / 5.0 + 32.0  # Convert to Fahrenheit
    return temp_c, temp_f

try:
    while True:
        temp_c, temp_f = read_temp_simulated()
        print(f"Simulated Temperature: {temp_c:.2f}°C / {temp_f:.2f}°F")
        time.sleep(1)  # Wait for 1 second before the next reading
except KeyboardInterrupt:
    print("Program terminated")