class Student:
    id=0
    student_data=[]

    @classmethod
    def getroll(cls):
        cls.id+=1
        return cls.id
    @classmethod
    def getdata(cls):
        return cls.student_data
    
    def __init__(self,name,marks):
        self.name=name
        self.roll=self.getroll()
        self.marks=marks
        

    def add_student(self):
        self.getdata().append({'name':self.name,'roll':self.roll,'marks':self.marks})
        



    
    def view_all_student(self):
         g=False
         for student in self.getdata():
             print("Name",student['name'],"Roll number:",student['roll'],"Mark:",student['marks'])  
             g=True
         if g == False:
             print("no data found")    

    def search_student(self):
        try:  
          roll= int(input("enter the roll of student:"))
          t=False
          for student in self.getdata():
              if student['roll'] == roll:
                   print("Name :",student['name'],"Roll number:",student['roll'],"Mark:",student['marks']) 
                   t=True  
          if t == False:
              print("roll number not found") 
        except Exception as e:
            print(e)   

    def update_student_info(self):
        try:
           roll= int(input("enter the roll of student:"))
           t=False
           for student in self.getdata():
              if student['roll'] == roll:
               name=input('enter new name :')    
               marks=input('enter the marks:')
               student['name']=name
               student['marks']=marks
               t=True
           if t ==False: 
               print("roll number not found")            
        except Exception as e:
            print(e) 

    def del_student(self):
        try:
           roll= int(input("enter the roll of student:"))
           for student in self.getdata():
              if student['roll'] == roll:
                   self.getdata().remove(student)
                   print(self.getdata())
                   t=True  
           if t == False:
              print("roll number not found")   

        except Exception as e:
            print(e) 

    def display_student(self):
        data=self.getdata()

        for x in range(0,len(data)-1): #insertion sort
            for y in range(x,len(data)-1):
              if data[x]['marks']<data[y+1]['marks']:
                temp=data[x]
                data[x]=data[y+1]
                data[y+1]=temp

        for student in data :
                print("Name :",student['name'],"Roll number:",student['roll'],"Mark:",student['marks'])

    def __str__(self):
        return self.name + '_' + self.roll           
g=0

while g==0:
   def exit():
    choice=input("-Are you sure want to exit?(Y/N)") 
    if choice == 'Y' or choice == 'y':
      print("-Thank you ")
      return 1
    
   print("---- student management system ----")
   print("add -> add student")
   print("view -> view all student")
   print("search -> search student")
   print("update -> update student")
   print("del -> delete student")
   print("sort -> diplay stu detail with mark high")
   print("exit -> exit")

   choice=input("enter your choice :")
  

   if choice == 'add':
       try:
           name=input('enter the name of student :')
           marks=float(input("enter the mark of student:"))
           
           data=Student(name,marks)
           data.add_student()
           print(id(data))
           print(Student.student_data)
       except Exception as e:
           print(e)
   elif choice == 'view':
          data.view_all_student()
          print(id(data))
   elif  choice == 'search':
          data.search_student()  
   elif  choice == 'update':
          data.update_student_info()    
   elif  choice == 'del':
          data.del_student()    
   elif  choice == 'sort':
          data.display_student() 
   elif  choice == 'exit':
       g=exit() 
   else:
       print("please choose valid choice")                        

              
              

        










        