
# "Alejandro Perez Gonzalez"
# "A01746643"
def intro():
    print("ALGORITMOS COMPUTACIONALES")
    print("ALEJANDRO PÉREZ GONZÁLEZ A01746643")
def divideList(arr, low, high): #function use to divide the upper and lower values of the pivot
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):


        if arr[j] < pivot:

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, lowLimit, highLimit): #recursive function for sort
    if lowLimit < highLimit:

        pi = divideList(arr, lowLimit, highLimit)

        quickSort(arr, lowLimit, pi - 1)
        quickSort(arr, pi + 1, highLimit)


def main():
    #arr = [123,983,2,5,76,4,-12,43,-5,53,71,-34]
    temp=[]
    arr=[]
    file = open("numbers.txt","r")
    for lines in file:
        num = lines.split(",")
        for i in range(len(num)):
            num[i]=int(num[i])
    for j in range(len(num)):
        temp.append(num[j])
    for k in range(len(temp)):
        arr.append(temp[k])

    print("Input:"+ str(arr))
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Output:" + str(arr))

intro()
main()
