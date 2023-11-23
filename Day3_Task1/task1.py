print("--managing to-do list--")
t=0
to_todo_list=[]
a=0

while t==0:
  def add_task(list1):
    task_desc=input("enter the detail of task")
    
    g=False
    for task in list1:
       if task['Task'] == task_desc:
          print("you cannot add same task")
          g=True
    if g==False:
      list1.append({"Task":task_desc,"status":False}) 
      print(list1)   
    

  def mark_complete(list1): 
    task_name=input("enter the task") 
    g=False
    for task in list1:
      if task['Task'] == task_name:    
        task['status']=True
        print("task commpleted marked")
        g=True
    if g==False:
      print("task not found")  

  def  task_display(list1):
    g=False
    for task in list1:
      print('task:',task['Task'],"status:",task['status']) 
      g=True
    if g == False:
      print("Empty task")

  def complete_task(list1):
    g=False
    for task in list1:
      if task['status']:
        print('task:',task['Task'],"status:",task['status']) 
        g=True
    if g == False:
      print("completed task not found ")
  def incomplete_task(list1):
    g=False
    for task in list1:
      if task['status'] == False:
        print('task:',task['Task'],"status:",task['status']) 
        g=True
    if g == False:
      print("incompleted task not found ")

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
    elif choice == 'help':
      help()
    elif choice == 'exit':
      t=exit()  
    else:
      print("choose valid option")    
  if a ==0:
   menu() 
   a=1  
  else:
    help()  


