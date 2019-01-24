# JoshBothell
# 1/19


class Human(object):
    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
        self.race = race

    def introduce_self(self):
        print("Hello my name is ", self.name)

    def describe_self(self):
        print("I have", self.hair_color, "hair")
        print("I have", self.eye_color, "eye")
        print("I am", self.height, "cm tall")
        print("I am", self.weight, "kg")
        print("I have an IQ of", self.iq,)
        print("I am", self.gender)
        print("I am", self.race)

    def insult_self(self):
        thicc = None
        short_king = None
        idiot = None
        if int(self.weight) > 200:
            thicc = True
        if int(self.height) < 72:
            short_king = True
        if int(self.iq) < 90:
            idiot = True
        if thicc:
            print(self.name, "is disgustingly gargantuan at a sickening", self.weight, "kg")
        if short_king:
            print(self.name, "is practically a child at a pathetic", self.height, "centimeters")
        if idiot:
            print(self.name, "has a pathetically low iq which is below average at", self.iq)

    def bmi_calc(self):
        heightSqrd = int(self.height) * int(self.height)
        bmiraw = (int(self.weight) / heightSqrd) * 10000
        bmi = round(bmiraw, 1)
        print(self.name,"'s BMI is ", bmi)
        if bmi < 18.5:
            print(self.name, "is underweight")
        elif bmi < 24.9:
            print(self.name, "is normal weight")
        elif bmi < 29.9:
            print(self.name, "is overweight")
        elif bmi > 30:
            print(self.name, "is obese")


josh = Human("Josh", "Blonde", "Blue", "180", "55", "0","Male", "White")
josh.bmi_calc()