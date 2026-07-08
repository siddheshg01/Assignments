from functools import reduce

def main():

    Data = list(map(int, input("Enter elements : ").split()))

    FData = list(filter(lambda no: no % 2 == 0, Data))
    print("List after filter =", FData)

    MData = list(map(lambda no: no * no, FData))
    print("List after map =", MData)

    RData = reduce(lambda x, y: x + y, MData)
    print("Output of reduce =", RData)

if __name__ == "__main__":
    main()