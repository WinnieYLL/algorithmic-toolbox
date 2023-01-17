from sys import stdin
from array import *
import copy

def maximum_gold(capacity, weights):
  # print("======= maximum_gold ======")
  value = []
  n = len(weights)
  rows, cols = (capacity+1, n)
  y = [[1 for i in range(cols)] for j in range(rows)]
  
  for w in range (0,capacity+1): 
    besti = -1
    # print("=== w = " +str(w) + "===")
    value.append(0)
    # print(value)
    # print(y)    
    for i in range (n):
      # print("== i = " +str(i) + "==")
      
      if (weights[i] <= w and y[w-weights[i]][i] == 1):
        # print("   weights[i] = " + str(weights[i]))
        val = value[w-weights[i]] + weights[i]
        
        if(val > value[w]):
          value[w] = val
          besti = i
          # print("potential update, besti = " + str(besti))

    if (besti != -1):
      # print("final besti = " + str(besti) + "; value[w] = " + str(value[w]) + "; weights[besti] = " + str(weights[besti]))
      # print(y)
      # print("Update y; y[w] = " + str(y[w]) + "; y[w-weights[besti]] = " + str(y[w-weights[besti]]))
      y[w] = copy.deepcopy(y[w-weights[besti]])
      y[w][besti] = 0
      # print(y)
      
    if (value[w] == 0):
      value[w] = copy.deepcopy(value[w-1])
      y[w] = y[w-1]
  # print(value)
  # print(y) 
  return value[capacity], y
  
def partition3(values):
  n = len(values)
  
  total_sum = sum(values)
  if (total_sum % 3 != 0):
    return 0
  value1, y1 = maximum_gold(total_sum//3, values)  
  # print(value1)
  if (value1 != total_sum//3):
    return 0
    
  for i in range(len(y1[-1])):
    if (y1[-1][i] == 0):
      values[i] = 0
  # print(values)
  value2, y2 = maximum_gold(total_sum//3, values) 
  
  if (value2 != total_sum//3):
    return 0
  return 1


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
