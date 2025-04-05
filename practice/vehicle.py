class Vehicle:
   def __init__(self, name , speed):
       self.name = name
       self.speed = speed


firstVehicle = Vehicle("아빠 어부바",3)
print(f"firstVehicle.name = {firstVehicle.name},"
      f"firstVehicle.speed = {firstVehicle.speed}")