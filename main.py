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