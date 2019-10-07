def bubbleSort():
    print ("BUBBLE SORT")
    notSorted = []
    notSorted = readFile()
    sorting = []
    sorting = notSorted
    executed = 0    
    for i in range (0,len(sorting)-1):
        for j in range (0,len(sorting)-i-1):
            if (int (sorting[j+1]) < int (sorting[j])):
                a1 = sorting[j] 
                a2 = sorting[j+1]
                sorting[j] = a2
                sorting[j+1] = a1
                executed = executed+1
                print(sorting)
    print(executed)
    return (sorting)
    


def testRead(numbersNotSorted):

    lista = []
    for i in range (0, len(numbersNotSorted)):
        lista.append(numbersNotSorted[i])
    print(lista)    
    
def readFile():
    print("READING FILE ")
    
    
    file = open("numbers.txt", "r")
    
    numbersNotSorted = []
    
    notSorted =  (file.read().split(','))
    
    numbersNotSorted = notSorted
    
    #testRead(numbersNotSorted)

    #print(numbersNotSorted)
    numbersNotSorted = [int(x) for x in numbersNotSorted]
    
    return numbersNotSorted

def intro():
    print("ALGORITMOS COMPUTACIONALES")
    print("OSCAR ZUNIGA LARA A01654827")


def main():
    intro()
    
    
    
    print (bubbleSort())
    
main()