# %% List
# Lists in Python: A list is a collection which is ordered and changeable. 
# Let's create a simple list of car brands
car_brands = ['Toyota', 'Honda', 'Tesla', 'Ford']

# Print the car brands in the list
for i, brand in enumerate(car_brands):
    print(f"Car brand {i+1} is {brand}")

# %% Dictionary
# Dictionaries in Python: A dictionary is a collection which is unordered, changeable and indexed.
# Let's create a simple dictionary of cars with their colors
cars_and_colors = {'Toyota Camry': 'Black', 'Honda Accord': 'White', 'Tesla Model 3': 'Red', 'Ford Mustang': 'Blue'}

# Print the car names and their colors
for car, color in cars_and_colors.items():
    print(f"The {car} is {color} in color")

# %% Classes
# Now let's talk about Classes and Objects in Python

# Define a class named "Car"
class Car:
    # The __init__ method is a special method that is called when an object is created.
    # It serves as the constructor of the class.
    # Here we are defining the properties of a car as class variables.
    def __init__(self, brand, model, year, color):
        self.brand = brand  # brand of the car
        self.model = model  # model of the car
        self.year = year  # year of the car
        self.color = color  # color of the car

    # A function to display the details of the car
    def display(self):
        return f"{self.brand} {self.model} ({self.year}) in {self.color} color"

# %% Objects

# Let's create some car objects now
car1 = Car('Tesla', 'Model 3', 2020, 'Red')
car2 = Car('Ford', 'Mustang', 2018, 'Blue')

# Print the details of the cars
print(f"Car 1 is a {car1.display()}")
print(f"Car 2 is a {car2.display()}")

# %% Chassis
# Now let's define a new class called Chassis
class Chassis:
    # The __init__ method is a special method that is called when an object is created.
    # It serves as the constructor of the class.
    # Here we are defining the properties of a chassis as class variables.
    def __init__(self):
        # Front Left motor status
        # Front Right motor status
        # Back Left motor status
        # Back Right motor status

    # A function to display the status of the motors
    def display_status(self):
        ...

    # A function to drive the chassis forward
    def drive_forward(self):
        ...
        print("Driving forward")

    # A function to drive the chassis backward
    def drive_backward(self):
        ...
        print("Driving backward")

    # A function to turn the chassis right
    def turn_right(self):
        ...
        print("Turning right")

    # A function to turn the chassis left
    def turn_left(self):
        ...
        print("Turning left")

# %% Drive the chassis
# Let's create a chassis object now
chassis = Chassis()

# Print the initial status of the motors
chassis.display_status()

# Drive the chassis forward and display the motor status
chassis.drive_forward()
chassis.display_status()

# Drive the chassis backward and display the motor status
chassis.drive_backward()
chassis.display_status()

# Turn the chassis right and display the motor status
chassis.turn_right()
chassis.display_status()

# Turn the chassis left and display the motor status
chassis.turn_left()
chassis.display_status()


# %% Mecanum Chassis
# Now let's modify the Chassis class to support Mecanum wheels
class MecanumChassis:
    def __init__(self):
        self.FLmotor = 'off'  # Front Left motor status
        self.FRmotor = 'off'  # Front Right motor status
        self.BLmotor = 'off'  # Back Left motor status
        self.BRmotor = 'off'  # Back Right motor status

    def display_status(self):
        print(f"FLmotor: {self.FLmotor}, FRmotor: {self.FRmotor}, BLmotor: {self.BLmotor}, BRmotor: {self.BRmotor}")

    def drive_forward(self):
        ...
        print("Driving forward")

    def drive_backward(self):
        ...
        print("Driving backward")

    def turn_right(self):
        ...
        print("Turning right")

    def turn_left(self):
        ...
        print("Turning left")

    def strafe_right(self):
        ...
        print("Strafing right")

    def strafe_left(self):
        ...
        print("Strafing left")

# %% Drive the mecanum chassis
# Let's create a MecanumChassis object now
mecanum_chassis = MecanumChassis()

# Print the initial status of the motors
mecanum_chassis.display_status()

# Drive the MecanumChassis forward and display the motor status
mecanum_chassis.drive_forward()
mecanum_chassis.display_status()

# Drive the MecanumChassis backward and display the motor status
mecanum_chassis.drive_backward()
mecanum_chassis.display_status()

# Turn the MecanumChassis right and display the motor status
mecanum_chassis.turn_right()
mecanum_chassis.display_status()

# Turn the MecanumChassis left and display the motor status
mecanum_chassis.turn_left()
mecanum_chassis.display_status()

# Strafe the MecanumChassis right and display the motor status
mecanum_chassis.strafe_right()
mecanum_chassis.display_status()

# Strafe the MecanumChassis left and display the motor status
mecanum_chassis.strafe_left()
mecanum_chassis.display_status()
