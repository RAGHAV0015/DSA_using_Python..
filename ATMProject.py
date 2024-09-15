'''
class Atm:
    
    def __init__(self):
        self.balance = 0
        self.pin = ''
    
    def set_pin(self):
        self.pin = input("Enter your pin: ")
    
    def credit(self):
        pin = input("Enter the pin: ")
        if pin == self.pin:
            try:
                amount = float(input("The amount to be credited: "))
                if amount > 0:
                    self.balance += amount
                    print("Your current balance is:", self.balance)
                else:
                    print("Amount should be positive.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        else:
            print("Invalid pin")
    
    def debit(self):
        pin = input("Enter the pin: ")
        if pin == self.pin:
            try:
                amount = float(input("Enter the amount to debit: "))
                if amount > 0:
                    if amount > self.balance:
                        print("Insufficient balance")
                    else:
                        self.balance -= amount
                        print("Your current balance is:", self.balance)
                else:
                    print("Amount should be positive.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        else:
            print("Invalid pin")
    
    def check_balance(self):
        print(f"Your current balance is {self.balance}")
  
    def menu(self):
        while True:
            user_input = input(""" 
            1. Select 1 to set your pin
            2. Select 2 to credit amount
            3. Select 3 to debit amount
            4. Select 4 to check balance
            5. Select 5 to exit
            """)
            
            if user_input == '1':
                self.set_pin()
            elif user_input == '2':
                self.credit()
            elif user_input == '3':
                self.debit()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Exiting...")
                break
            else:
                print("Invalid input, try again...")

a = Atm()
a.menu()
'''
class Students:
    number_of_students =0
    def __init__(self,name,marks,roll_no):
        self.name =name
        self.__marks =marks
        self.roll_no =roll_no
        Students.number_of_students =Students.number_of_students+1
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,pass_word,new_marks):
        if pass_word==self.priv():
            self.__marks =new_marks
        else:
            print("incorrect password!!")
    
    def priv(self):
        return '0001'
s1 =Students("tom",98,1)
s1.set_marks('0001',99)
print(s1.get_marks())
s2=Students("jerry",2,97)
print(s2.get_marks(),s2.name,s2.roll_no)
print(Students.number_of_students)
