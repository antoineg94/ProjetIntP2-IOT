#/usr/bin/python3

import AlertStorageClass
import API_Calls
import API_ResponseClass
from datetime import date
import time
from gpiozero import TonalBuzzer,Button,LED
import RPi.GPIO as GPIO
import math
from gpiozero.tones import Tone
import threading

exit_event = threading.Event()
global wait_time_inside_thread, delay_checking_new_data

wait_time_inside_thread = 50 #Seconds
delay_checking_new_data = 45 #Seconds

def TakeMedicationTest(exit_event, wait_time_inside_thread):
    while not button.is_pressed:
        alertor()
        led.on()
        if button.is_pressed:
            print('Medication taken')
            led.off()
            stopAlertor()
        return


dht_thread = threading.Thread(target=TakeMedicationTest, args=(exit_event,wait_time_inside_thread,))







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

def CheckAlerts():
    # Check if there are any alerts for today
    today = date.today()
    print(today)
    for alert in alertStorage.alertList:
        if alert.getDateOfIntake() == today & alert.getIsMediactionTaken() == False:
            todayAlerts.addAlert(alert)
    print(todayAlerts)

def TakeMedication():
	buzzer.playsong(buzzerSong)
	(LED(15)).on()
	if button.is_pressed:
		print('Medication taken')
		return



    
def alertor():
    buzzer.play(Tone(220.0)) 
    time.sleep(1)
        
def stopAlertor():
    buzzer.stop()
            
def destroy():
    buzzer.close()  

def UpdateAlerts():
    #Update the alert in the API
    #alerts = api.set_data("api/alerts/index")

    pass

def main():
    print('debut')
    dht_thread.start()
        
        

if __name__ == "__main__":
    try:
        
        main()
    except KeyboardInterrupt:
        print("Exiting...")

    except Exception as e:
        print(e)
        
    finally:
        print("Done")
  

