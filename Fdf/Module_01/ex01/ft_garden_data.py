from classes import Planta

def ft_garden_data():
    print("=== Garden Plant Registry ===")
    planta1 = Planta ("Rose", 25, 30)
    planta2 = Planta ("Sunflower", 80, 45)
    planta3 = Planta ("Cactus", 15, 120)

    planta1.show()
    planta2.show()
    planta3.show()

if __name__ == "__main__":
    ft_garden_data()
