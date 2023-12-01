import re
class Account:
    
    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.email_check=False
        self.password_check=False


    def check_email(self):
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if email_pattern.match(self.email):
           print("Valid email address")
           self.email_check=True
        else:
           print("Invalid email address")

    def check_password(self):
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+{};:,<.>]).{8,}$')
        if password_pattern.match(self.password):
            print("valid password")
            self.password_check=True
        else:
            print("invalid password") 
    def register(self):
        if self.password_check and self.email_check:
            print("you account is created") 
        else:
            print("soory account not created") 


ram=Account("aaryanshah615gmail.com","Pankaj123@#")
ram.check_email()
ram.check_password()
ram.register()
