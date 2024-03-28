# Modify attributes in class
class Car():
    """ A simple attempt to create a car"""
    def _init_(self,make,model,year): #_init_: means this will run automatically

        """ Initialize car attributes """
        self.make = make
        self.model = model
        self.year = year

        #fuel capacity and level in gallons
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """ Fill gas tank to capacity """
        self.fuel_level = self.fuel_capacity
        print('Fuel tank is full')

    def drive(self):
        """ Stimulate driving """
        print('The car is moving')

#Create object of Car class
my_car=Car('Benz','G3',2022)

#Accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)

#calling methods
my_car.drive()
my_car.fill_tank()
my_car.fuel_level()

#write a method to update an attributes values
def update_fuel_level(self,new_level):
    """ Update fuel level """
    if new_level <= self.fuel_capacity:
        self.fuel_level = new_level
    else:
        print('The tank cant hold that much')

#adding above function to original class as methos from outside
Car.update_fuel_level = update_fuel_level
my_car.update_fuel_level(12)
my_car.fuel_level

def add_fuel(self, amount):
    """ Add fuel to tank """
    if (self.fuel_level + amount <= self.fuel_capacity):
        self.fuel_level += amount
        print('Added fuel')
    else:
        print('The tank cannot hold that much')

Car.add_fuel = add_fuel
my_car.add_fuel(10)
my_car.add_fuel(2)
my_car.fuel_level