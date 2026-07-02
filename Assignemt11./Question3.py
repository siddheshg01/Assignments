def SumDigits(n):
    sum = 0

    while n > 0:
        digit = n % 10      
        sum = sum + digit   
        n = n // 10         

    return sum

def main():
    a = int(input("Enter a number: "))

    ret = SumDigits(a)

    print("Sum of digits is:", ret)


if __name__ == "__main__":
    main()