import machine
import time

adc = machine.ADC()
apin = adc.channel(pin='P16')


while True:
  millivolts = apin.voltage()
  celsius = (millivolts - 500.0) / 10.0

  print(celsius)
  
  time.sleep(1)
  