# Assessment Task: Object-Oriented Programming - Carpark System

## Overview

In this assessment, you are required to design and implement a simplified carpark system using Object-Oriented Programming (OOP) concepts in Python. The system will consist of a Carpark, Sensors, and Displays to track the cars entering and exiting and the availability of parking bays.

## Objectives

By completing this task, you will demonstrate the following competencies as outlined in ICTPRG430:

1. **Modularity**: Implementing the logic for one object operation using a modular approach.
2. **Data Structures**: Utilizing arrays of primitive data types within a class.
3. **File Operations**: Reading from and writing to a text file.
4. **Class Design**: Developing two classes with four instance variables each.
5. **Object Construction**: Creating a class that offers two options for object construction.
6. **Object Aggregation**: Employing user-defined object aggregation within a class.
7. **Polymorphism**: Implementing polymorphism to enhance code extensibility.
8. **Debugging**: Utilizing a debugging tool to troubleshoot your code.
9. **Code and Documentation Conventions**: Applying specified coding and documentation standards.
10. **Unit Testing**: Conducting and documenting two unit test cases.

## Task Requirements

1. **Carpark Class**:
   - Implement a `Carpark` class with instance variables for location, capacity, current vehicle count, and an array of `Sensor` objects.
   - Include methods to increment/decrement the vehicle count and to update the display.
   - The class should have two constructors: one default and one that allows setting the initial values of the instance variables.

2. **Sensor Class**:
   - Create a `Sensor` class with instance variables for ID, status, location, and type.
   - Implement methods to activate/deactivate the sensor and detect a car's presence.
   - The `Sensor` class should interact with the `Carpark` class to update the vehicle count and availability of bays.

3. **Display Class**:
   - Design a `Display` class with instance variables for ID, message, status, and an array of `Carpark` data.
   - This class should have a method to display the current number of available parking bays.

4. **Aggregation**:
   - Use aggregation in the `Display` class to hold information about the `Carpark` class, showing the relationship between them.

5. **Polymorphism**:
   - Implement polymorphism by creating a method that can be overridden in a subclass to provide different display messages.

6. **File Operations**:
   - Implement file reading and writing in the `Carpark` class to log the entry and exit times of cars.

