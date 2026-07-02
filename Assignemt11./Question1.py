#write a program which accepts a number and checks whether it is a prime number or not.
def prime(n):
   if n <= 1:
        return False
   for i in range (2, n):
         if n % i ==0:
             return False
   return True

def main():
    c = int(input("Enter a number: "))
    a= prime(c)
    if True == a:
        print(c,"is a prime number")
    else:
        print(c,"is not a prime number")


if __name__ == "__main__":
    main()