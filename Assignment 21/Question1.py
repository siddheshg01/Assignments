import threading

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def Prime(arr):
    print("Prime Numbers:")
    for i in arr:
        if ChkPrime(i):
            print(i)


def NonPrime(arr):
    print("Non Prime Numbers:")
    for i in arr:
        if not ChkPrime(i):
            print(i)


def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        no = int(input("Enter element: "))
        data.append(no)

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()