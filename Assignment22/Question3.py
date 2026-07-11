from multiprocessing import Pool

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False

    return True


def PrimeCount(no):
    count = 0

    for i in range(1, no + 1):
        if ChkPrime(i):
            count += 1

    return count


def main():

    data = list(map(int, input("Enter numbers : ").split()))

    p = Pool()

    result = p.map(PrimeCount, data)

    p.close()
    p.join()

    for i in range(len(data)):
        print("Prime count between 1 and", data[i], "=", result[i])


if __name__ == "__main__":
    main()