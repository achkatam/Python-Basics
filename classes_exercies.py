class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, my name is  {self.name}.")


johny = Person("Johny")
johny.talk()

bobby = Person("Bobby Leshly")
bobby.talk()