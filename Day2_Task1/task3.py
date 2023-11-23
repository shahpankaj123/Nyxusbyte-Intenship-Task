t=0
book_list=[]
while t==0:
  def add_book(book_list):
    
    name=input("-enter the book name")
    author=input("-enter the author name")
   
    if len(book_list)== 0:
      book_list.append({'name':name,'author':author})
      print(book_list[0]['name'])
      
      
    for x in range(0,len(book_list)):
      if book_list[x]['name'] != name:
       book_list.append({'name':name,'author':author})
       print(book_list[x]['name'])
      else:
        print("-you cannot add same book") 
     

  def remove_book(book_list):
    name=input("-enter the name of book")
    g=False
    for book in book_list:
      if book['name'] == name:
        book_list.remove(book)
        g=True
        print("-removed sucessfully")
    if g == False:
      print("-your book name not found")    
     
       



  def display(book_list):
    if len(book_list) == 0:
      print("-book not found")
    else:  
      print("-Name of book:")
      for x in range(0,len(book_list)):
       print(book_list[x]['name']) 

  def exit():
    choice=input("-Are you sure want to exit?(Y/N)") 
    if choice == 'Y' or choice == 'y':
      print("-Thank you for playing")
      return 1

  print("Managing book")
  

  print("add->add a book")
  print("remove-> remove a book")
  print("display-> display a book")
  print("exit-> exit")


  choice=input("-enter your choice:")

  if choice == 'add':
    add_book(book_list)
  elif choice == 'remove':
    remove_book(book_list)
  elif choice == 'display':
    display(book_list)
  elif choice == 'exit':
    t=exit()
  else:
    print("please choose the correct choice")
 

