import Marvellousnum

def ListPrime(arr):
    sum = 0

    for i in arr:
        if(Marvellousnum.ChkPrime(i)):
            sum = sum + i

    return sum

def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        no = int(input("Enter element: "))
        data.append(no)

    ans = ListPrime(data)

    print("Addition of prime numbers =", ans)

if __name__ == "__main__":
    main()