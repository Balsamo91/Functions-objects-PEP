class Dog:
    species = "Dog" # class attributes

    def __init__(self, name, age): # conctructor
        #Initialize name and age atttributes.
        self.name = name
        self.age = age

    def show_info(self):
        # Display a sentence showing the dogs name and age
        print(f"My dog's name is {self.name} and he-she is {self.age} years old.")

# Creating instances of Dog class
my_dog = Dog("Daisy", 3)
my_friend_dog = Dog("Emmet", 12)

# Calling functions on those objects
my_dog.show_info()
my_friend_dog.show_info()

# Accesing attributes from objects 
print(f"{my_dog.name} is going fo a walk!")
print(f"{my_friend_dog.name} is taking a poo!")

# Accessing clas attributes
print(my_dog.species)
print(my_friend_dog.species)

# Overwriting class attribute
Dog.species = "Good Dog"

print(my_dog.species)
print(my_friend_dog.species)