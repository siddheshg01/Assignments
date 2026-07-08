def AddFactors(no):
    sum = 0

    for i in range(1, no):
        if(no % i == 0):
            sum = sum + i

    return sum

def main():
    num = int(input("Enter a number: "))

    ans = AddFactors(num)
    print("Addition of factors =", ans)

if __name__ == "__main__":
    main()