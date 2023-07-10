class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating objects (instances) of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing object attributes and methods
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

person1.greet()  # Output: Hello, my name is Alice and I'm 25 years old.
person2.greet()  # Output: Hello, my name is Bob and I'm 30 years old.