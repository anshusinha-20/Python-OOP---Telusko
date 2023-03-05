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