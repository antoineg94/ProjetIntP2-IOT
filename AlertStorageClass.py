import API_ResponseClass

class AlertStorage:
    global alertList
    alertList = {}
    User = None
    
    
    def __init__(self, alertList = None, User = None):
        self.alertList = []  
        self.User = User
    
    def __str__(self):
        return f"Alerts: {self.alertList}"
    
    def addAlert(self, alert):
        self.alertList.append(alert)
    
    def removeAlert(self, alert):
        self.alertList.remove(alert)
        
    

    


