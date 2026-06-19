class Planta:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.name}, {self.height} cm, {self.age} days old")
    def grow(self):
        self.height += 0.8
        self.height = round(self.height, 1)
    def age_old(self):
        self.age += 1
