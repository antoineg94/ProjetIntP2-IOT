#/usr/bin/python3

import AlertStorageClass
import API_Calls
import API_ResponseClass
import time
from gpiozero import TonalBuzzer,Button,LED
import RPi.GPIO as GPIO
import math
from gpiozero.tones import Tone
import threading

exit_event = threading.Event()
button_exit_event = threading.Event()


global alertStorage, todayAlerts
alertStorage = AlertStorageClass.AlertStorage()
todayAlerts = AlertStorageClass.AlertStorage()

api = API_Calls.API_Calls("http://192.168.1.151:8000")

buzzer = TonalBuzzer(17)
button = Button(18)
led = LED(22)

def GetAlertsFromAPI():
    # Get alerts from API
    alerts = api.get_data("api/alerts/index")
    print(alerts)

# def CheckAlerts():
#     # Check if there are any alerts for today
#     today = date.today()
#     print(today)
#     for alert in alertStorage.alertList:
#         if alert.getDateOfIntake() == today & alert.getIsMediactionTaken() == False:
#             todayAlerts.addAlert(alert)
#     print(todayAlerts)

# def TakeMedication():
# 	buzzer.playsong(buzzerSong)
# 	(LED(15)).on()
# 	if button.is_pressed:
# 		print('Medication taken')
		# return

    
def alertor(exit_event):
    while not exit_event.is_set():
        buzzer.play(Tone(220.0))
        time.sleep(5)
        buzzer.stop()
        time.sleep(5)
        
def stopAlertor():
    buzzer.stop()
            
def destroy():
    buzzer.close()  

def FlashLed(exit_event):
    while not exit_event.is_set():
        led.on()
        time.sleep(5)
        led.off()
        time.sleep(5)


def UpdateAlerts():
    #Update the alert in the API
    #alerts = api.set_data("api/alerts/index")

    pass

def TakeMedicationTest(exit_event):
    while not exit_event.is_set():
        alertor()
        FlashLed()
        

def CheckForButtonPress(exit_event):
    while not exit_event.is_set():
        if button.is_pressed:
            print('Medication taken')
            button_exit_event.set()
        time.sleep(0.1)

alertor_thread = threading.Thread(target=alertor, args=(button_exit_event,))
FlashLed_thread = threading.Thread(target=FlashLed, args=(button_exit_event,))

# take_medic_thread = threading.Thread(target=TakeMedicationTest, args=(button_exit_event,))
button_thread = threading.Thread(target=CheckForButtonPress,args=(exit_event,))


def main():
 
    # take_medic_thread.start()
    alertor_thread.start()
    FlashLed_thread.start()
    button_thread.start()
    
def resetButtonEvent():
    button_exit_event.clear()
    
    print("Button event cleared")
    return

def stop():
    exit_event.set()
    button_exit_event.set()
    alertor_thread.join()
    FlashLed_thread.join()
    button_thread.join()
    print("Exiting...")
    exit()
        

if __name__ == "__main__":
    try:
        while not exit_event.is_set():
         main()
         time.sleep(4)
         resetButtonEvent()

    except KeyboardInterrupt:
        print("Exiting...")
        exit_event.set()
        stop()

    except Exception as e:
        print(e)
        
    finally:
        print("Done")
  

