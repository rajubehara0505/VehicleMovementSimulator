# VehicleMovementSimulator

A Python-based application demonstrating the principles of Object-Oriented Programming (OOP), specifically focusing on inheritance, abstraction, and polymorphism. This repository contains a base `Vehicle` class with abstract methods, and several subclasses (`Car`, `Bicycle`, `Boat`) that implement the abstract `move` method in their own unique ways.

## Features:
- **Abstract Base Class**: Defines a `Vehicle` class with an abstract `move` method.
- **Subclasses**: `Car`, `Bicycle`, and `Boat` classes that inherit from `Vehicle` and implement the `move` method.
- **Polymorphism Demonstration**: A function `operate_vehicle` that takes a `Vehicle` object and calls its `move` method.

## Usage:
```python
from abc import ABC, abstractmethod

# Define an abstract base class called Vehicle
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        """
        Abstract method that sets up an interface for subclasses.
        Subclasses must implement their own unique implementation of the move method.
        """
        pass

# Create a subclass Car that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        """
        Implementation for Car's move method.
        """
        print("Car is driving on the road.")

# Create a subclass Bicycle that inherits from Vehicle
class Bicycle(Vehicle):
    def move(self):
        """
        Implementation for Bicycle's move method.
        """
        print("Bicycle is pedaling along the bike path.")

# Create a subclass Boat that inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        """
        Implementation for Boat's move method.
        """
        print("Boat is sailing on the water.")

# Function to demonstrate polymorphism
def operate_vehicle(vehicle):
    """
    Calls the move method of the given vehicle object.
    """
    vehicle.move()

if __name__ == "__main__":
    # Create instances of each type of vehicle
    car = Car()
    bicycle = Bicycle()
    boat = Boat()

    # Demonstrate polymorphism by calling the move method for each vehicle
    operate_vehicle(car)
    operate_vehicle(bicycle)
    operate_vehicle(boat)

Getting Started:
Clone the repository:
sh
Copy code
git clone https://github.com/yourusername/VehicleMovementSimulator.git
Navigate to the project directory:
sh
Copy code
cd VehicleMovementSimulator
Run the example script:
sh
Copy code
python vehicle_simulator.py
Contributing:
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
