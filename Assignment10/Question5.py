def odd():
    a = int(input("enter first number "))
    for i in range(1,a+1):
        if (i  % 2 != 0):
            print(i)
            
          
def main():
    odd()

if __name__ == "__main__":
    main()