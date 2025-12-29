

"""
# Abstract Factory Pattern
# Intent: Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
# Example: GUI toolkit that supports multiple look-and-feel standards (e.g., Windows, MacOS, Linux).
Provides a way to access functionality without caring about the implementation details of the functionality.
one level of abstraction above the factory pattern.
separation of concerns.
Allows foe testability.
# Use Cases:
# Cross-Platform Applications
"""
## problem : -  a restautant sells a combos that must come as consistent set:
## MainCourse + Drink

## if a customer orders a Vegan combo, they should get a Vegan MainCourse and a Vegan Drink.
## if a customer orders a NonVegan combo, they should get a NonVegan Main


from abc import ABC, abstractmethod
from typing import Type, Dict
from dataclasses import dataclass


# Abstract Products
class MainCourse(ABC):
    @abstractmethod
    def name(self) -> str:
        pass
class Drink(ABC):
    @abstractmethod
    def name(self) -> str:
        pass    

# Concrete Products
# Veg family
class PaneerBurger(MainCourse):
    def name(self):
        return "Paneer Burger"
class Lemonade(Drink):
    def name(self):
        return "Lemonade"
    
# Non-Veg family

class ChickenBurger(MainCourse):
    def name(self):
        return "Chicken Burger"
class Cola(Drink):
    def name(self):
        return "Cola"

# Abstract Factory
class MealFactory(ABC):
    @abstractmethod
    def create_main(self) -> MainCourse:
        pass
    @abstractmethod
    def create_drink(self) -> Drink:
        pass
# Concrete Factories
class VeganMealFactory(MealFactory):
    def create_main(self) -> MainCourse:
        return PaneerBurger()
    def create_drink(self) -> Drink:
        return Lemonade() 
class NonVeganMealFactory(MealFactory):
    def create_main(self) -> MainCourse:
        return ChickenBurger()
    def create_drink(self) -> Drink:
        return Cola()

# Client Code
def order_meal(factory: MealFactory):
    main = factory.create_main()
    drink = factory.create_drink()
    print(f'main : {main.name()}')
    print(f'drink : {drink.name()}')
    
if __name__ == '__main__':
    
    order_meal(VeganMealFactory())
    print("-----")
    order_meal(NonVeganMealFactory())


"""
with this pattern, the client code (order_meal function) is decoupled from the concrete classes of the products it uses. It only interacts with the abstract interfaces and factories, allowing for easy extension and modification of product families without changing the client code.
without this pattern, the client code would need to know about the specific classes of MainCourse and Drink it wants to create, leading to tight coupling and difficulty in extending or modifying product families.
"""
"""
without the Abstract Factory Pattern.
from abc import ABC, abstractmethod

# Product interfaces
class Button(ABC):
    @abstractmethod
    def paint(self) -> None: ...

class Checkbox(ABC):
    @abstractmethod
    def toggle(self) -> None: ...


# Windows products
class WinButton(Button):
    def paint(self) -> None:
        print("Win Button")

class WinCheckbox(Checkbox):
    def toggle(self) -> None:
        print("Win Checkbox")


# Mac products
class MacButton(Button):
    def paint(self) -> None:
        print("Mac Button")

class MacCheckbox(Checkbox):
    def toggle(self) -> None:
        print("Mac Checkbox")


# Client (problem: knows concrete classes and has if/else)
class AppWithoutAF:
    def __init__(self, os_name: str) -> None:
        if os_name.lower() == "windows":
            self.button = WinButton()
            self.checkbox = WinCheckbox()
        elif os_name.lower() == "mac":
            self.button = MacButton()
            self.checkbox = MacCheckbox()
        else:
            raise ValueError(f"Unsupported OS: {os_name}")

    def run(self) -> None:
        self.button.paint()
        self.checkbox.toggle()


if __name__ == "__main__":
    AppWithoutAF("windows").run()
    AppWithoutAF("mac").run()


"""