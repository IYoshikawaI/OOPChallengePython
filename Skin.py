from Organ import Organ

class Skin(Organ):

    def __init__(self, medicalCondition: str, color: str, softness: int):
        super().__init__("Skin", medicalCondition)
        self.color = color
        self.softness = softness
    
    def getDetails(self):
        super().getDetails()
        print(f"Skin Color: {self.color}")