from Eye import Eye
from Heart import Heart
from Stomach import Stomach
from Skin import Skin

class Patient():

    def __init__(self, name: str, age: int, leftEye: Eye, rightEye: Eye, heart: Heart, stomach: Stomach, skin: Skin):
        self.name = name
        self.age = age
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.heart = heart
        self.stomach = stomach
        self.skin = skin