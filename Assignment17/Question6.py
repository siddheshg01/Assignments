def Display(no):
    for i in range(1, no + 1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    num = int(input("Enter a number: "))
    Display(num)

if __name__ == "__main__":
    main()