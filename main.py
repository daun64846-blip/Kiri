class Car:

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print("--- Car Information ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

car1 = Car("Toyota", "Camry", 2022, "Silver")
car2 = Car("Ford", "Mustang", 1969, "Red")
car3 = Car("Tesla", "Model 3", 2024, "Black")

car1.display_info()
car2.display_info()
car3.display_info()