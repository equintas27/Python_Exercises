class Planta:
    def __init__(self, name, height, age):
        self._name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        
    def set_height(self, height):
        if height < 0:
            print("Height cannot be negative")
        else:
            self._height = height

    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative")
        else:
            self._age = age

    def get_height(self):
        return self._height
    def get_age(self):
        return self._age

    def show(self):
        print(f"Created: {self._name}, {self._height} cm, {self._age} days old")


    def grow(self):
        self._height += 0.8
        self._height = round(self._height, 1)


