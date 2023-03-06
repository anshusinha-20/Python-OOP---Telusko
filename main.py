## Class and objects
# """creating class"""
# class Computer:
#     """method"""
#     def config(self):
#         print("i3, 8gb ram, 256gb ssd")


# """creating object"""
# comp1 = Computer()
# """print type of comp1"""
# print(type(comp1))
# """assigning method to objects"""
# comp1.config()

#####

## The __init__ method

# """creating class"""
# class Computer:

#     """init method"""
#     def __init__(self, processor, ram): # self is the object being passed
#         self.processorName = processor
#         self.ramCapacity = ram

#     """method"""
#     def config(self):
#         print(f"{self.processorName}, {self.ramCapacity}gb")


# """creating object"""
# comp1 = Computer("i9", 16)
# comp2 = Computer("ryzen 5", 32)

# """print type of comp1"""
# # print(type(comp1))

# """assigning method to objects"""
# comp1.config()
# comp2.config()

#####

## Constructor, self and comparing objects
# """creating computer class"""
# class Computer:

#     """init method"""
#     def __init__(self):
#         self.name = "Anshu"
#         self.age = 19

#     """update method"""
#     def update(self):
#         self.name = "Sahil"
#         self.age = 17

#     """compare method"""
#     def compare(self, other): # here self = c1 and other = c2
#         if (self.age > other.age):
#             print(f"{self.name} is older than {other.name} by {self.age - other.age} years")
#         else:
#             print(f"{other.name} is older than {self.name} by {other.age - self.age} years")


# """creating objects"""
# c1 = Computer()
# c2 = Computer()

# """changing the attibute values"""
# # c2.name = "Sahil"
# # c2.age = 17

# """updates the attributes of the c2 object by calling the update method"""
# c2.update()

# """comparing ages by calling the compare method"""
# c1.compare(c2)

#####

## Types of variables
# """creating car class"""
# class Car:

#     """creating static/class variables"""
#     wheels = 4

#     """creating init method"""
#     def __init__(self):
#         self.mileage = 10
#         self.brand = "Tesla"


# """creating objects"""
# c1 = Car()
# c2 = Car()

# c2.mileage = 8
# c2.brand = "Kia"

# print(c1.brand, c1.mileage, c1.wheels)
# print(c2.brand, c2.mileage, c2.wheels)

# """trying to change the class variable"""
# c1.wheels = 3
# print(f"{c1.brand} should have {c1.wheels} wheels!") # it works

# """changing the class variable for all the objects"""
# Car.wheels = 5

# """printing the update value"""
# print(c1.brand, c1.mileage, c1.wheels)
# print(c2.brand, c2.mileage, c2.wheels)

#####

## Types of methods
# """creating class"""
# class Student:
    
#     """class variable"""
#     school = "Telusko"

#     """init method"""
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     """method to find avg"""
#     def avg(self): # instance method, because it works with the instance variables
#         return round((self.m1 + self.m2 + self.m3) / 3, 2)
    
#     """creating class methods, which works with the class variable"""
#     @classmethod
#     def info(cls):
#         return cls.school # accessing the class variable
    
#     """creating static method"""
#     @staticmethod
#     def statInfo():
#         return "This is a return string from a static method"
    

# """creating objects"""
# s1 = Student(98, 87, 99)
# s2 = Student(88, 91, 90)

# """calling the avg method"""
# print(s1.avg())
# print(s2.avg())

# """calling the class method"""
# print(Student.info())

# """calling the static method"""
# print(Student.statInfo())

#####

## Inner class
# """creating outer class"""
# class Student:

#     """init method"""
#     def __init__(self, name, rollNo):
#         self.name = name
#         self.rollNo = rollNo
#         self.laptop = self.Laptop()

#     """show method"""
#     def show(self):
#         print(self.name, self.rollNo)
#         self.laptop.showConfig()

#     """creating innerclass"""
#     class Laptop:

#         """creating init method in inner class"""
#         def __init__(self):
#             self.brand = "Apple"
#             self.processor = "M2"
#             self.ram = "16gb"

#         """creating showConfig method"""
#         def showConfig(self):
#             print(self.brand, self.processor, self.ram)


# """creating objects"""
# s1 = Student("Anshu", 1)
# s1.show()