def CountDigits(no):
    count = 0

    while no > 0:
        count = count + 1
        no = no // 10

    return count

def main():
    num = int(input("Enter a number: "))

    ans = CountDigits(num)
    print("Number of digits =", ans)

if __name__ == "__main__":
    main()