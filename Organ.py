class Organ:

    def __init__(self, name: str, medicalCondition: str):
        self.name = name
        self.medicalCondition = medicalCondition
    
    def getDetails(self):
        print(f"Name: {self.name}")
        print(f"Medical Condition: {self.medicalCondition}")