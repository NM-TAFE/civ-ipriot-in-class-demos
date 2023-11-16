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

7. Commit your changes to the repository, locally and add a tag so your lecturer can find it. A tag is a way to mark a specific commit as important. You can use tags to mark milestones in your project, often marking releases. You will use it to mark specific commits for your lecturer to review.

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

**Evidencing:**
Ensure that you have completed the previous steps and created the appropriate tags. Confirm that the tags have been created by running `git tag` in the terminal and provide a screenshot of the output.

```text
[student@workstation ipriot-carpark-prj]$ git tag
s1
s2
```
## TO BE CONTINUED

Additional content to be added shortly
