class Car:

    def __init__(self, make, model, hp):
        print(f"argumenti: {make} {model} {hp}")
        self.make = make
        self.model = model
        self.hp = hp

    def print_something(self):
        print(f"JA SAM {self.make}")