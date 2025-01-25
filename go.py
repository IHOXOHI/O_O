### uncomment the lines to rewrite the boot.py... in this case the board could communicate, but the full security is broken.
from machine import Pin, SPI
from micropython_rfm9x import *
from time import sleep_ms

bR = Pin(16, Pin.IN, Pin.PULL_UP)
#bL = Pin(17, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

def check_buttons():
    if bR.value() == 0:
        led.on()
        rfm9x.send(b'Open The Door, Please.')
        sleep_ms(500)
        led.off()
#    if bL.value() == 0:
 #       led.on()
  #      fil = open('boot.py', 'w')
   #     fil.write('import machine\n')
    #    fil.close()
     #   sleep_ms(500)
      #  led.off()

RADIO_FREQ_MHZ = 433.0
CS = Pin(13, Pin.OUT)
RESET = Pin(7, Pin.OUT)
spi = SPI(1, baudrate=1_000_000, sck=Pin(14), mosi=Pin(15), miso=Pin(12))
rfm9x = RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.hight_power = 5

while 1:
    check_buttons()
    sleep_ms(10)
