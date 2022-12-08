from Organ import Organ

class Stomach(Organ):

    def __init__(self, medicalCondition: str, isEmpty: bool):
        super().__init__("Stomach", medicalCondition)
        self.isEmpty = isEmpty
    
    def getDetails(self):
        super().getDetails()
        print("Need to be fed") if self.isEmpty else print("Stomach is full")

    def digest(self):
        if self.isEmpty:
            print("Digesting begin...")
            self.isEmpty = False
        else:
            print("Stomach is already full")