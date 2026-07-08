import threading

sum_result = 0
product_result = 1

def SumList(arr):
    global sum_result

    sum_result = sum(arr)

def ProductList(arr):
    global product_result

    for i in arr:
        product_result *= i

def main():

    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        no = int(input("Enter element: "))
        data.append(no)

    t1 = threading.Thread(target=SumList, args=(data,))
    t2 = threading.Thread(target=ProductList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum =", sum_result)
    print("Product =", product_result)

if __name__ == "__main__":
    main()