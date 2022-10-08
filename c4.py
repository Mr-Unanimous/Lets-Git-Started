def div(a,b):
    try:
        c=a/b
        print("Division is :- ",c)
    except :
        print("Division with zero is not possible!!!")
    finally:
        print("Program executed")

a=int(input("Enter the first number:- "))
b=int(input("Enter the second number:- "))
div(a,b)
