import machine
import time
from machine import Pin
from machine import Timer
from machine import ADC

LightSensorPin = 'P20'  # sensor connected to P16. Valid pins are P13 to P20.

lightPin = Pin(LightSensorPin, mode=Pin.IN)  # set up pin mode to input
#
# create an ADC object bits=10 means range 0-1024 the lower value the less light detected
adc = ADC(bits=10)
# create an analog pin on P16;  attn=ADC.ATTN_11DB measures voltage from 0.1 to 3.3v
apin = adc.channel(attn=ADC.ATTN_11DB, pin=LightSensorPin)

while True:
    val = apin()  # read an analog value
    print("Value", val)
    time.sleep(1)  # wait 1 sec


# Motion
# motionDetected = 1
# noMotionDetected = 0
# hold_time_sec = 0.1
# pir = Pin('P4',mode=Pin.IN)

# chrono = Timer.Chrono()
# chrono.start()

# print("Starting Detection")
# while True:
#     if pir()==motionDetected:
#         print(chrono.read(), "Motion Detected!")
#     # print(pir())

#     if pir()==noMotionDetected:
#         pass

#     time.sleep(hold_time_sec)


# temperature
# adc = machine.ADC()
# apin = adc.channel(pin='P16')


# while True:
#   millivolts = apin.voltage()
#   celsius = (millivolts - 500.0) / 10.0

#   print(celsius)

#   time.sleep(1)
