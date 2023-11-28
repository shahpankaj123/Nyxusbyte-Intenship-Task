class  LibraryMember:
    member_data=[]
    
    @classmethod
    def getdata(cls):
        return cls.member_data
    
    def add_member(self):
       try: 
        name=input("enter your name:")
        address=input("enter your address:")
        roll=int(input("enter the roll of student"))
        semester=input("enter the semester of student:")
        self.getdata().append({'name':name,'address':address,'roll':roll,'semester':semester,'book_taken':0})
       except Exception as e:
            print(e)   
    def update_member(self):
        try:
           roll= int(input("enter the roll of student:"))
           t=False
           for member in self.getdata():
              if member['roll'] == roll:
                name=input("enter your name:")
                address=input("enter your address:")
        
                semester=input("enter the semester of student:")
               
                member['name']=name
                member['address']=address
                member['semester']=semester
                t=True
           if t ==False: 
               print("Roll number not found")            
        except Exception as e:
            print(e)  
    def Remove_member(self):
        try:
           roll= int(input("enter the roll of number:"))
           for member in self.getdata():
              if member['roll'] == roll:
                   self.getdata().remove(member)
                   print(self.getdata())
                   t=True  
           if t == False:
              print("roll number not found")   

        except Exception as e:
            print(e)           
        
        
