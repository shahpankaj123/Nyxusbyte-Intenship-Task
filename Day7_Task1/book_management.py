
class Book:
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
           name=input('enter the name of book:')
           price=float(input("enter the price of book:"))
           quantity=int(input("enter the quantity of book"))
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

