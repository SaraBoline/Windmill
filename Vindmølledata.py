from machine import Pin, PWM
from neopixel import Neopixel
import time

# Define pins
MOTOR_PWM_PIN = 26  # Motor connected to GP26
BUTTON_PIN = 20     # Start button connected to GP20
NEOPIXEL_PIN = 28   # NeoPixel connected to GP28

# Set up motor PWM
motor_pwm = PWM(Pin(MOTOR_PWM_PIN))
motor_pwm.freq(5000)  # Set PWM frequency to 5kHz
motor_pwm.duty_u16(0)  # Start with motor off

# Set up button (PULL_UP: active LOW when pressed)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Set up NeoPixel (5 pixels, change if needed)
num_pixels = 5
pixels = Neopixel(num_pixels, 0, NEOPIXEL_PIN, "RGB")  

# Wind strength data (1-5 scale)
wind_data = [2, 2, 1, 1, 2, 3, 2, 3, 3, 3, 4, 4, 3, 3, 4, 4, 4, 5, 5, 4, 3, 5]
index = 0

# Wind strength to color mapping
wind_colors = [
    (255, 0, 0),    # 1 - Red
    (0, 255, 0),    # 2 - Green
    (0, 0, 255),    # 3 - Blue
    (255, 255, 0),  # 4 - Yellow
    (255, 0, 255)   # 5 - Magenta
]

def set_color(color):
    """Set all NeoPixels to the given color."""
    for i in range(num_pixels):
        pixels.set_pixel(i, color)
    pixels.show()

def blink_neopixel():
    """Blink NeoPixel white 3 times when the wind data array ends."""
    for _ in range(3):
        set_color((255, 255, 255))  # White
        time.sleep(0.3)
        set_color((0, 0, 0))  # Off
        time.sleep(0.3)

def run_windmill():
    """Runs the windmill based on wind data."""
    global index
    while not button.value():  # Runs while button is pressed (LOW)
        wind_strength = wind_data[index]  # Get current wind strength
        
        set_color(wind_colors[wind_strength - 1])  # Update NeoPixel color
        
        duty_cycle = wind_strength * 13000  # Scale wind strength (1-5) to PWM (0-65535)
        motor_pwm.duty_u16(duty_cycle)
        
        time.sleep(1)  # Wait for 1 second
        index += 1

        # When the wind data array ends
        if index >= len(wind_data):
            blink_neopixel()
            index = 0  # Restart from the beginning

    # Stop motor and turn off NeoPixel when button is released
    motor_pwm.duty_u16(0)
    set_color((0, 0, 0))  # Turn off NeoPixel

try:
    while True:
        if not button.value():  # Start when button is pressed
            run_windmill()
        time.sleep(0.1)  # Small delay to avoid excessive CPU usage

except KeyboardInterrupt:
    motor_pwm.duty_u16(0)  # Stop motor on exit
    set_color((0, 0, 0))  # Turn off NeoPixel
    print("Program stopped.")

