print("--managing to-do list--")
t=0
a=0
to_todo_list=[]
bin=[]
while t==0:
  def add_task(list1):
    task_name=input("enter the name of task :")
    task_desc=input("enter the detail of task :")
    
    g=False
    for task in list1:
       if task['name'] == task_name:
          print("you cannot add same task")
          g=True
    if g==False:
      list1.append({"name":task_name,"desc":task_desc,"status":False}) 
      print(list1)   
    

  def mark_complete(list1): 
    task_name=input("enter the task name :") 
    g=False
    for task in list1:
      if task['name'] == task_name:    
        task['status']=True
        print("task commpleted marked")
        g=True
    if g==False:
      print("task not found")  

  def  task_display(list1):
    g=False
    for task in list1:
      print('task:',task['name'],'Desc :',task['desc'],"status:",task['status']) 
      g=True
    if g == False:
      print("Empty task")

  def complete_task(list1):
    g=False
    for task in list1:
      if task['status']:
        print('task:',task['name'],'Desc :',task['desc'],"status:",task['status']) 
        g=True
    if g == False:
      print("completed task not found ")

  def incomplete_task(list1):
    g=False
    for task in list1:
      if task['status'] == False:
        print('task:',task['name'],'Desc :',task['desc'],"status:",task['status']) 
        g=True
    if g == False:
      print("incompleted task not found ")

  def Delete(list1,bin):
    task_name=input("enter the name of task to be deleted")
    g=False

    for task in list1:
      if task['name'] == task_name:
        choices=input("Do you want to delete Permantely (Y/N)")
        if choices.lower() == 'y':
          list1.remove(task)
          g=True
        else:
          list1.remove(task)
          bin.append(task) 
          g=True
        
        print(list1,bin)  
    if g == False:
        print("Enter task not found")  

  def Restore_task(list1,bin):
       name=input("enter the task name to be restore:")
       g= False
       for task in bin:
         if task['name'] == name:
           list1.append(task)
           bin.remove(task)
           g=True
           print(list1,bin)
       if g == False:
         print("Task not found")    

  def view_bin(bin):
    g=False
    for task in bin:
        print('task:',task['name'],'Desc :',task['desc'],"status:",task['status']) 
        g=True
    if g == False:
      print("Empty Bin")  

  def clear_bin(bin):
    choice=input("do you sure want to delete task of bin(Y/N):")
    if len(bin) == 0:
      print("bin doesnot contain any data")
    elif choice.lower() == 'y':
      bin.clear()
      print(bin)
    else:
      print("Bin contain the data.there is no loss of any data")  

  def exit():   
    choice=input("-Are you sure want to exit?(Y/N)") 
    if choice == 'Y' or choice == 'y':
      print("-Thank you for playing")
      return 1
    
  def help():
     mes=input("enter the help key to display all menu ")
     if mes.lower() == 'help':
       menu()

  

  def menu():
    print("add-> add a task")
    print("complete-> mark a task as complete")
    print("view all -> view the current task in the to-do list")
    print("view complete -> view complete task")
    print("view incomplete -> view incomplete task")
    print("Delete -> delete to-do task")
    print("Restore -> Restore the task")
    print("View bin -> view the task in the bin")
    print("clear bin -> clear all data of bin")
    print("help -> display all help message")
    print("exit -> exit")

    choice = input("enter your choice")

    if choice == 'add':
      add_task(to_todo_list)
    elif choice == 'complete':
       mark_complete(to_todo_list)
    elif choice == 'view all':
        task_display(to_todo_list)  
    elif choice == 'view complete':
       complete_task(to_todo_list)    
    elif choice == 'view incomplete':
      incomplete_task(to_todo_list)  
    elif choice == 'view bin':
      view_bin(bin)
    elif choice == 'clear bin':
      clear_bin(bin)    
    elif choice == 'help':
      help()
    elif choice == 'exit':
      x=exit()  
    elif choice == 'delete':
      Delete(to_todo_list,bin)  
    elif choice == 'restore':
       Restore_task(to_todo_list,bin) 
    else:
     print("choose valid option")  
   
  if a ==0:
   menu() 
   a=1  
  else:
    help()  
