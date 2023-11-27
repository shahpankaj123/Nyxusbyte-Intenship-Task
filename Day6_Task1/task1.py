from abc import ABC
class Inventory(ABC):
    id=0
    raw_data=[]

    @classmethod
    def getid(cls):
        cls.id+=1
        return cls.id
    @classmethod
    def getdata(cls):
        return cls.raw_data
    
    def __init__(self,name,price,quantity,category):
        
        self.id=self.getid()
        self.name=name
        self.price=price
        self.quantity=quantity
        self.category=category     

    def add_item(self):
        self.getdata().append({'id':self.id,'name':self.name,'price':self.price,'quantity':self.quantity,'category':self.category})
        



    
    def view_all_item(self):
         g=False
         for item in self.getdata():
             print("id",item['id'],"Name",item['name'],"price:",item['price'],"quantity:",item['quantity'],"category:",item['category'])  
             g=True
         if g == False:
             print("no data found")    

    def report_item(self):
        try:  
          
          t=False
          for item in self.getdata():
              if item['quantity'] < 10:
                   print("id",item['id'],"Name",item['name'],"price:",item['price'],"quantity:",item['quantity'],"category:",item['category']) 
                   t=True
          if t==True:
              print("these are the product with the minimum quantity")
                         
          if t == False:
              print("quantity less 10 not available") 
        except Exception as e:
            print(e)   

    def update_item_info(self):
        try:
           id= int(input("enter the id of product:"))
           t=False
           for item in self.getdata():
              if item['id'] == id:
               print("your product name :",item['name'])
               price=int(input('enter new price :'))    
               quantity=int(input('enter the new quantity:'))
               category=input("enter the category of product:")
               item['price']=price
               item['quantity']=quantity
               item['category']=category
               t=True
           if t ==False: 
               print("id number not found")            
        except Exception as e:
            print(e) 

    def del_item(self):
        try:
           id= int(input("enter the id of item:"))
           for item in self.getdata():
              if item['id'] == id:
                   self.getdata().remove(item)
                   print(self.getdata())
                   t=True  
           if t == False:
              print("id number not found")   

        except Exception as e:
            print(e) 

class Electronic(Inventory):
    def __init__(self, name, price, quantity, category):
        super().__init__(name, price, quantity, category)


g=0

while g==0:
   def exit():
    choice=input("-Are you sure want to exit?(Y/N)") 
    if choice == 'Y' or choice == 'y':
      print("-Thank you ")
      return 1
    
   print("---- Inventory management system ----")
   print("add -> add item")
   print("view -> view all item")
   print("report -> look report of item")
   print("update -> update item")
   print("del -> delete item")
   print("exit -> exit")

   choice=input("enter your choice :")
  

   if choice == 'add':
       try:
           name=input('enter the name of product:')
           price=float(input("enter the price of product:"))
           quantity=int(input("enter the quantity of product"))
           category=input("enter the name of category")      
           data=Electronic(name,price,quantity,category)
           data.add_item()
           print(id(data))
           print(Electronic.raw_data)
       except Exception as e:
           print(e)

   elif choice == 'view':
          data.view_all_item()
          print(id(data))
   elif  choice == 'report':
          data.report_item()  
   elif  choice == 'update':
          data.update_item_info()    
   elif  choice == 'del':
          data.del_item()    

   elif  choice == 'exit':
       g=exit() 
   else:
       print("please choose valid choice")   