mess=input("enter any string:")
message=mess.lower()
count=0

for x in message:
    if x == 'a' or x== 'e' or x == 'i' or x== 'o' or x== 'u':
        count+=1
print(count)        