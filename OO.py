import pyb
import machine
from time import ticks_ms, sleep_ms
##it could be possible to add a led's checker to add more complexity/security
##style: while led2 == 1: ....
###and/or a destruction of alls files if two wrong entrances are detected, ... in this case  maybe import a peace/attack file?

sw = pyb.Switch()

t1 = ticks_ms()
t2 = ticks_ms()
n = 0

while (t2 - t1) < 5000:
    pyb.LED(3).on()
    t2 = ticks_ms()
    if sw.value():
        n += 1
    sleep_ms(500)#The sensitivity of the switch button
pyb.LED(3).off()
if n == 2:
    pyb.usb_mode('VCP+MSC')
else:
    while n < 100:##This is not possible, but open a stream by an other ucontroller, ..., maybe, so you can add, a led_pulse with a ms of delay to shunt this possibility. In this case, if it doesn't work, for sure you loose your board in an infinite loop... So beautifull!
        sleep_ms(1000)
        pyb.LED(2).toggle()