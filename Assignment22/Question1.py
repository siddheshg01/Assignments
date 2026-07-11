from multiprocessing import Pool

def SumSquare(no):
    sum = 0

    for i in range(1, no + 1):
        sum = sum + (i * i)

    return sum

def main():

    data = list(map(int, input("Enter numbers : ").split()))

    p = Pool()

    result = p.map(SumSquare, data)

    p.close()
    p.join()

    print("Output :", result)

if __name__ == "__main__":
    main()