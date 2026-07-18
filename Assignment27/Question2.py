class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        Money = float(input("Enter Deposit Amount : "))
        self.Amount += Money
        print("Amount Deposited Successfully")

    def Withdraw(self):
        Money = float(input("Enter Withdraw Amount : "))

        if Money <= self.Amount:
            self.Amount -= Money
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


Obj1 = BankAccount("Siddhesh", 10000)
Obj2 = BankAccount("Rahul", 5000)

print("Object 1")
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest :", Obj1.CalculateInterest())
Obj1.Display()

print("\nObject 2")
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest :", Obj2.CalculateInterest())
Obj2.Display()