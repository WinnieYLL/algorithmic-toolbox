def edit_distance(first_string, second_string):
  n = len(first_string) 
  m = len(second_string) #The string that we want 
  
  #first = [x for x in first_string]
  #second = [x for x in second_string]
  #print(first)
  #print(second)

  D = [[0 for i in range(m+1)] for j in range(n+1)]
  for i in range (m+1):
    D[0][i] = i
  for j in range (n+1):
    D[j][0] = j

  for j in range (1, n+1):
    for i in range (1, m+1):
      #insertion
      insertion = D[j][i-1] + 1
      #deletion
      deletion = D[j-1][i] + 1
      #match
      match = D[j-1][i-1] 
      #mismatch
      mismatch = D[j-1][i-1] + 1
      if (first_string[j-1] == second_string[i-1]): # should it be i-1???
        D[j][i] = min(insertion, deletion, match)
      else:
        D[j][i] = min(insertion, deletion, mismatch)
  
  return D[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))