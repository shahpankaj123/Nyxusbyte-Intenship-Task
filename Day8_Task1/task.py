import os
print("--managing to-do list--")
t=0
current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = 'todo.txt'
file_path = os.path.join(current_directory, file_name)
while t==0:
  def add_task():
    try:
       task_desc=input("enter the detail of task")
       status="False"
       data=task_desc + " " + status + "\n"
       file=open(file_path,"a")
       file.write(data)
       print("To-do task inserted successfully")
       file.close()
    except Exception as e:
      print(e)
      
    

  def mark_complete(): 
    task_name=input("enter the task") 
    try:
      g=False
      file = open(file_path, 'r')
      lines=file.readlines()
      for i,line in enumerate(lines):
        if task_name in line:
            lines[i] = task_name +' ' +'True' + '\n'
            g=True
      if g==True:      
       with open(file_path, 'w') as file:
         file.writelines(lines)
      else:
        print('task not found')   
    except Exception as e:
      print(e)       
      
  def  task_display():
    try:
      g=False
      file = open(file_path, 'r')
      for line in file:
        word=line.split()
        print('task:',word[0],"status:",word[1])
        g=True
      if g==False:
        print("no data")
    except Exception as e:
      print(e)        


  def complete_task():
    try:
      g=False
      file = open(file_path, 'r')
      for line in file:
        word=line.split()
        if word[1] == 'True':
          print('task:',word[0],"status:",word[1])
          g=True
      if g==False:
        print("no data")
    except Exception as e:
      print(e)  
    
  def incomplete_task():
    try:
      g=False
      file = open(file_path, 'r')
      for line in file:
        word=line.split()
        if word[1] == 'False':
          print('task:',word[0],"status:",word[1])
          g=True
      if g==False:
        print("no data")
    except Exception as e:
      print(e) 

  def exit():   
    choice=input("-Are you sure want to exit?(Y/N)") 
    if choice == 'Y' or choice == 'y':
      print("-Thank you for playing")
      return 1

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
      add_task()
    elif choice == 'complete':
       mark_complete()
    elif choice == 'view all':
        task_display()  
    elif choice == 'view complete':
       complete_task()    
    elif choice == 'view incomplete':
      incomplete_task()  
    elif choice == 'help':
      help()
    elif choice == 'exit':
      t=exit()  
    else:
     print("choose valid option")  
   
  
  menu() 
  