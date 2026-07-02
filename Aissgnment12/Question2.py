def factor(n):
   for i in range(1,n+1):
      if n % i == 0:
         print("it is a  factor of that number", i)
        
   

def main():
  a = int(input("Enter a number: "))
  factor(a)
    
if __name__ == "__main__":
    main()