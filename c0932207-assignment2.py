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
