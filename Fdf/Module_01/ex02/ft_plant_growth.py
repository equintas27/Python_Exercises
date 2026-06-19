from classes import Planta 

def ft_plant_growth():
    print("=== Garden Plant Growth ===")
    planta = Planta("Rose", 25, 30)
    init_growth = planta.height
    planta.show()
    for i in range(1, 8):
        print(f" === Day {i} ===")
        planta.grow()
        planta.age_old()
        planta.show()
    grow_total = round(planta.height - init_growth, 1)
    print (f"Growth this week: {grow_total} cm")

if __name__ == "__main__":
    ft_plant_growth()
