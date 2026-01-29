class Car:
    def __init__(self, brand, model, vin):
        self.brand = brand
        self.model = model
        self.vin = vin

    def __str__(self):
        return f"{self.brand} is the car brand"

    def honk(self):
        print(f"{self.model} is honking")

    def sale(self, buyer):
        print(f"{self.vin} is bough by {buyer}")


c1 = Car("Toyota", "Camry", 1234)
print(c1.model)
print(c1.vin)
c1.honk()
c1.sale("Casper")

print(c1)
