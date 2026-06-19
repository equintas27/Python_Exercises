class Planta:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Nome: {self.name}, Height: {self.height} cm, Age: {self.age} days old")


