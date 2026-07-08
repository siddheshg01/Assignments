from functools import reduce

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def main():

    Data = list(map(int, input("Enter elements : ").split()))

    FData = list(filter(ChkPrime, Data))
    print("List after filter =", FData)

    MData = list(map(lambda no: no * 2, FData))
    print("List after map =", MData)

    RData = reduce(lambda x, y: x if x > y else y, MData)
    print("Maximum =", RData)

if __name__ == "__main__":
    main()