import sys
import re
from collections import deque
#from memory_profiler import profile # type: ignore <-- used when running memory profiler to get space complexity graph

#Run memory profiler in terminal to get space complexity graph (must uncomment related code & comment main):
  # pip install memory_profiler
  # mprof run binary_search.py
  # mprof plot

#compile and run command: python3 binary_search.py

#@profile(precision=4) <-- used when running memory profiler to get space complexity graph
def binary_search(array, target):
  #ITERATIVE BINARY SEARCH <-- use this for testing & main
  if(len(array) == 0):
    #edge case -> array contains no elements
    return -1
  
  start = 0
  end = len(array) - 1
  
  #iteratively find target
  while(start <= end):
  
    #find mid - avoid integer overflow
    mid = start + (end - start) // 2

    if(array[mid] == target):
      #target found
      return mid
    elif (array[mid] < target):
      #target greater than mid -> search right half
      start = mid + 1
    elif (array[mid] > target):
      #target less than mid -> search left half
      end = mid - 1
    
  return -1

#@profile(precision=4) <-- used when running memory profiler to get space complexity graph
def binary_search_recursive(array, start, end, target):
  #function is used to test space complexity ONLY
  #RECURSIVE BINARY SEARCH - implemented this first but optimized to iterative
  if(len(array) == 0):
    #edge case -> array contains no elements
    return -1

  if(end < start):
    #target not found
    return -1
  
  #find mid - avoid inter
  mid = start + (end - start) // 2

  if(array[mid] == target):
    #target found
    return mid
  elif (array[mid] < target):
    #target greater than mid -> search right half
    return binary_search_recursive(array, mid + 1, end, target)
  elif (array[mid] > target):
    #target less than mid -> search left half
    return binary_search_recursive(array, start, mid - 1, target)
  
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
      
      index = binary_search(nums, target)
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
  #array = list(range(1,101)) <--for running memory profiler
  #binary_search(array, 0) <--for running memory profiler
  #binary_search_recursive(array, 0) <--for running memory profiler

  main()
  
