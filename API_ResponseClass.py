
class API_Response:
    
    def __init__(self, id=None, isMediactionTaken=False, calendar_id=None, dateOfIntake=None, hourOfIntake=None, medicationName=None):
        self.id = id
        self.isMediactionTaken = isMediactionTaken
        self.calendar_id = calendar_id
        self.dateOfIntake = dateOfIntake
        self.hourOfIntake = hourOfIntake
        self.medicationName = medicationName
        
    def __str__(self):
        return f"Alert {self.id} - {self.isMediactionTaken} - {self.calendar_id} - {self.dateOfIntake} - {self.hourOfIntake} - {self.medicationName}"
    
    def __eq__(self, API_Response) -> bool:
        return self.id == API_Response.id
    
    def getId(self):
        return self.id
    
    def getIsMediactionTaken(self):
        return self.isMediactionTaken
    
    def setIsMediactionTaken(self, isMediactionTaken):
        self.isMediactionTaken = isMediactionTaken
    
    def getCalendarId(self):
        return self.calendar_id
    
    def getDateOfIntake(self):
        return self.dateOfIntake
    
    def getHourOfIntake(self):
        return self.hourOfIntake
    
    def getMedicationName(self):
        return self.medicationName
    
    
    