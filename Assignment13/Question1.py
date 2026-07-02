def Display(l,w):
    area = l * w
    print("Area of rectangle is:", area)
   
def main():
    Length = float(input("Enter a Length: "))
    Width = float(input("Enter a Width: "))
    Display(Length, Width)

if __name__ == "__main__":
    main()