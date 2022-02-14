def message():
    print("hello python")
message()
message()

# argument in function.
def addition(a,b):
    c=a+b
    print("add=",c)
addition(5,9)

# or we can do like this also.
def addition(a,b):
    c=a+b
    print("add=",c)
a=int(input("please enter number:"))
b=int(input("pease enter number:"))
addition(a,b)

# return statement examples.
def add(a,b):
    c=a+b
    return c
x=int(input("please enter:"))
y=int(input("please enter:"))
z=add(x,y)
print(z)