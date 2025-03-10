# Project: Binary Search
Members: Daveyon Brown, Mary Hanson

Date: April 22, 2025

# Project Description

Binary search is a divide and conquer algorithm, used to find elements in a sorted list.​

How it works​:
- Starts with the middle element of a sorted array ​
- If it’s the targeted value, element will be returned ​
- If the target is smaller, the search will be repeated in the left half​
- If the target is larger, the search will be repeated in the right half​
- Will continue until element is found or the range is empty


# Compile & Run Command

## For unit tests:
command: python3 unit_tests.py 

## For binary search:
command: python3 binary_search.py

# Input and Output for binary_search.py

## Input:
When running binary_search.py directly, the user inputs a sorted list of integers seperated by a space and a target value when prompted in the command line. The program will repeatedly ask the user for valid inputs, if the given numbers are not integers. The execution will continue based on the user's choice to continue the program or exit. This way the user can continually test the program without the need to recompile.

Menu Options:
1) Find target from sorted list.
2) Exit.

## Output:

The program outputs directly to the command line. If the target is found, it will output the corresponding index. If the target is not found, the program outputs a string: "The target was not found."

# Output for unittests.py:

The unit tests will execute and return OK if all passed. Otherwise, if the tests do not pass, there is failure details.