"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/16/2020
Homework Problem: #6
Description: A program that prints different instances of a pet class and also
prints each class properties

"""


class Pet:
    """
    The base class `Pet` for the project
    """

    # Create two variables kind and color; assign values
    kind = "animal"
    color = "brown"

    def __init__(self, name):
        """
        Initializes the base class `Pet`
        """

        # In the constructor, initialize the pets name
        self.name = name

    def __str__(self):
        """
        Overrides description of base class `Pet`
        """

        # return a string with the name and description of pet so that it
        # matches the sample output from assignment
        return f"I am an {Pet.color} {Pet.kind} named {self.name}."

    def do_tricks(self):
        """
        A method for doing tricks
        """

        # Call the speak method
        # Call the jump method
        # return the name of the pet and that it is doing tricks
        return f"{self.name} is doing tricks", self.speak(), self.jump()

    def speak(self):  # this will be overridden - leave as is
        pass

    def jump(self):   # this will be overridden - leave as is
        pass


class Jumper(Pet):
    """
    The mixin class Jumper for the project
    """

    def jump(self):
        """
        The jump method for jump action
        """

        # return pet's name and that the Pet is jumping
        return f"{self.name} is jumping"


class Dog(Jumper):    # You will need to inherit for this to work
    """
    The class for `Dog` which is inherits from `Pet` and `Jumper`
    """

    # Change kind to canine
    kind = "canine"

    def __str__(self):
        """
        Overrides description of class `Dog`
        """

        # return the name and a description of dog so that it matches the
        # sample output from assignment
        return f"I am a dog named {self.name}."

    def call_the_dog(self):
        """
        Public method to call `__call` private method and returning its value
        """

        # Use this public method to call the private __call(self) method
        # Return the string returned by the private method
        return self.__call()

    def __call(self):
        """
        Private method for returning the rollover and owner actions
        """

        # Rollover action returns the name of the dog and that it is rolling
        # over

        # Owner action returns the name of the owner
        return f"{self.name} is rolling over", f"My owner is Chris"


class BigDog(Dog):    # You will need to inherit for this to work
    """
    The class for `BigDog` which is inherits from `Dog`, `Pet` and `Jumper`
    """

    # Change the color to tan
    color = "tan"

    def __str__(self):
        """
        Overrides description of class `BigDog`
        """

        # return the name and description of BigDog so that it matches the
        # sample output from assignment
        return f"{self.name} is a large and muscular dog."

    def speak(self):
        """
        Method for returning what the big dog says
        """

        return f"{self.name} says woof!"


class SmallDog(Dog):    # You will need to inherit for this to work
    """
    The class for `SmallDog` which is inherits from `Dog`, `Pet` and `Jumper`
    """

    # Change the color to brindle
    color = "brindle"

    def __str__(self):
        """
        Overrides description of class `SmallDog`
        """

        # return the name and description of SmallDog so that it matches the
        # sample output from assignment
        return f"{self.name} is a tiny and cute dog."

    def speak(self):
        """
        Method for returning what the small dog says
        """

        return f"{self.name} says yip!"


class Cat(Jumper):     # You will need to inherit for this to work
    """
    The class for `Cat` which is inherits from `Pet` and `Jumper`
    """

    # Change the kind to feline
    kind = "feline"

    def __str__(self):
        """
        Overrides description of class `Cat`
        """

        # return the name and description of cat so that it matches the
        # sample output from assignment
        return f"I am a cat named {self.name}."

    def speak(self):
        """
        Method for returning what the cat says
        """

        # return cats name and what it says
        return f"{self.name} says meow!!!"

    def climb(self):
        """
        method for returning the `climb` action
        """

        # return the name of the cat and that it is climbing
        return f"{self.name} is climbing the curtains again."


class HouseCat(Cat):     # You will need to inherit for this to work
    """
    The class for `HouseCat` which is inherits from `Cat`, `Pet` and `Jumper`
    """

    # Change the color to white
    color = "white"

    def __str__(self):
        """
        Overrides description of class `HouseCat`
        """

        # return the name and description of the house cat so that it matches
        # the sample output from assignment
        return f"{self.name} is a house cat with fluffy and " \
               f"{HouseCat.color} fur."

    def speak(self):
        """
        Method for returning what the house cat says
        """

        # return cats name and what it says
        return f"{self.name} says purr"


###############################################
# EXERCISES YOUR CODE
#
#    1. Instantiate each class(except Jumper)
#    2. Create a list of the instantiated objects
#    3. Loop through the objects
#    4. Print __str__
#    5. Print the Kind of pet
#    6. Print the Color of the pet
#    7. Have the pet do tricks
#    8. if applicable, print rollover action and the owners name
#    9. If applicable, have the pet climb
#   10. To separate each pet print a line of underscores
###############################################

# Your code to work with the class objects and print everything goes here!

animals_list = [
    Pet("Rover"),
    Cat("Lion"),
    Dog("Roo"),
    BigDog("Noah"),
    SmallDog("Lucky"),
    HouseCat("Zebra")
]

for animal in animals_list:
    print(f"{animal}\n{animal.kind}\n{animal.color}")

    do_trick, speak, jump = animal.do_tricks()
    print(f"{do_trick}")

    if speak is not None:
        print(f"{speak}")

    if jump is not None:
        print(f"{jump}")

    if animal.kind is "canine":
        rollover, owner = animal.call_the_dog()
        print(f"{rollover}\n{owner}")

    if animal.kind is "feline":
        print(animal.climb())

    print("_"*25)
