from multiprocessing import Pool
import os

def Factorial(no):

    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Factorial :", fact)
    print()

    return fact


def main():

    data = list(map(int, input("Enter numbers : ").split()))

    p = Pool()

    p.map(Factorial, data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()