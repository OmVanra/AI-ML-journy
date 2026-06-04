# Q9. Create the following classes: Herbivore , Carnivore , Omnivore
# with some 
# attributes & methods. Then create a class Bear that inherits from all the above 
# classes to showcase how multiple inheritance works.

class Herbivore:
    def eat_plants(self):
        return "Eating plants."
class Carnivore:
    def eat_meat(self):
        return "Eating meat."
class Omnivore:
    def eat_both(self):
        return "Eating both plants and meat."
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

# Example usage
bear = Bear("Baloo")
print(f"{bear.name} is a bear that can:")
print(bear.eat_plants())
print(bear.eat_meat())
print(bear.eat_both())

