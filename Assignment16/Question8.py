def Display(no):
    for i in range(no):
        print("*", end=" ")

def main():
    num = int(input("Enter a number: "))
    Display(num)

if __name__ == "__main__":
    main()