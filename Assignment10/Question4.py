def Even():
    a = int(input("enter first number "))
    for i in range(2,a+1):
        if (i  % 2 == 0):
            print(i)
          
def main():
    Even()

if __name__ == "__main__":
    main()