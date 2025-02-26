import sys
import re
from collections import deque

#compile and run command: python3 binary_match.py test1.txt


def binary_search(array):
  return 0

def print(matches):
  #write to output file
  with open('output.txt', 'w') as file:
    #print stable matching
    file.write("Binary Search\n")



def parse(file):

  #get first line
  line = file.readline()

  #parse n
  n = 0
  n_pattern = r"\s*n\s*=\s*(\d+)"
  isN = re.match(n_pattern, line)
  if isN:
    n = int(isN.group(1)) #guarenteed to be int
  else:
    print("First line is not n declaration! Parsing failed.")
    return -1

  return 0


def main():
  filePath = ""
  if (len(sys.argv) > 1):
    filePath = sys.argv[1]
  else:
    print("Input file path was not passed to main!")
  
  try:
    with open(filePath, "r") as file:
      parse(file)
  except FileNotFoundError:
    print("File path did not open file!")


if __name__ == "__main__":
  main()
  
