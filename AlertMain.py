#/usr/bin/python3

import AlertStorageClass
import API_Calls
import API_ResponseClass
from datetime import date,time


global alertStorage, todayAlerts
alertStorage = AlertStorageClass.AlertStorage()
todayAlerts = AlertStorageClass.AlertStorage()


def GetAlertsFromAPI():
    # Get alerts from API
    api = API_Calls.API_Calls("http://192.168.1.151:8000")
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
    
    pass

def UpdateAlerts():
    # Update the alert in the API
    pass

def CreateAlarmForTakingMedication(ColorLed, Buzzer, TimeToTakeMedication,Type):
    # Create an alarm for taking medication
    match(Type):
        case "Warning":
            ColorLed.setColor("Red")
            Buzzer.setBuzzer(1)
        case "Info":
            ColorLed.setColor("Blue")
            Buzzer.setBuzzer(0)
        case "Success":
            ColorLed.setColor("Green")
            Buzzer.setBuzzer(0)
        case "Error":
            ColorLed.setColor("Red")
            Buzzer.setBuzzer(1)
        case _:
            print("Invalid Type")
    pass
    # 
    pass




def main():
    GetAlertsFromAPI()
    print(alertStorage)
    pass

if __name__ == "__main__":
    try:
        
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        pass
    except Exception as e:
        print(e)
        pass
    finally:
        print("Done")
        pass
    
#
 
    
    