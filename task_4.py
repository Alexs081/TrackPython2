if __name__ == "__main__":
    # Write your solution here
    pass
class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0

    def drive(self, distance: float) -> None:
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self._mileage += distance

    def get_mileage(self) -> float:
        return self._mileage

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year})"


class PassengerCar(Car):
    def __init__(self, brand: str, model: str, year: int, seats: int):
        super().__init__(brand, model, year)
        self.seats = seats

    def drive(self, distance: float) -> None:
        if distance > 1000:
            raise ValueError("Легковой автомобиль не может проехать более 1000 км за раз")
        super().drive(distance)

    def __str__(self) -> str:
        return f"Легковой автомобиль: {self.brand} {self.model} ({self.year}), места: {self.seats}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year}, seats={self.seats})"


class Truck(Car):
    def __init__(self, brand: str, model: str, year: int, capacity: float):
        super().__init__(brand, model, year)
        self.capacity = capacity

    def load_cargo(self, weight: float) -> str:
        if weight > self.capacity:
            return "Превышена грузоподъемность!"
        return f"Груз весом {weight} тонн загружен"

    def __str__(self) -> str:
        return f"Грузовой автомобиль: {self.brand} {self.model} ({self.year}), грузоподъемность: {self.capacity}т"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year}, capacity={self.capacity})"


if __name__ == "__main__":
    car1 = PassengerCar("Toyota", "Camry", 2020, seats=5)
    car2 = Truck("Volvo", "FH16", 2019, capacity=20)

    print(car1)
    print(repr(car1))
    car1.drive(200)
    print(f"Пробег {car1.get_mileage()} км")

    print(car2)
    print(repr(car2))
    print(car2.load_cargo(15))
    car2.drive(500)
    print(f"Пробег {car2.get_mileage()} км")
