def factorial(num):
    if(num==1):
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter a number"))
f=factorial(num)
print("Factorial of the no. is ",f)