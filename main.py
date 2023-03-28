a=int(input("enter a value:"))
b=int(input("enter b value:"))
h=int(input("enter h value:"))

def divisionByTwo(additionValue):
    return(additionValue/2)

def multiplication(divisionValue,h):
    return(divisionValue*h)

def addition(a,b):
    return(a+b)

add=addition(a,b)
div=divisionByTwo(add)
mul=multiplication(div,h)
print("Traepzoid area is:",mul)

