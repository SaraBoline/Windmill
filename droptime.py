from machine import ADC, Pin
import time

# definere kondensator
kondensator = "K1000"  # Change this to match the capacitor's value or label

#definere pin og filnavne 
adc = ADC(Pin(28))
filename = "adc_measurements.csv"
time_column = f"{kondensator}_time"
adc_column = f"{kondensator}_value"

# header CSV
with open(filename, "a") as file:
    file.write(f"{time_column},{adc_column}\n")

#Indsamle data 
start_time = None
timing = False

while True:
    value = adc.read_u16()

    if not timing and value < 65535:
        print("Start detected")
        start_time = time.time()
        timing = True

    if timing:
        elapsed_time = round(time.time() - start_time, 2)
        print(f"{elapsed_time}s | ADC: {value}")

        # Log data to CSV
        with open(filename, "a") as file:
            file.write(f"{elapsed_time},{value}\n")

        if value < 30000:
            print("Threshold reached, stopping.")
            break

    time.sleep(0.5)

