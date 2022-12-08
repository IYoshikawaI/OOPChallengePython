import os
import pickle
from Patient import Patient
from Eye import Eye
from Heart import Heart
from Stomach import Stomach
from Skin import Skin

if __name__ == '__main__':

    with open(f"{os.path.dirname(os.path.realpath(__file__))}\\patient.info", "rb") as file:
        patient: Patient = pickle.load(file)

    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")

    while True:
        organ = int(input(f"""Choose an Organ:
        \t1. {patient.leftEye.name}
        \t2. {patient.rightEye.name}
        \t3. {patient.heart.name}
        \t4. {patient.stomach.name}
        \t5. {patient.skin.name}
        \t6. Quit\n"""))
        if organ == 1:
            patient.leftEye.getDetails()
            if patient.leftEye.isOpened:
                answer = int(input("\t\t1. Close the Eye\n"))
                if answer == 1:
                    patient.leftEye.closeEye()
            else:
                answer = int(input("\t\t1. Open the Eye\n"))
                if answer == 1:
                    patient.leftEye.openEye()
        elif organ == 2:
            patient.rightEye.getDetails()
            if patient.rightEye.isOpened:
                answer = int(input("\t\t1. Close the Eye\n"))
                if answer == 1:
                    patient.rightEye.closeEye()
            else:
                answer = int(input("\t\t1. Open the Eye\n"))
                if answer == 1:
                    patient.rightEye.openEye()
        elif organ == 3:
            patient.heart.getDetails()
            answer = int(input("\t\t1. Change the heart rate\n"))
            if answer == 1:
                heartRate = int(input("Enter the new heart rate:\n"))
                patient.heart.heartRate = heartRate
                print(f"Heart rate changed to: {patient.heart.heartRate}")
        elif organ == 4:
            patient.stomach.getDetails()
            answer = int(input("\t\t1. Digest\n"))
            if answer == 1:
                patient.stomach.digest()
        elif organ == 5:
            patient.skin.getDetails()
        elif organ == 6:
            with open(f"{os.path.dirname(os.path.realpath(__file__))}\\patient.info", "wb") as file:
                patient.stomach.isEmpty = True
                pickle.dump(patient, file)
            break