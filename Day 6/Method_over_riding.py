#Method overriding
class Animal():
    def speak():
        return "Animal is speaking"
class Dog(Animal):
     def speak():
        return "Dog is speaking"
class Puppy():
    def speak():
        return "Puppy is speaking"
obj3=Puppy
print(obj3.speak())