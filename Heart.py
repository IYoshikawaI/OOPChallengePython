from Organ import Organ

class Heart(Organ):

    def __init__(self, medicalCondition: str, heartRate: int):
        super().__init__("Heart", medicalCondition)
        self.heartRate = heartRate
    
    def getDetails(self):
        super().getDetails()
        print(f"Heart rate: {self.heartRate}")