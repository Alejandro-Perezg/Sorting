# "Alejandro Perez Gonzalez"
# "A01746643"
# """Taking the numbers of numbers.txt given to me:
# 123,983,2,5,76,4,-12,43,-5,53,71,-34,""

from math import log10

def intro():
    print("ALGORITMOS COMPUTACIONALES")
    print("ALEJANDRO PÉREZ GONZÁLEZ A01746643")

def get_digit(num, base, pos):
  return (num // base ** pos) % base

def prefix_sum(arr):
  for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]
  return arr

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)

  for pos in range(passes):
    count = [0] * base

    for i in l:
      digit = get_digit(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(l):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    l = list(output)
  return output


def createArr(file):
    for line in file:
        numbers = line.split(",")
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
    return numbers


def main():

    file = open("numbers.txt","r")
    numbers = createArr(file)
    print("Input: "+str((numbers)))
    print("Output: "+str(radixsort(numbers,10)))
    file.close()

intro()
main()