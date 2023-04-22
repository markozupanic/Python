class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    def who_am_i(self):
        print(f"JA SAM OSOBA {self.first_name} {self.last_name} i imam {self.age} ")
        
        
    def pesonification(self):
        print("personificcarion")
        
        
makro=Person("marko","županic",23)
Person.who_am_i(makro)
Person.pesonification(self=6)