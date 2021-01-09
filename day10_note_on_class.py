# The purpose of classes is to have a template of how the objects are designed.
# Without any designs, you cannot have an object
# In class nomenclature, attributes == variables, methods or behaviours == functions
# A class is a blue print from which you can make objects
# In class, object is a collection of properties that can be referred to as attributes and methods (funtions ie what the object can do, its behaviour)
# Class variables are attributes shared by all instances (objects) of a specific class while
# instance variables are attributes belonging to a specific instance of a class that is not shared
# by all instances of a class — they are variables that are specific to the object they are attached to
# __init__() is what defines instance variables. Any other is a class variable until an instance changes
# it within its own context, thereby adopting a new instance variable.
# instance variables are for data unique to each instance and class variables are for attributes and methods
# shared by all instances of the class:


class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)  # shared by all dogs
# prints 'canine'
print(e.kind)  # shared by all dogs
# prints 'canine'
print(d.name)  # unique to d
# prints Fido
print(e.name)  # unique to e
# prints Buddy


class Family:
    pass


# Family() is creating an object which is an instance of the class
# Instance of the class (Family()) is now stored in the variable class sodiq
# sodiq is now the variable which holds an instance of the class Family
sodiq = Family()


# A class instance is also called an object. The pattern of defining classes and
# creating objects to represent the responsibilities of a program is known as
# Object Oriented Programming or OOP
# Instantiation takes a class and turns it into an object, the type() function does
# the opposite of that. When called with an object, it returns the class that the
# object is an instance of.

print(type(sodiq))
# prints "<class '__main__.Family'>"

# In Python __main__ means “this current file that we’re running” and so one could read
# the output from type() to mean “the class Family that was defined here, in the
# script you’re currently running.”

# The type() command returns the namespace and class for the object provided.
# For classes defined in the local file, the namespace will be reported as __main__.
# For classes imported from other modules, the namespace reported will be the same as the module.

# CLASS VARIABLE
# When we want the same data to be available to every instance of a class we use a class variable.
# A class variable is a variable that’s the same for every instance of the class.
# You can define a class variable by including it in the indented part of your class definition,
# and you can access all of an object’s class variables with object.variable syntax.

# We defined the class Musician


class Musician:
    title = "Rockstar"  # class variable


# We instantiated drummer to be an object of type Musician
drummer = Musician()
# We then printed out the drummer.title attribute, which is a class variable that we defined
# as the string “Rockstar”
print(drummer.title)
# prints "Rockstar"
# If we defined another musician, like guitarist = Musician() they would have the same .title attribute.


# METHODS
# Methods are functions that are defined as part of a class. The first argument in a method is always the
# object that is calling the method. Convention recommends that we name this first argument self.
# Methods always have at least (self) arguement. We define methods similarly to functions, except
# that they are indented to be part of the class.

# Below we created a Dog class with a time_explanation method that takes one argument, self,
# which is the object calling the function. We created a Dog named pipi_pitbull and called the .time_explanation()
# method on our new object for Pipi. Notice we didn’t pass any arguments when we called .time_explanation(),
# but were able to refer to self in the function body. When you call a method it automatically passes the object
# calling the method as the first argument.

class Dogs:
    dog_time_dilation = 7  # class variable
    # class method

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(
            self.dog_time_dilation))


pipi_pitbull = Dogs()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."


# Methods with Arguments
# Methods can also take more arguments than just self:


class DistanceConverter:
    kms_in_a_mile = 1.609  # class variable

    # class method
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile


# Instantiating the class
converter = DistanceConverter()

# Notice again that even though how_many_kms takes two arguments in its definition,
# we only pass miles, because self is implicitly passed (and refers to the object converter).
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"


# CONSTRUCTORS
# The word “constructor” is used to describe similar features in other object-oriented programming languages
# but programmers who refer to a constructor in Python are usually talking about the __init__() method

# There are several methods in Python class with special behaviour
# They are sometimes called “magic,” because they behave differently from regular methods.
# A popular term used for methods is dunder methods, so-named because they have two underscores __init__

# __init__
class Shouter:
    def __init__(self, phrase):
        # make sure phrase is a string
        if type(phrase) == str:

            # then shout it out
            print(phrase.upper())


shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

# Above we’ve updated our Shouter class to take the additional parameter phrase.
# When we created each of our objects we passed an argument to the constructor. The constructor
# takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.

# The purpose of the __init__() method is to resolve the input parameters into instance
# attributes (the unique data given to the object).


class Circle:
    def __init__(self, radius):
        self.radius = radius


circle_a = Circle(1)       # instance a
circle_b = Circle(2)       # instance b

print(circle_a.radius)    # 1
print(circle_b.radius)    # 2

# Above, circle_a and circle_b are unique instances of the Circle class, and we can
# see they each have their own radius attribute. self in the above refers to the
# instance object in context when we poll the attributes or invoke the methods.


# ATTRIBUTE FUNCTIONS
# Both class and instance variables are considered attribute of an object or instance of a class
# If we try to access non-existence attribute, we get AttributeError
# To check if attribute exist (remember attributes referred to both class & instance variables), we can
# use hasattr()...it returns True if exist, else, False

# syntax hasattr(object, “attribute”)
# 1. object: the object we want to see its attribute
# 2. "attribute": the attribute we want to see if it exist

# getattr(object, “attribute”, default) # will return the value of a given object and attribute
# we can also supply a third argument that will be the default if the object does not have the given attribute.
# the getattr() function will not create an attribute which is not present. If a default value is provided,
# it will return that value at the time getattr() is called, otherwise an AttributeError error will be raised
# if no default value is provided.

# For every element in the list, check if the element has the attribute count
# using the hasattr() function
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")


# Attributes can be added to user-defined objects after instantiation, so it’s possible
# for an object to have some attributes that are not explicitly defined in an object’s constructor.

# STRING REPRESENTATION
# When we print out an object we get a default representation that seems fairly useless.
class Employee():
    def __init__(self, name):
        self.name = name


argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"
# This default string representation gives us some information, like where the class is defined
# and our computer’s memory address where this object is stored, but is usually not useful
# information to have when we are trying to debug our code
# __repr__() is a method we can use to tell Python what we want the string representation of the class to be.
# __repr__() can only have one parameter, self, and must return a string
# In our Employee class above, we have an instance variable called name that should be unique enough to be
# useful when we’re printing out an instance of the Employee class


class Employees():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


argus = Employees("Argus Filch")
print(argus)
# prints "Argus Filch"
# We implemented the __repr__() method and had it return the .name attribute of the object. When we printed
# the object out it simply printed the .name of the object!


class Profession:
    def __init__(self, name, job, designition):
        self.name = name
        self.job = job
        self.designition = designition

    def age_by_double(self, age):
        return age * 2


bb = Profession("Sodiq", "Data Engineer", "Senior")

print(bb.age_by_double(3))
