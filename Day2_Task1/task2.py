s1=set()
s2=set()

num1=int(input("enter the size of 1st set"))
num2=int(input("enter the size of 2nd set"))

for i in range(1,num1+1):
    x=int(input("enter value of position"))
    s1.add(x)



for i in range(1,num2+1):
    x=int(input("enter value of position"))    
    s2.add(x)



res1=s1.union(s2)   
res2=s1.intersection(s2)

print(res1)
print(res2)
    
