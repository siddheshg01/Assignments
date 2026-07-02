def Natural():
    a = int(input("enter first number "))
    sum = 0
    for i in range(1,a+1):
        sum = i + sum
        
    print(sum)



def main():
    Natural()

if __name__ == "__main__":
    main()