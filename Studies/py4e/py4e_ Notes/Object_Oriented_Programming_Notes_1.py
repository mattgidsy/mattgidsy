print("================ Test 1 ===================")
#create class
class Bike:
    #name and gear are attributes of bike
    name = ""
    gear = 0

#create objects of class
bike1 = Bike()
 #access value of the attribute, gear, in the bike object of the Bike class
print(bike1.gear)

#modify or assign new values 
bike1.gear = 420
bike1.name = "Montain Bike"

print(bike1.gear)
print(f"Name: {bike1.name}  Gears: {bike1.gear}")

#multiple objects:
print(f"================== Multiple Objects ====================")
class Employee:
    #define an attribute
    employee_id = 0

#create 2 objects of the Employee class
employee1 = Employee()
employee2 = Employee()

#assign and access attributes of empoyee1
employee1.employee_id = 42069
print(f"Employee ID: {employee1.employee_id}")

#assign and access attributes of employee2
employee2.employee_id = 1337
print(f"Employee ID: {employee2.employee_id}")

print(f"====================== Python Methods ========================")

# we can define a function inside a python class. This is called a method.

#create a class
class Room:
    #2 attributes to be assigned
    length = 0.0
    width = 0.0
    #method of class to calculate the area
    def calculate_area(self):
        self.area = self.length*self.width
        return self.area
    
    def calculate_area2(self):
        print(f"Area of Room = ", self.length*self.width)
        
# create object of the Room class (i'm saying that study_room is of the class Room()
#AKA it can be classified as a room
study_room = Room()

#assign values to all of the attributes
study_room.length = 42.5
study_room.width = 30.8

print(f"Area is = ", study_room.calculate_area())

print(f"================= Method printing as part of the method ====================")

study_room.calculate_area2()
