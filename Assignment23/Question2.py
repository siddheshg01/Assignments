from multiprocessing import Pool
import os

def SumOdd(no):
    sum = 0

    for i in range(1, no + 1, 2):
        sum = sum + i

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Sum of Odd Numbers :", sum)
    print()

    return sum

def main():

    data = list(map(int, input("Enter numbers : ").split()))

    p = Pool()

    p.map(SumOdd, data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()