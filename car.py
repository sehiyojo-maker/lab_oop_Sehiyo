
class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, km):
        if not isinstance(km, (int, float)) or isinstance(km, bool):
            print("Invalid distance.")
        elif km <= 0:
            print("Distance must be positive.")
        else:
            self.mileage += km
            print(f"The car traveled {km} km.")

    def age(self, year):
        if year < self.year:
            return "Invalid year."
        return year - self.year

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}) "
                f"| Wheels: {self.wheels} "
                f"| Mileage: {self.mileage} km")


# Creating three objects
car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Mitsubishi", "Mirage", 2021)


# Testing drive method
car1.drive(100)
car2.drive(50)
car3.drive(200)

# Testing validation
car1.drive(-10)

# Displaying car information
print("\nCAR INFORMATION")
print(car1)
print(car2)
print(car3)

# Testing age method
print("\nCAR AGE")
print("Toyota Vios:", car1.age(2026), "years old")
print("Honda Civic:", car2.age(2026), "years old")
print("Mitsubishi Mirage:", car3.age(2026), "years old")
