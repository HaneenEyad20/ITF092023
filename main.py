#first solu#

operator=input("please enter ur operator: ")
num1=int (input("enter num 1: "))
num2=int (input("enter num 2: "))
if operator=="+" : print(num1+num2)
elif operator=="-":print(num1 - num2)
elif operator=="*" : print(num1*num2)
elif operator=="/" : print(num1/num2)
else:
    print("sth wrong")
###########
#second solu#

def add(x,y):
          total=x+y
          print(total)

num1 = int (input("enter num 1"))
num2 = int (input("enter num 2"))
add(num1,num2)
###########
def sub(x, y):
    total = x - y
    print(total)
num1 = int(input("enter num 1"))
num2 = int(input("enter num 2"))
sub(num1, num2)
#######
def mul(x, y):
    total = x * y
    print(total)
num1 = int(input("enter num 1"))
num2 = int(input("enter num 2"))
mul(num1, num2)
##########
def div(x, y):
    total = x / y
    print(total)
x = int(input("enter num 1"))
y = int(input("enter num 2"))
div(x, y)

