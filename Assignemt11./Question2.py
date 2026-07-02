
def size(n):
   
   count = 0
   while n > 0:
      count = count + 1
      n = n // 10
   return count

def main():
  a = int(input("Enter a number: "))
  c= size(a)
  print(c)


if __name__ == "__main__":
    main()