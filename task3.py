l1=[]
num=int(input("enter the  number of data"))
i=1
sum_even=0
sum_odd=0
while i<=num:
    num2=int(input("enter any number"))
    l1.append(num2)
    i+=1
for x in l1:
    if x % 2 == 0:
        sum_even+= x   
    else:
        sum_odd+=x

print("sum of even number:",sum_even)
print("sum of odd number:",sum_odd)        