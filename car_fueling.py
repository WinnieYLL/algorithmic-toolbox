from sys import stdin

def min_refills(distance, tank, stops):
  print_info = False
  milestones = [0]
  for i in stops:
    milestones.append(i)
  milestones.append(distance)
  
  cur = tank
  if print_info:
    print("Tank capacity: " + str(tank))
  refill = 0
  
  n = len(milestones) - 1
  for i in range(n):
    fuel_needed = milestones[i + 1] - milestones[i]
    if print_info:
      print("i = " + str(i))
      print("  | cur = " + str(cur))
      print("  | this_stop = " + str(milestones[i]))
      print("  | next_stop = " + str(milestones[i+1]))
    if (fuel_needed > tank):
      if print_info:
        print("Not enough to go further!")
      return -1

    elif (fuel_needed > cur):
      if print_info:
        print("Refilling...")
      refill = refill + 1
      cur = tank - fuel_needed
      if print_info:
        print("Refilled " + str(refill) + " times")

    elif (fuel_needed <= cur):
      if print_info:
        print("Keep going.")
      cur = cur - fuel_needed
      if print_info:
        print("Fuel left: " + str(cur))
  
  return refill

    
if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))