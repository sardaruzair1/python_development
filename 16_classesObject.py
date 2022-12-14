#  classes and objects in python
class myClass:
    x = 10

p1 = myClass()

print(p1.x)    

#__init__ in python classes

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p2 = Person('sardar',19)

print(p2.name)
print(p2.age)    


#  lets do it with another flavour


class programmers:
    def __init__(self,name,age):
        self.name = name
        self.age = age

name = input("enter your name: ")
age = input("enter your age: ")
p3 = Person(name,age)

print(p3.name)
print(p3.age)   