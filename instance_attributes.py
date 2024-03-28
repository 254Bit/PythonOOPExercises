#Creating classes with instance variables
# Write a python program to create a vehicle class with max_speed and mileage instance

class Vehicle:
    def _int_(self, max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

maruti = Vehicle (120, 15)
print(maruti.max_speed, maruti.mileage)

