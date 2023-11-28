import member_management
import borrow_return

from abc import ABC
class Book(ABC):
    id=0
    raw_data=[]

    @classmethod
    def getid(cls):
        cls.id+=1
        return cls.id
    @classmethod
    def getdata(cls):
        return cls.raw_data
       

    def add_book(self):
        try:
           name=input('enter the name of product:')
           price=float(input("enter the price of product:"))
           quantity=int(input("enter the quantity of product"))
           author=input("enter the name of category")  
           self.getdata().append({'id':self.getid(),'name':name,'price':price,'quantity':quantity,'author':author})    
           
          
           print(self.getdata())
        except Exception as e:
           print(e)
        
        



    
    def view_all_book(self):
         g=False
         for book in self.getdata():
             print("id",book['id'],"Name of book:",book['name'],"price:",book['price'],"quantity:",book['quantity'],"author:",book['author'])  
             g=True
         if g == False:
             print("no data found")    

      

    def update_book_info(self):
        try:
           id= int(input("enter the id of book:"))
           t=False
           for book in self.getdata():
              if book['id'] == id:
               name=input("enter the name of book")
               price=int(input('enter new price :'))    
               quantity=int(input('enter the new quantity:'))
               author=input("enter the category of product:")
               book['name']=name
               book['price']=price
               book['quantity']=quantity
               book['author']=author
               t=True
           if t ==False: 
               print("id number not found")            
        except Exception as e:
            print(e) 

    def del_book(self):
        try:
           id= int(input("enter the id of book:"))
           for book in self.getdata():
              if book['id'] == id:
                   self.getdata().remove(book)
                   print(self.getdata())
                   t=True  
           if t == False:
              print("id number not found")   

        except Exception as e:
            print(e) 
    def __str__(self):
        return 'name'




g=0

while g==0:
   def exit():
    choice=input("-Are you sure want to exit?(Y/N)") 
    if choice == 'Y' or choice == 'y':
      print("-Thank you ")
      return 1
    
   print("---- Student management system ----")
   print("add -> add book")
   print("view -> view all book")
   
   print("update -> update book")
   print("del -> delete book")
   print("add_member -> add the member:")
   print("update_member -> update the data of member")
   print("delete_member -> delete the data of member")
   print("exit -> exit")

   choice=input("enter your choice :")
   data=Book()
   member=member_management.LibraryMember()
   borrow=borrow_return.Bookrent()
  

   if choice == 'add':
       
          
          data.add_book()

   elif choice == 'view':
          data.view_all_book()
          print(id(data)) 
   elif  choice == 'update':
          data.update_book_info()    
   elif  choice == 'del':
          data.del_book()    

   elif  choice == 'exit':
       g=exit() 
   elif choice == 'add_member':
       member.add_member()
   elif choice == 'update_member':
       member.update_member()
   elif choice == 'del_member':
       member.Remove_member() 
   elif choice == 'take':
       borrow.givebook()  
   elif choice == 'return':
       borrow.returnbook()           
   else:
       print("please choose valid choice")   