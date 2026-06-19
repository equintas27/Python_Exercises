from classes import Planta

def ft_garden_security():
    print("=== Garden Security ===")
    planta = Planta("Garden", 15, 10)
    planta.show()

    planta.grow()
if __name__ == "__main__":
    ft_garden_security()