7. **Debugging**:
   - Utilize a debugging tool of your choice (e.g., Pycharm's debugger) to debug your classes.

8. **Documentation Conventions**:
   - Ensure that your code is well-documented, including comments for classes and methods, and use consistent naming conventions for variables and functions.
   - Specify at least three documentation aspects according to the organizational standards provided in the task brief.

9. **Unit Testing**:
   - Write two unit tests to verify that the `Sensor` and `Display` classes are functioning as expected.

## Version control requirements

As part of this assessment, you will demonstrate competencies in using a version control system as outlined in ICTICT449. You will plan, install, create, and manage a repository to control versions of your code for the Carpark system.

- Create a new repository and configure it with a README, .gitignore, and other essential setup files.
- Initialize your local repository and link it to a remote repository on GitHub.
- Make initial commits with the basic structure of your Carpark system.
- As you develop the system, commit your changes each time you reach a significant milestone or complete a task.
- Make at least three commits to demonstrate the evolution of your project.
- Manage any changes or improvements by committing to the repository with clear, descriptive commit messages.

## Scaffolding

1. Begin by outlining the classes and their relationships.
2. Pseudocode can help map out the logic before actual coding.
3. Use comments to mark sections where file operations and arrays are used.
4. Develop a simple flowchart to illustrate object interactions within the system.
5. Example code snippets will be provided to guide the construction of methods for reading/writing files and for implementing constructors.

## Submission

Your final submission should include:

- Python script files for each class in a zip file.
- Your `.git/` should be included with your zip file.
- Your `.gitignore` file should exclude any files that are not required for marking
- Your `venv/` should **not** be included in your submission.
- A text file used for logging car entries/exits.
- This worksheet, completed with your documentation.

## Assessment Criteria

You will be assessed on:

- The correct implementation of OOP concepts.
- Code functionality and adherence to the provided specifications.
- Quality and clarity of code documentation.
- Successful execution and documentation of unit tests.

## Instructions

### Set up version control

1. Create a new repository on GitHub. Initialize it with a `README.md`, .`gitignore`, and optionally a license.
2. Clone the repository to your local machine.
3. Update the `README.md` file with a brief description of the project.
4. Modify the `.gitignore` file to exclude the `.idea/` folder. This folder is created by Pycharm and contains project-specific settings that should not be shared.
5. Create a virtual environment for your project. This will allow you to install packages without affecting other projects on your machine.

   ```bash
   python -m venv venv
   
   # On Windows cmd:
   venv\Scripts\activate.bat
   
   # On Git Bash:
   source venv/Scripts/activate
   
   # On any other OS:
   source venv/bin/activate
   ```

6. Open the project folder in Pycharm. Pycharm will detect the virtual environment and use it for the project.
7. Create a `src` and `tests` directories in your project. The `src` directory will contain your Python scripts, and the `tests` directory will contain your unit tests. Your project structure should look like this:

   ```bash
   ipriot-carpark-prj/
   ├── .git/
   ├── venv/
   ├── .gitignore
   ├── README.md
   ├── src/
   └── tests/
   ```

8. Create a new Python file in the `src` directory called `main.py`. This will be the main script for your Carpark system.
9. Create a new Python file in the `tests` directory called `test_carpark.py`. This will be the main script for your unit tests.
10. In PyCharm, mark the `src` directory as a source root. This will allow you to import modules from the `src` directory in your unit tests; mark the `tests` directory as a test root. This will allow you to run your unit tests from the IDE.
11. Commit your changes to the repository, both locally and remotely:

      ```bash
      git add .
      git commit -m "Initial commit"
      git push
      ```

**Evidencing:**
Include a screenshot of your GitHub repository **after** you have pushed your initial commit.

```text
![Initial commit](images/mu_image.png)
```

### Identify classes, methods, and attributes

After reading the task requirements, you should be able to identify the classes, methods, and attributes required for the Carpark system. Complete the following table with the classes, methods, and attributes you will need to implement.

| Class Name | Attributes | Methods |
| ---------- | ---------- | ------- |
| `Carpark`    |            |         |
| `Sensor`     |            |         |
| `Display`    |            |         |
| `Config`     |            |         |

**Evidencing:**
Ensure that you have completed the previous table and include at least two methods, and two attributes for each.

### Implement stubs for the classes

1. In your `src/` directory, create a new Python file for each class you identified in the previous step. For example, `carpark.py`, `sensor.py`, `display.py`, and `config.py`.
   Notice that the file names are all lowercase and use underscores to separate words. This is a common convention for Python file names.
2. In each file, create a class with the same name as the file. For example, the `carpark.py` file should contain a `Carpark` class. Notice that the class name is capitalized and uses CamelCase to separate words. This is a common convention for Python class names. An example class definition is shown below:

   ```python
   class Carpark:
       pass
   ```

3. Commit your changes to the repository, both locally and remotely:

      ```bash
      git add .
      git commit -m "Added stubs for classes"
      git push
      ```

**Evidencing:**
Include a screenshot of your GitHub repository `src/` directory **after** you have pushed your changes

```text
![Added stubs for classes](images/stubs-for-classes.png)
```

### Add constructors and attributes to the classes

#### Carpark class

1. Create an `__init__` method for the `Carpark` class. This method will be called when a new `Carpark` object is created. The method should accept the following parameters:
   - `location`
   - `capacity`
   - `current_vehicle_count`
   - `sensors`
   - `displays`
2. Add instance variables for each of the parameters. For example, `self.location = location`.
3. Add a default value for each parameter. For example, `location = "Unknown"`.
4. Notice that sensors and displays are arrays. This is because a carpark can have multiple sensors and displays. Add an empty array for each of these parameters. For example, `self.sensors = []`. However, we must never set mutable defaults for parameters. So make the defaults `None`.
5. Add a `__str__` method to the `Carpark` class. This method will be called when you print a `Carpark` object. The method should return a string containing the carpark's location and capacity. For example, `"Carpark at 123 Example Street, with 100 bays."`.
6. Your carpark class should now look similar to this:

   ```python
   class Carpark:
      def __init__(self, location="Unknown", capacity=0, current_vehicle_count=0, sensors=None, displays=None):
         self.location = location
         self.sensors = sensors or [] # uses the first value if not None, otherwise uses the second value
         ... # Add the other parameters here
      
      def __str__(self):
         ... # Return a string containing the carpark's location and capacity
   ```

7. Commit your changes to the repository locally and add a tag so your lecturer can find it. A tag is a way to mark a specific commit as important. You can use tags to mark milestones in your project, often marking releases. You will use it to mark specific commits for your lecturer to review.

   ```bash
   git add .
   git commit -m "Added constructors and attributes to the carpark class"
   git tag -a "s1" -m "Added a constructor and attributes to the carpark class"
   ```

#### Display class

1. Create an `__init__` method for the `Display` class. This method will be called when a new `Display` object is created. The method should accept the following parameters:
   - `id`
   - `message`
   - `is_on`
   - `carpark`
2. Add instance variables for each of the parameters. For example, `self.id = id`.
3. Add default values for parameters, such that there is no default for id or carpark, but there is a default for message and status. For example, `message = ""` and `is_on = False`.
4. Create a `__str__` method for the `Display` class. This method will be called when you print a `Display` object. The method should return a string containing the display's id and message. For example, `"Display 1: Welcome to the carpark."`.

#### Sensor class

1. Create an `__init__` method for the `Sensor` class. This method will be called when a new `Sensor` object is created. The method should accept the following parameters:
   - `id`
   - `is_active`
   - `carpark`

   You realize that you need to distinguish between entry and exit sensors. Since each of those sensors will need different methods, you decide to subclass the `Sensor` class.

2. Create a new class called `EntrySensor` that inherits from `Sensor`. The `EntrySensor` class should **not** have an `__init__` method.
Do the same for the `ExitSensor` class.

   Your `sensor.py` file should now look similar to this:

   ```python
   class Sensor:
      def __init__(self, id ...): # Add the other parameters
         self.id = id
         self.is_active = is_active
         ... # Add the other attributes

      def __str__(self):
         ... # Return a string containing the sensor's id and status

   class EntrySensor(Sensor):
      ...

   # Also create an ExitSensor class
   ```

3. Commit your changes to the local repository and add a tag so your lecturer can find it:

   ```bash
   git add .
   git commit -m "Added constructors and attributes to the display and sensor classes"
   git tag -a "s2" -m "Added constructors and attributes to the display and sensor classes"
   ```

4. Now push your **tagged** changes to the remote repository:

   ```bash
   git push --tags
   ```

#### Config class

You realize that you need a way to configure the carpark system. You decide to create a `Config` class to store the configuration data. However, you want to have a firmer grasp of the requirements before you implement the class. So you skip this step for now.

--------
**Evidencing:**
Ensure that you have completed the previous steps and created the appropriate tags. Confirm that the tags have been created by running `git tag` in the terminal and provide a screenshot of the output.

```text
[student@workstation ipriot-carpark-prj]$ git tag
s1
s2
```

Additional content to be added shortly
=======
----

### Relate the classes

Let's consider how the classes relate to each other. We can start by using a sequence diagram to illustrate the interactions between the classes. A sequence diagram shows the interactions between objects in a sequential order. The following diagram shows the interactions between the `Carpark`, `Sensor`, and `Display` classes.

```mermaid
sequenceDiagram
    actor v as Vehicle
    participant s as Sensor
    participant c as Carpark
    participant d as Display
    v->>s: enters (detect_car())
    s->>s: scan_plate()
    s->>c: update_carpark(+1)
    c->>d: update_displays()
    v->>s: exits (detect_car())
    s->>s: scan_plate()
    s->>c: update_carpark(-1)
    c->>d: update_display()
```

Notice a sensor detects cars and notifies a carpark. The carpark then updates the displays. Sensors connect **to** a carpark and a carpark connects **to** displays.

In other words, a sensor needs to know about a carpark, and a carpark needs to know about displays. This is an example of aggregation, where one object holds a reference to another object. In this case, the `Carpark` class holds a reference to instances of the `Display` classes (aggregation); sensors for their part hold a reference to a carpark.

The following class diagram presents this relationship:

```mermaid
classDiagram
      Carpark "1" o-- "0..*" Display
      Carpark "1" *-- "0..*" Sensor
      Sensor <|-- EntrySensor
      Sensor <|-- ExitSensor 
      

      class Carpark {
         - sensors: Sensor[]
         - displays: Display[]
         - plates: String[]
         + register(obj: Sensor | Display) void
         + add_car(plate: str) void
         + remove_car(plate: str) void 
         + update_displays() void
      }
      class Sensor {
         <<abstract>>
         - carpark: Carpark
         - update_carpark(plate: str) void
         + detect_car() void
      }
      class EntrySensor{
         - update_carpark(plate: str) void

      }
      class ExitSensor{
         - update_carpark(plate: str) void
      }
      class Display {
         - carpark: Carpark
         + update() void
      }
```

The diagram omits methods and attributes that are not relevant to the relationship between the object. Notice that the `Carpark` class has a `register` method that allows it to register sensors and displays.

Notice also that displays and sensors reference a carpark and a carpark references displays. This kind of two way relationship is not always advisable. But for this project, it is acceptable.

### Implement methods for the Carpark class

Our analysis shows that the carpark will need to implement the following methods:

- `register`: This method will allow the carpark to register sensors and displays.
- `add_car`: This method will be called when a car enters the carpark. It will record the plate number and update the displays.
- `remove_car`: This method will be called when a car exits the carpark. It will remove the plate number and update the displays.
- `update_displays`: This method will be called when the carpark needs to update the displays. It will iterate through the displays and call their `update` method.

As we implement these methods, we may find we need additional methods and attributes. For example, we may need a method to check if a plate number is already in the carpark. We may also need an attribute to store the plate numbers. We can add these as we go.

We will focus on these key principles to guide the need for additional methods and attributes:

- **Encapsulation**: We want to hide the implementation details of the class from other classes. We can do this by making attributes private and only exposing them through methods.
- **Single Responsibility**: We want each method to have a single responsibility. This will make the code easier to understand and maintain.
- **DRY**: We want to avoid repeating code or information about state (Don't Repeat Yourself). We can do this by creating methods and attributes for behaviors and values that are repeated.

---

#### Register method

1. Create a `register` method for the `Carpark` class. This method should accept a single parameter, `obj`. This parameter will be either a `Sensor` or `Display` object.
2. If the `obj` is a `Sensor`, add it to the `sensors` array. If the `obj` is a `Display`, add it to the `displays` array.
3. If the `obj` is neither a `Sensor` nor a `Display`, raise a `TypeError` with the message `"Object must be a Sensor or Display"`.

**Stuck?**
Here are some some hints to help you complete this task:

Even though we often think of exceptions last, we generally want to put them first in our method definitions. This is because exceptions are exceptional. We want to handle them first and then handle the normal flow of the method. This is called a **guard pattern** and is a common pattern in Python and other languages.
Let's do that now. Add the following code to the top of the `register` method:

   ```python
   # ... inside the Carpark class
   def register(self, component):
      if not isinstance(component, (Sensor, Display)):
         raise TypeError("Object must be a Sensor or Display")
   ```

The `isinstance` function checks if an object is an instance of a class. In this case, we are checking if the `component` is an instance of either the `Sensor` or `Display` class. Notice, that we'll need to import the `Sensor` and `Display` classes to use them in the `isinstance` function. Add the following import statement to the top of the `carpark.py` file:

   ```python
   from sensor import Sensor
   from display import Display
   ```

Now we can add the code to add the `component` to the appropriate array. Add the following code to the `register` method:

   ```python
   # ... inside the register method
   if isinstance(component, Sensor):
      self.sensors.append(component)
   # add an elif to check if the component is a Display
   ```

**Evidencing:**
After you have implemented the required code, commit your changes to the local repository and add a tag so your lecturer can find it:

   ```bash
   git add .
   git commit -m "Added a register method to the carpark class"
   git tag -a "s3" -m "Added a register method to the carpark class"
   ```

#### Add and remove car methods

When a car enters the carpark, we record its plate number and update the displays. When a car exits the carpark, we remove its plate number and update the displays. We can implement these behaviors in the `add_car` and `remove_car` methods.

1. In the Carpark class, create an `add_car` method. This method should accept a single parameter, `plate`. This parameter will be a string containing the car's plate number.
2. Append the `plate` to the `plates` list (`self.plates.append(plate)`).
3. Call the `update_displays` method.
   Hang on, we haven't implemented the `update_displays` method yet. We'll do that next.
   Here is a sample implementation of the `add_car` method:

      ```python
      # ... inside the Carpark class
      def add_car(self, plate):
         self.plates.append(plate)
         self.update_displays()
      ```

4. Repeat the previous steps to implement the `remove_car` method. This method also accepts a single parameter, `plate` and also calls `update_displays`. However, this method should remove the plate from `self.plates`.

#### Update displays method

Finally, we are going to create the `update_displays` method. This method will iterate through the `displays` list and call the `update` method on each display. Before we proceed, consider, as a driver, what information you would like to see when you enter a carpark.

You may want to see the number of available bays, the current temperature, and the time.

Now consider, between the `Carpark`, `Sensor`, and `Display` classes, which class is responsible for each of these pieces of information? There's no right or wrong answer here. But you should be able to justify your answer.

Q. Which class is responsible for the number of available bays (and why)?
Q. Which class is responsible for the current temperature (and why)?
Q. Which class is responsible for the time (and why)?

--------

##### Detour: implement available bays

You realize that you are not currently maintaining the number of available bays. The number of available bays is a curious case. This value, on the one hand, clearly seems like an attribute of the carpark. However, it is also a **property** of the carpark's capacity and the number of cars in the carpark. In other words, it is a **derived** value. We can calculate the number of available bays by subtracting the number of cars from the capacity. We can do this in the `Carpark` class by adding a `get_available_bays` method. This method will return the number of available bays.

But you're not comfortable with this, because even though you are deriving the value through a calculation it still seems like an attribute. Python has a built-in way to treat a method as though it is a simple attribute. We can use it to protect values as well as make attributes derived via simple calculations easier to access. Fittingly, it is called a **property**. We can create a property by adding a `@property` decorator (we'll learn more about decorators in the diploma) to a method. While we don't yet fully understand decorators, the important thing is that they make a method act like an attribute.

Let's add `available_bays` as a property now:

```python
      # ... inside the Carpark class
      @property
      def available_bays(self):
         return self.capacity - len(self.plates)
```

Notice that we did **not** use a verb in a property name. This is because properties are accessed like attributes. For example, `carpark.available_bays` instead of `carpark.get_available_bays()`.

An added bonus is that if someone accidentally tries to set the value to this property, they will get an error. This is because we have not defined a property setter, and this is a good thing in this case.

You recognize an issue: what if the number of cars that entered exceeds capacity?

We might not be able to stop this from happening!

But what should happen if it does? Do we want to allow the number of available bays to be negative? Or should we set it to zero? Or should we raise an exception? Something else??

You discuss with the senior developer and decide that if the number of plates exceeds the capacity you will return 0.

> Modify the `available_bays` property to return 0 if the number of plates exceeds the capacity.

--------

**TO BE CONTINUED...**


