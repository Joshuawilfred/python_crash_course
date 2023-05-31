# 0x06. Python - Classes and Objects

This project focuses on Object-Oriented Programming (OOP) in Python. It covers various concepts related to classes, objects, and attributes. The project consists of several tasks, each building upon the previous one to reinforce the understanding of OOP principles.

## Learning Objectives

Upon completing this project, you should be able to:

- Explain why Python programming is awesome
- Understand the fundamentals of Object-Oriented Programming
- Define and use classes and objects
- Differentiate between class attributes and instance attributes
- Understand and implement encapsulation and information hiding
- Define properties and use them as an alternative to getters and setters
- Dynamically create attributes for class instances
- Explore the `__dict__` attribute of classes and instances
- Utilize the `getattr` function to access attributes
- Implement proper documentation using docstrings

## Tasks

The project consists of the following tasks:

1. **My first square**: Define an empty class `Square` that represents a square.

2. **Square with size**: Define a class `Square` that has a private instance attribute `size`. Implement instantiation with a size parameter and prevent direct access to the attribute.

3. **Size validation**: Extend the `Square` class to include validation for the `size` attribute. Raise appropriate exceptions if the size is not an integer or is less than 0.

4. **Area of a square**: Add a public instance method `area` to the `Square` class that calculates and returns the area of the square.

5. **Access and update private attribute**: Implement getter and setter methods for the `size` attribute in the `Square` class. Add validation to ensure that the size is an integer and not less than 0.

6. **Printing a square**: Extend the `Square` class to include a public instance method `my_print` that prints a square of `#` characters based on the size attribute.

7. **Coordinates of a square**: Add two private instance attributes, `x` and `y`, to the `Square` class to represent the square's position. Implement getters and setters for these attributes.

## Requirements

- Python 3.8.5
- Code should follow PEP 8 style guidelines
- All files should be executable
- Documentation using docstrings is required

**Note:** The above tasks are summarized for brevity. Please refer to the individual task files for detailed requirements and examples.

## Author

This project is created and maintained by Guillaume for the ALX Higher-Level Programming curriculum.
