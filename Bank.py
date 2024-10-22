class Bank_account:
    def __init__(
        self, account_name, account_number: int, account_type, account_balance: float, password
    ):
        self.__account_name = account_name
        self.__account_number = account_number
        self.account_type = account_type
        self.__account_balance = account_balance
        self.__password = password

    @property
    def account_balance(self):
        return self.__account_balance
    
    def account_number(self):
        return self.__account_number

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        self.__account_name = new_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def change_password(self, new_password):
        self.__password = new_password
        print(f"Your password was chaged to {new_password}")

    def login(self):
        try:
            account_number = int(input("Enter account number "))
            password = input("Enter password ")
            if account_number != self.__account_number:
                print(f"The account number{account_number} is not valid")
            elif password != self.__password:
                print(f"the password is Invalid")
            else:
                print("login successful")
        except ValueError:
            print("account number must be integers")

    def withdraw(self, amount):
        amount = input("Enter amount to withdraw ")
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrawal of {amount} successful. Your balance: {self.__account_balance}")
        else:
            print("Insufficient Fund or Invalid amount")

    def deposit(self, amount):
        try:
            amount = float(input("Enter amount to deposit "))
            if 0 < amount:
                self.__account_balance += amount
                print(f"You deposited {amount} Your balance: {self.__account_balance}")
            else:
                print("Amount must be greater than 0!")
        except:
            print("Only accept numbers, try again ")

    def transfer(self, amount: float, other_bank: str, other_account_number: int):
        if len(str(other_account_number)) != 10:
            print("Account number must be 10 digits")
        elif amount < 0:
            print("Invalid amount")
        elif amount > self.__account_balance:
            print("Insufficient fund")
        else:
            self.__account_balance -= amount
            print(
                f"Your transfer of {amount} to {other_bank} : {other_account_number} is successful."
                f"Balance: {self.__account_balance}"
            )

    def check_balance(self):
        print(f"Your account balance is {self.__account_balance}")


account1 = Bank_account("Godfrey Obruche", 2263285695, 
                        "savings account", 200000, "engrprof")

#account1.password = input("enter a new password ")
#account1.change_password = input("Enter a new password ")
account1.change_password = 'myrealname'
account1.login()