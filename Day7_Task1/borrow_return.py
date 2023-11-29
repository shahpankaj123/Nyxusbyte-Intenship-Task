import member_management
import book_management
from datetime import datetime

class Bookrent:
    borrow_data=[]

    @classmethod
    def getdata(cls):
        return cls.borrow_data
    
    def givebook(self):
        roll=int(input("enter the roll number of student"))
        id=int(input('enter the id of book:'))
        today = datetime.today()
        formatted_date = today.strftime('%Y-%m-%d')
        
       
       
        list=[mem for mem in member_management.LibraryMember.getdata() if  mem['roll']==roll]
        list2=[book for book in book_management.Book.getdata() if book['id']==id] 
        g=False
        for book in book_management.Book.getdata():
             if book['id'] ==id:
                  if book['quantity']>0:
                       book['quantity']-=1
                       g=True
        if g ==True:
          print(list,list2)
          if list and list2:
            self.borrow_data.append({"book_id":id,"roll":roll,"date":formatted_date})
            print(self.borrow_data)
            print(book_management.Book.getdata())
          else:
            print("data not found")  
       
                       
                       

    def returnbook(self):
        roll=int(input("enter the roll number of student"))
        id=int(input('enter the id of book:'))
        g=False
        for data in self.borrow_data:
           
            if data['book_id'] == id and data['roll'] ==roll:
                self.borrow_data.remove(data)
                print(self.borrow_data)

                print("Return book success")
                g=True
        if g:
            for book in book_management.Book.getdata():
             if book['id'] ==id:
                  if book['quantity']>0:
                       book['quantity']+=1
                       

        if g==False:
                print('data not found')
