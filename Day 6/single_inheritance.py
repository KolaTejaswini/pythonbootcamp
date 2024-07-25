#inheritance
#Single inheritance
class Animal():
    def speak():
        return "Animal is speaking"
#Multilevel inheritance
class Dog():
    def bark():
        return "bow"
class Puppy():
    def talk() :
        return"iam Puppy"
obj2=Dog
obj3=Puppy
print(obj2.bark())
print(obj3.talk())

#Multiple inheritance
class Father():
    def Father_speak():
        return "Father class"
class Mother():
    def Mother_speak():
        return "Mother class"
class Kid(Father,Mother): 
    def Kid_speak():
        return "iam kid from Father class and Mother"
obj4=Kid
print(obj4.Father_speak())
print(obj4.Mother_speak())
print(obj4.Kid_speak())
