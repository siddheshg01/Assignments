def ChkPrime(no):
    for i in range(2, no):
        if(no % i == 0):
            return False

    return True

def main():
    num = int(input("Enter a number: "))

    if ChkPrime(num):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()