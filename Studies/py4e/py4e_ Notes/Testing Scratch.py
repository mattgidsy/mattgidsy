#create class
class Bike:
    #name and gear are attributes of bike
    name = ""
    gear = 0

#create objects of class
bike1 = Bike()
 #access value of the attribute, gear, in the bike object
print(bike1.gear)

#modify or assign new values 
bike1.gear = 420
bike1.name = "Montain Bike"

print(bike1.gear)
print(f"Name: {bike1.name}  Gears: {bike1.gear}")