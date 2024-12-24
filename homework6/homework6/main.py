from abc import ABC, abstractmethod

# Абстракция
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass


# Инкапсуляция
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__fuel_type = fuel_type
        self.__is_engine_on = False

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model

    def start_engine(self):
        if not self.__is_engine_on:
            self.__is_engine_on = True
            print(f"{self.__brand} {self.__model}: Двигатель запущен.")
        else:
            print(f"{self.__brand} {self.__model}: Двигатель уже работает.")

    def stop_engine(self):
        if self.__is_engine_on:
            self.__is_engine_on = False
            print(f"{self.__brand} {self.__model}: Двигатель остановлен.")
        else:
            print(f"{self.__brand} {self.__model}: Двигатель уже выключен.")

    def drive(self):
        if self.__is_engine_on:
            print(f"{self.__brand} {self.__model} едет!")
        else:
            print(f"{self.__brand} {self.__model}: Запустите двигатель перед началом движения.")

    def get_info(self):
        return f"Марка: {self.__brand}, Модель: {self.__model}, Год: {self.__year}, Тип топлива: {self.__fuel_type}"


# Наследование
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year, "electric")
        self.__battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"{self.get_brand()} {self.get_model()}: Зарядка батареи. Ёмкость: {self.__battery_capacity} кВт⋅ч.")

    # Полиморфизм
    def drive(self):
        print(f"{self.get_brand()} {self.get_model()} (электромобиль) едет бесшумно!")


# Использование
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, "gasoline")
    print(car.get_info())
    car.start_engine()
    car.drive()
    car.stop_engine()

    print("\n")

    tesla = ElectricCar("Tesla", "Model S", 2022, 100)
    print(tesla.get_info())
    tesla.start_engine()
    tesla.drive()
    tesla.charge_battery()
    tesla.stop_engine()