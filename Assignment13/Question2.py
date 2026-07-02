def Display(pi,radius):
    area = pi * radius * radius
    print("Area of circle is:", area)

def main():
    Pi =  3.14
    radius = float(input("Enter a radius: "))
    Display(Pi, radius)

if __name__ == "__main__":
    main()