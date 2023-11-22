t=0
start_state=False
stop_state=True
while t==0:
  

  def start(start_state):
    if start_state:
      print("car is already in start state")
    else:
      print("car has started") 
    return False

  def stop(stop_state):
    if stop_state:
      print("car is already in stop state")
    else:
      print("car has stopped") 
    return False
    

  def exit():
    choice=input("Are you sure want to exit?(Y/N)") 
    if choice == 'Y' or choice == 'y':
      print("Thank you for playing")
      return 1

  print("Car Racing Games")
  print("start->start the car")
  print("stop->stop the car")
  print("exit->exit the game")



  choice=input("enter your choice:")


  if choice == 'start':
     stop_state=start(start_state)
     start_state=True
     

  elif choice == 'stop':
     start_state=stop(stop_state)
     stop_state=True
     

  elif choice == 'exit':
     t=exit()
  else:
    print("please choose the correct choice")   