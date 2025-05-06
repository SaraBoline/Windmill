from machine import ADC, Pin
import time

# definere adc på Pin (gpio 28)
adc = ADC(Pin(28))

# læs den her pin i et loop
while True:
    value = adc.read_u16()  # Reads a 16-bit value (0–65535)
    print("ADC Reading:", value)
    time.sleep(0.5)



from machine import ADC, Pin
import time

adc = ADC(Pin(28))

while True:
    value = adc.read_u16()  # Reads a 16-bit value (0–65535)
    voltage = (value / 65535) * 3.3  # Convert to voltage
    print(f"ADC Reading: {value} | Voltage: {voltage:.2f} V")
    time.sleep(0.5)
