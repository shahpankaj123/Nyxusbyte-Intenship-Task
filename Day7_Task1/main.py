import member_management
import borrow_return
import report
import book_management



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
   data=book_management.Book()
   member=member_management.LibraryMember()
  
   report_data=report.Report()
   bor=borrow_return.Bookrent()
  

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
       bor.givebook()  
   elif choice == 'return':
       bor.returnbook()  
   elif choice == 'report':
       report_data.generate_book_taken_report() 
   elif choice == 'fine':
       report_data.fine_report()               
   else:
       print("please choose valid choice")   