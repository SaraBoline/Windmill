from machine import ADC, Pin
import time

# Initialize ADC on GPIO 28 (which is ADC2)
adc = ADC(Pin(28))

# Infinite loop to read every 0.5 seconds
while True:
    value = adc.read_u16()  # Reads a 16-bit value (0–65535)
    print("ADC Reading:", value)
    time.sleep(0.5)
