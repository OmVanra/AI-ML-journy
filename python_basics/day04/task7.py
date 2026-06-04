# Q7. Create a class that allows the constructor to work with: 
# • name only 
# • name + age 
# • name + age + address 
# that 
# As direct constructor overloading (multiple constructors) are not allowed but 
# we have to use default parameters to simulate constructor overloading.

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

# Example usage
person1 = Person("Alice")
person2 = Person("Bob", 30)
person3 = Person("Charlie", 25, "123 Main St")
print(f"Person 1: Name: {person1.name}, Age: {person1.age}, Address: {person1.address}")
print(f"Person 2: Name: {person2.name}, Age: {person2.age}, Address: {person2.address}")
print(f"Person 3: Name: {person3.name}, Age: {person3.age}, Address: {person3.address}")


