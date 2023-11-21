print("simple calculator")

num1=int(input("enter any number"))
num2=int(input("enter any number"))
res=0


print("please the choose the operation number to perform task")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input())

if choice==1:
    res=num1+num2
elif choice==2:
    res=num1-num2

elif choice==3:
    res=num1*num2
elif choice ==4:
    res =num1/num2
else:
    print("please choose valid choices")

print("your result:",res)
