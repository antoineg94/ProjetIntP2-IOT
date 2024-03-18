from gpiozero import LED

class Led:
    
    def __init__(self,ledName = None, ledPin=None):
        self.ledName = ledName
        self.ledPin = LED(ledPin)
    
    def getLedName(self):
        return self.ledName
    
    def getLedPin(self):
        return self.ledPin
    
    def getLedState(self):
        return self.ledState
    
    def setLedState(self, ledState):
        self.ledState = ledState
    
    def turnOn(self):
        self.ledPin.on()
        self.ledState = True
        
    def turnOff(self):
        self.ledPin.off()
        self.ledState = False
     
    def Flash(self):
        self.ledPin.blink() 
          
    
    
    
    
        
        