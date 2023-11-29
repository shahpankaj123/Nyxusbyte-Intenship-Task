import borrow_return
from datetime import datetime
import os
class Report:
    def generate_book_taken_report(self):
      try:  
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = 'example.txt'
        file_path = os.path.join(current_directory, file_name)
        file = open(file_path, 'w')
        file.write('Book taken by student')
        for data in borrow_return.Bookrent.getdata():
            data="roll number:",data['roll'],"id of book:",data['book_id'],"date:",data['date']
            print(data)
            file.write(str(data))

        file.close() 
      except Exception as e:
          print(e)
        

    def fine_report(self):
     try:   
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = 'example.txt'
        file_path = os.path.join(current_directory, file_name)
        file = open(file_path, 'w')
        file.write('Fine of student due to late return')
        today = datetime.today()
        formatted_date = today.strftime('%Y-%m-%d')
        date1 = datetime.strptime(formatted_date, '%Y-%m-%d')
        for data in borrow_return.Bookrent.getdata():
            dat2=data['date']
            date2 = datetime.strptime(dat2, '%Y-%m-%d')
            date_difference = (date2 - date1).days
            if date_difference>10:
                data="roll number:",data['roll'],"id of book:",data['book_id'],"date:",data['date'],"fine:",'Rs100'
                print(data)
                file.write(str(data))
            else:
                print("there is no fine report till todat") 
                file.write("there is no fine report till todat")   

        file.close() 
     except Exception as e:
          print(e)         




        
