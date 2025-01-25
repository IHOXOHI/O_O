##############
### IMPORTANT: You can rename this file 'boot.py', but after no acces to the board... forever!
### you can uncomment the lines started by #!# to preserve the possibility to communicate... but you loose the full security... 

from machine import Pin, PWM
from time import sleep_ms, ticks_ms

bL = Pin(17, Pin.IN, Pin.PULL_UP)

led = PWM(Pin(25))
led.freq(20)

t1 = ticks_ms()
t2 = ticks_ms()
n = 0
while (t2 - t1) < 10000:
    if bL.value() == 0:
        n += 1
        led.duty_u16(1000)
        sleep_ms(500)
        led.duty_u16(0)
    t2 = ticks_ms()

if n == 1:
    import go.py
#!#if n == 3:
#!#    fil = open('boot.py', 'w')
#!#    fil.write('import machine\n')
#!#    fil.close()
else:
    led.duty_u16(100)
    while n < 100:
        sleep_ms(10)
