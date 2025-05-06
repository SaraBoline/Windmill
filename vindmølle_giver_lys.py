from machine import ADC, PWM, Pin
import time

wind = ADC(Pin(26))
led = 16

pwm = PWM(Pin(led))
pwm.freq(1000)

#brug værdier mellem 10000 (0.5V) og 60000(3V)
#spring på 10000 svarer til ca. 0.5V

pwm.duty_u16(1000)
volts = 0

while True:
    val = wind.read_u16()
    print(val)
    pwm.duty_u16(val*2)
    time.sleep(0.5)
