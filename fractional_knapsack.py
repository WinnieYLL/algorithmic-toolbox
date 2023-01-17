from sys import stdin
import numpy as np
import copy as cp
import decimal as de


def optimal_value(capacity, weights, values):
    totalValue = 0.
    new_values = cp.deepcopy(values)
    #print("values before new_values:" + str(values))
    n = len(values)
    for i in range (n):
        new_values[i] = values[i]/weights[i]

    #print("values after new_values:" + str(values))
    a = np.array([new_values, weights, values])
    #print("a before sort: " + str(a))
    sorted_inds = np.argsort(a[0,:])
    
    #print("sorted_inds: " + str(sorted_inds))

    b = a[:, sorted_inds]
    #print("b (sorted a: " + str(b))
  
    #print(b)
  
    tmp = capacity
    for j in range (n-1, -1, -1):
      if(tmp >= weights[sorted_inds[j]]):
        totalValue = totalValue + round(new_values[sorted_inds[j]]*weights[sorted_inds[j]], 3)
        #print(values[sorted_inds[j]])
        #print(totalValue)
        tmp = tmp - weights[sorted_inds[j]]
      elif(tmp < weights[sorted_inds[j]]):
        totalValue = totalValue + round(new_values[sorted_inds[j]]*tmp, 3)
        return totalValue
        #print(totalValue)
    return totalValue 


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))