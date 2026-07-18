class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are :")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum += i

        return Sum


Obj1 = Numbers(int(input("Enter First Number : ")))
Obj2 = Numbers(int(input("Enter Second Number : ")))

for Obj in [Obj1, Obj2]:

    print("\nNumber :", Obj.Value)

    print("Prime :", Obj.ChkPrime())
    print("Perfect :", Obj.ChkPerfect())

    Obj.Factors()

    print("Sum of Factors :", Obj.SumFactors())