class Bank:
    def __init__(self):
        self.__balance = 0   # private balance

    def add(self):
        ino = int(input("Enter amount to deposit: "))
        if ino > 0:
            self.__balance += ino
            print("Amount added successfully")
        else:
            print("Please enter valid amount")

    def wit(self):
        inon = int(input("Enter amount to withdraw: "))
        if inon <= self.__balance:
            self.__balance -= inon
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)


# Object
s1 = Bank()

s1.add()
s1.wit()
s1.show_balance()