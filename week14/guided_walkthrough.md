# Student Handout Smart Carpark System Development

## Overview

In this practical session, we are going to build a Smart Carpark System for the City of Moondalup. Below are detailed instructions and code snippets to guide you through the creation of each class required for the system. Follow these instructions closely, and don't forget to run tests to ensure your code is working as expected!

---

## 1. Car Class

### Objective

Create a `Car` class to represent a car in the carpark.

### Attributes

- `license_plate`: String to store the car’s license plate.
- `car_model`: String to store the car model.
- `entry_time`: Datetime object to store the time the car entered the carpark.
- `exit_time`: Datetime object to store the time the car exited the carpark.

### Methods

- `__init__`: Constructor to initialize the car object.
- `__str__`: String representation method to easily print car details.

### Code Snippet

```python
from datetime import datetime

class Car:
    def __init__(self, license_plate, car_model, entry_time=None):
        self.license_plate = license_plate
        self.car_model = car_model
        self.entry_time = entry_time if entry_time else datetime.now()
        self.exit_time = None

    def __str__(self):
        return f"Car {self.license_plate} ({self.car_model})"
```

---

## 2. Carpark Class

### Objective

Create a `Carpark` class to manage cars and parking bays.

### Attributes

- `capacity`: Integer to store the total number of parking bays.
- `cars`: List to store the cars currently in the carpark.
- `available_bays`: Integer to track the number of available parking bays.

### Methods

- `__init__`: Constructor to initialize the carpark. If `pre_filled` is provided, add those cars to the carpark.
- `add_car`: Method to add a car to the carpark.
- `remove_car`: Method to remove a car from the carpark based on its license plate.

### Code Snippet

```python
class Carpark:
    def __init__(self, capacity, pre_filled=None):
        self.capacity = capacity
        self.cars = pre_filled if pre_filled else []
        self.available_bays = self.capacity - len(self.cars)

    def add_car(self, car):
        if self.available_bays > 0:
            self.cars.append(car)
            self.available_bays -= 1
            print(f"{car} has entered the carpark. Available bays: {self.available_bays}")
        else:
            print("Carpark is full. Cannot add more cars.")

    def remove_car(self, license_plate):
        for car in self.cars:
            if car.license_plate == license_plate:
                self.cars.remove(car)
                self.available_bays += 1
                print(f"{car} has exited the carpark. Available bays: {self.available_bays}")
                return
        print("Car not found in carpark.")
```

---

## 3. Display Class

### Objective

Create a `Display` class to show the number of available bays and current temperature.

### Attributes

- `carpark`: The `Carpark` object to access the number of available bays.
- `temperature_file`: String representing the path to the temperature data file.

### Methods

- `__init__`: Constructor to initialize the display.
- `read_temperature`: Method to read the current temperature from a file.
- `show_status`: Method to display the carpark status and current temperature.

### Code Snippet

```python
class Display:
    def __init__(self, carpark, temperature_file):
        self.carpark = carpark
        self.temperature_file = temperature_file

    def read_temperature(self):
        with open(self.temperature_file, 'r') as file:
            return file.read().strip()

    def show_status(self):
        temperature = self.read_temperature()
        print(f"Available Bays: {self.carpark.available_bays}")
        print(f"Current Temperature: {temperature}°C")
```

---

## 4. Sensor Classes

### Objective

Create `Sensor` classes to manage the entry and exit of cars.

### EntrySensor Class

- Inherits from a base `Sensor` class.
- Has a method `car_enters` to simulate a car entering the carpark.

### ExitSensor Class

- Inherits from a base `Sensor` class.
- Has a method `car_exits` to simulate a car exiting the carpark.

### Code Snippet

```python
class Sensor:
    def __init__(self, carpark):
        self.carpark = carpark

class EntrySensor(Sensor):
    def car_enters(self, car):
        self.carpark.add_car(car)

class ExitSensor(Sensor):
    def car_exits(self, license_plate):
        self.carpark.remove_car(license_plate)
```

---

## Testing Your Code

Make sure to write and run unit tests for each of your classes to ensure everything is working as expected.

## Conclusion

Congratulations! You've now implemented a Smart Carpark System. Remember to follow best coding practices and ensure your code is well-documented. Happy coding!