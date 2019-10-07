
import threading  
def mergeSort():
    print("MERGE SORT")
    notSorted = []
    notSorted = leerArchivo()
    sorting = []
    sorting = notSorted
    executed = 0    
    return(mergeSortReal(sorting))
    

def mergeSortReal(sorting):
    left = []
    right = []
    middle = 0
    size = len(sorting)
    if size > 1:
        i1=0 
        i2=0
        i3=0
        middle = size//2
        left = sorting[:middle]
        right = sorting[middle:]
        #mergeSortReal(left)            
        #mergeSortReal(right)           single thread sort
        t1 = threading.Thread(target= mergeSortReal, args = (left,))   
        t2 = threading.Thread(target= mergeSortReal, args = (right,))      #multithread sort
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
        while (i1 < len(left) and i2 < len(right)):
            if (left[i1] <= right[i2]):
                sorting[i3]=left[i1]
                i1=i1+1
            else:
                sorting[i3]=right[i2]
                i2=i2+1
            i3=i3+1
        while (i1 < len(left)):
            sorting[i3]=left[i1]
            i1=i1+1
            i3=i3+1

        while (i2 < len(right)):
            sorting[i3]=right[i2]
            i2=i2+1
            i3=i3+1
    print(sorting , (threading.current_thread().name))
    return sorting
        
            

def testRead(numbersNotSorted):

    lista = []
    for i in range (0, len(numbersNotSorted)):
        lista.append(numbersNotSorted[i])
    print(lista)    
    
def leerArchivo():
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
    
    
    
    print (mergeSort())
    
main()