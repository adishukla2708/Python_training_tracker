import sys


def sec_lowest():
    n = int(input("Enter the number of items: "))
    arr = []

    for i in range(n):
        arr.append(int(input()))
    print("Entered Array is: ", arr, "\n")
    if n != 1:  # for array having just 1 element
        lowest = sys.maxsize

        for i in range(n):
            if arr[i] < lowest:
                lowest = arr[i]

        second_lowest = sys.maxsize

        for i in range(n):
            if second_lowest > arr[i] > lowest:
                second_lowest = arr[i]

        print("Second lowest mark in the array is: ", second_lowest)

    else:
        print(arr[0])


sec_lowest()