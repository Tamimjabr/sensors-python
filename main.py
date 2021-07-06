import machine
import time
import pycom
from machine import Pin
from machine import Timer
from machine import ADC

# LightSensorPin = 'P20'  # sensor connected to P20. Valid pins are P13 to P20.

# lightPin = Pin(LightSensorPin, mode=Pin.IN)  # set up pin mode to input
# #
# # create an ADC object bits=10 means range 0-1024 the lower value the less light detected
# adc = ADC(bits=10)
# # create an analog pin on P16;  attn=ADC.ATTN_11DB measures voltage from 0.1 to 3.3v
# apin = adc.channel(attn=ADC.ATTN_11DB, pin=LightSensorPin)

# while True:
#     val = apin()  # read an analog value
#     print("Value", val)
#     time.sleep(1)  # wait 1 sec


# temperature
# adc = machine.ADC()
# apin = adc.channel(pin='P16')


# while True:
#   millivolts = apin.voltage()
#   celsius = (millivolts - 500.0) / 10.0

#   print(celsius)

#   time.sleep(1)


# Motion
# motionDetected = 1
# noMotionDetected = 0
# hold_time_sec = 0.1
# pir = Pin('P4', mode=Pin.IN)

# chrono = Timer.Chrono()
# chrono.start()

# print("Starting Detection")
# while True:
#     if pir() == motionDetected:
#         print(chrono.read(), "Motion Detected!")
#     # print(pir())

#     if pir() == noMotionDetected:
#         pass

#     time.sleep(hold_time_sec)

# # Button

# p_in = Pin('P10', mode = Pin.IN)  # SENSOR BUTTON FORM ELEKTROKIT
# # p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)  # A REGULAR BUTTON PULLED UP

# while(1):
#     val = p_in() # get value, 0 or 1
#     if val == 1:
#         print("NOT PRESSED !")
#     else:
#         print("PRESSED !")

#     time.sleep(1)


powerOn = False
pycom.heartbeat(False)

p_in = Pin('P10', mode=Pin.IN)  # SENSOR BUTTON FORM ELEKTROKIT


while(1):
    val = p_in()  # get value, 0 or 1
    if val == 0:
        if (powerOn):
            powerOn = False
            print(powerOn)
        else:
            powerOn = True
            print(powerOn)

            motionDetected = 1
            noMotionDetected = 0
            hold_time_sec = 0.1
            pir = Pin('P4', mode=Pin.IN)

            chrono = Timer.Chrono()
            chrono.start()

            print("Starting Detection")
            pycom.rgbled(0x00FF00)  # Green
            time.sleep(1)
            pycom.rgbled(0x000000)
            while True:
                if pir() == motionDetected:
                    print(chrono.read(), "Motion Detected!")
                    pybytes.send_signal(1, "Motion Detected!")
                    print("sending: Motion Detected!")
                    pycom.rgbled(0xFF0000)  # Red
                    time.sleep(10)

                # print(pir())

                if pir() == noMotionDetected:
                    pycom.rgbled(0x000000)
                    pass
                time.sleep(1)
                val2 = p_in()
                if val2 == 0:
                    powerOn = False
                    print("Stop detection")
                    pycom.rgbled(0x0000FF)  # blue
                    time.sleep(1)
                    pycom.rgbled(0x000000)
                    break
    time.sleep(1)

    # motionDetected = 1
    # noMotionDetected = 0
    # hold_time_sec = 0.1
    # pir = Pin('P4', mode=Pin.IN)

    # chrono = Timer.Chrono()
    # chrono.start()

    # print("Starting Detection")
    # while True:
    #     if pir() == motionDetected:
    #         print(chrono.read(), "Motion Detected!")
    #     # print(pir())

    #     if pir() == noMotionDetected:
    #         pass

    #     time.sleep(hold_time_sec)


# while True:
#     #The value can be a sensor reading being done here
#     value = 5

#     #Sending to pybytes in channel 1
#     pybytes.send_signal(1, value)
#     print("sending: {}".format(value))

#     #Send every 5 seconds
#     time.sleep(5)
