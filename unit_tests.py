import unittest
import time
from binary_search import binary_search

#python3 unit_tests.py 

class BinSearchTests(unittest.TestCase):
  #find the index of the target if it exists
  def test_small_true(self):
    #test range 1, index exists
    array = [1]
    target = 1
    expectedIndex = 0
    actualIndex = binary_search(array, target)
    self.assertEqual(expectedIndex, actualIndex)

  def test_small_false(self):
    #test range 1, index does not exist
    array = [1]
    target = 2
    expectedIndex = -1
    actualIndex = binary_search(array, target)
    self.assertEqual(expectedIndex, actualIndex)

  def test_medium_true(self):
    #test range [1,100] inclusive, index exists
    array = list(range(1,101))
    target = 34
    expectedIndex = 33
    actualIndex = binary_search(array, target)
    self.assertEqual(expectedIndex, actualIndex)

  def test_medium_false(self):
    #test range [1,100] inclusive, index does not exist
    array = list(range(1,101))
    target = 199
    expectedIndex = -1
    actualIndex = binary_search(array, target)
    self.assertEqual(expectedIndex, actualIndex)

  def test_large_true(self):
    #test range [1,1000] inclusive, index exists
    array = list(range(1,1001))
    target = 756
    expectedIndex = 755
    actualIndex = binary_search(array, target)
    self.assertEqual(expectedIndex, actualIndex)

  def test_large_false(self):
    #test range [1,1000] inclusive, index does not exist
    array = list(range(1,1001))
    target = 1008
    expectedIndex = -1
    actualIndex = binary_search(array, target)
    self.assertEqual(expectedIndex, actualIndex)

  def test_range_worst_case(self):
    #gets time for inputs from 1, 200
    #also tests all outputs for every input size given
    times = []
    for end in range(1, 200):
      start_time = time.perf_counter()
      array = list(range(1,end))
      target = 0
      expectedIndex = -1
      actualIndex = binary_search(array, target)
      end_time = time.perf_counter()
      times.append(end_time - start_time)
      self.assertEqual(expectedIndex, actualIndex)
    #print(times) <-- used for matplotlib graph of time complexity

if __name__ == '__main__':
    unittest.main()