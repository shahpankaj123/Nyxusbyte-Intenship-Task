num=int(input("enter any number:"))

if num<0:
    num=num*-1

fac=1
for i in range(1,num+1):
    fac*=i

print("Factorial number of ",num,"is:",fac)    
