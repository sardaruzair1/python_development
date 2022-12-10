# functions in python
# indention is must in python functions

def greeting_function():
    print("hello world")

greeting_function()


# function with parameter
def parm_function(name):
    print("hello world ",name)

parm_function("sardar")

# function with two parameter
def two_parm_function(name, age):
    print("your name is ",name," and your age is ",age)

two_parm_function("sardar",19)

#function with tupple
def tupple_function(*names):
    print("your name is ",names[0])

tupple_function("sardar uzair","ali","muhammad aman")

# function with two parameter from input by using variable
def inp_parm_function(name, age):
    print("your name is ",name," and your age is ",age)
name = input("enter your name")
age  = input("enter your age")    
inp_parm_function(name,age)

# return i n python function
def return_parm_function(num1, num2):
    return num1 + num2
num1 = int(input("enter first number"))
num2  = int(input("enter second number"))    
print(return_parm_function(num1,num2))