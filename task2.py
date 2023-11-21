import random

print("Guessing game")
random_number=random.randint(1,100)
print(random_number)
i=3
while(i>0):
    print("Plaese guess any number between 1 to 100")
    num=int(input())
    if num==random_number:
        print("congrats you won ")
        break
    if num>random_number:
        print("your guessed number is greater than actual number ")  
    if num <random_number:
        print("your guessed number is lower than actual number ") 
       
    i-=1
    print("you have left trial",i) 
