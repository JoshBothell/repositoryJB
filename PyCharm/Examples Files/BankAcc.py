class BankAcc(object):
    def __init__(self, name):
        self.account_num = input("Enter your account number: ")
        self.phone_num = input("Enter your phone number: ")
        self.pin_num = 25717
        self.balance = 0
        self.name = name

    def credit_acc(self):
        get_pin = input("Enter your pin: ")
        while True:
            if get_pin != self.pin_num:
                get_pin = input("What is your pin: ")
            else:
                ammount = input("How much do you want to deposit: ")
                self.balance -= ammount
                break

    def debit_acc(self):
        get_pin = input("Enter your pin: ")
        while True:
            if get_pin != self.pin_num:
                get_pin = input("What is your pin: ")
            else:
                ammount = input("How much do you want to add to your account: ")
                if ammount <= self.balance:
                    self.balance -= ammount
                    break
                else:
                    print("You lack the funds to do so...")
                break

