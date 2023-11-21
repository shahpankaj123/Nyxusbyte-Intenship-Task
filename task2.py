import random

print("Guessing game")


def guess():
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
guess()
w=0
while w==0:
 choice=input("do you want to continue (Y/N)") 
 if choice == 'Y' or choice == 'y':
   guess()
 else:
    w=1
    print("thank you")

  

