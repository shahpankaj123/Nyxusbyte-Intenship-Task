import member_management
import task1
from datetime import date
class Bookrent:
    borrow_data=[]
    def givebook(self):
        roll=int(input("enter the roll number of student"))
        id=int(input('enter the id of book:'))
        today = date.today()
        
       
       
        list=[mem for mem in member_management.LibraryMember.getdata() if  mem['roll']==roll]
        list2=[book for book in task1.Book.getdata() if book['id']==id] 
        print(list,list2)
        if list and list2:
            self.borrow_data.append({"book_id":id,"roll":roll,"date":today})
            print(self.borrow_data)
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
        if g==False:
                print('data not found')
