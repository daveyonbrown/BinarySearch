import sys
import re
from collections import deque

#compile and run command: python3 binary_search.py

def binary_search(array, start, end, target):

  if(end < start):
    #target not found
    return -1
  
  #find mid
  mid = (end + start) // 2

  if(array[mid] == target):
    #target found
    return mid
  elif (array[mid] < target):
    #target greater than mid -> search right half
    return binary_search(array, mid + 1, end, target)
  elif (array[mid] > target):
    #target less than mid -> search left half
    return binary_search(array, start, mid - 1, target)
  
  return -1

def main():
  go = True
  while(go):
    menu = "--Menu--\n1) Find target from sorted list.\n2) Exit."
    print(menu)
    try:
      option = int(input("Enter the option number (1 or 2): "))
    except ValueError:
      print("Given option was not an integer! Please try again.")
      continue

    if(option == 1):

      #get sorted list from user
      isNums = False
      while(not isNums):
        try:
          nums = list(map(int, input("Enter sorted list of numbers separated by spaces:\n").split()))
          isNums = True
        except ValueError:
          print("Given list of numbers were not integers! Please re-enter list")
          isNums = False

      #get target from user
      isTarget = False
      while(not isTarget):
        try:
          target = int(input("Enter the target value: "))
          isTarget = True
        except ValueError:
          print("Given target was not an integer! Please re-enter your target")
          isTarget = False
      
      index = binary_search(nums, 0, len(nums) - 1, target)
      if(index == -1):
        print("Target was not found!")
      else:
        print("Target found at index: "+str(index))
    elif (option == 2):
      print("Goodbye!")
      go = False
    else:
      print("Given option did not correspond to a menu number! Please try again.")


if __name__ == "__main__":
  main()
  
