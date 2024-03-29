#!/usr/bin/env python3
from gpiozero import TonalBuzzer,Button,LED
from gpiozero.tones import Tone
import time
import math

buzzer = TonalBuzzer(17)
button = Button(18)
led = LED(22)

def loop():
    while True:
        if not button.is_pressed:  # if button is pressed
            buzzer.play(Tone(220.0))
            led.on()
            time.sleep(0.2)
            buzzer.stop()
            led.off()
            time.sleep(0.2)
        else :
            buzzer.stop()
            print ('Medication Taken')
            break
            
def destroy():
    buzzer.close()                  
    led.off()

if __name__ == '__main__':     # Program entrance
    print ('Buzzer is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()