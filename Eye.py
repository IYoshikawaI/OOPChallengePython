from Organ import Organ

class Eye(Organ):
    
    def __init__(self, name: str, medicalCondition: str, color: str, isOpened: bool):
        super().__init__(name, medicalCondition)
        self.color = color
        self.isOpened = isOpened
    
    def getDetails(self):
        super().getDetails()
        print(f"Color: {self.color}")
    
    def openEye(self):
        print(f"{self.name} Opened")
        self.isOpened = True
    
    def closeEye(self):
        print(f"{self.name} Closed")
        self.isOpened = False