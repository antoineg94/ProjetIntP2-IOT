from gpiozero import Button

class Button:
        
        def __init__(self, buttonPin=None):
            self.buttonName = buttonName
            self.buttonPin = Button(buttonPin)
        
        def getButtonPin(self):
            return self.buttonPin
        
        def getButtonState(self):
            return self.buttonState

        def setButtonState(self, buttonState):
            self.buttonState = buttonState
        
        def whenPressed(self):
            self.buttonPin.when_pressed = self.setButtonState(True)
            #arrête le buzzer / led a l'aide d'un thread
        
        def isPressed(self):
            return self.buttonPin.is_pressed
            
        def wait_for_press(self):
            self.buttonPin.wait_for_press()
   
        def wait_for_press(self, timeout):
            self.buttonPin.wait_for_press(timeout)
