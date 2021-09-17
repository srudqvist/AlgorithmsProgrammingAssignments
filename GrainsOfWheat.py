### File: GrainsOfWheat.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### 
### This program finds the total grains on a board of size n*n 
### And the time it takes to count all of the grains.
### 
### Modification Log:
### 
###

# myfun is a lambda function, dimension is the dimension of the board.
def numberOfGrains(myfun,dimension):
  #YOUR CODE GOES HERE
  try:
    totSquares = dimension * dimension
    totGrains = 0
    # Loop through as many times as there are squares. 
    # Starting from the last square, add the number of grains on that square
    # to totGrains and then take away that square.
    for i in range(0,totSquares):
      grainsOnSquare = myfun(totSquares)
      #print('Current Square:',totSquares)
      #print('Grains on current square', grainsOnSquare)
      totGrains = totGrains + grainsOnSquare
      totSquares = totSquares - 1

    #print('Total Grains:', totGrains)
    return totGrains
  except:
    print('Please check the input in the test function')


# Count the time it takes to count all of the grains
def timeToCount(myfun,dimension):
  # Time constants
  SECONDS_IN_YEAR = 31536000
  SECONDS_IN_DAY = 86400
  SECONDS_IN_HOUR = 3600
  SECONDS_IN_MINUTE = 60
  # Set seconds equal to the total number of grains, use divmod to get
  # the years, days, hours, minutes, seconds
  seconds = numberOfGrains(myfun, dimension)
  years = divmod(seconds, SECONDS_IN_YEAR)
  days = divmod(years[1], SECONDS_IN_DAY)
  hours = divmod(days[1], SECONDS_IN_HOUR)
  minutes = divmod(hours[1], SECONDS_IN_MINUTE)
  seconds = minutes[1]
  years = years[0]
  days = days[0]
  hours = hours[0]
  minutes = minutes[0]
  #print("Time:", "Seconds:", seconds, "Minutes:", minutes, "Hours:", hours, "Days:", days, "Years:", years)
  return [seconds,minutes,hours,days,years]


def testCount():
  if numberOfGrains(lambda k:k,10)==5050:
    print ("Test 1 passed. Number of grains with identity function")
  else:
    print ("Test 1 failed. Number of grains with identity function")

  if numberOfGrains(lambda k:k*k,2)==30: 
    print ("Test 2 passed. Number of grains with square function")
  else:
    print ("Test 2 failed. Number of grains with square function")

  if numberOfGrains(lambda k:k**k,2)==288: 
    print ("Test 5 passed. Number of grains with exponential function")
  else:
    print ("Test 5 failed. Number of grains with exponential function")

  if numberOfGrains(lambda k:k-k-1,8)== - 64: 
    print ("Test 6 passed. Number of grains with linear function, removing one")
  else:
    print ("Test 6 failed. Number of grains with linear function, removing one")

  if numberOfGrains(lambda k:2*k - 1,8)== 4096: 
    print ("Test 7 passed. Count answer part b")
  else:
    print ("Test 7 failed. Count answer part b")


def testTime():
  if timeToCount(lambda k:k,10)==[10,24,1,0,0]:
    print ("Test 3 passed.  Time to count with identity function.")
  else:
    print ("Test 3 failed.  Time to count with identity function.")

  if timeToCount(lambda k:k*k,10)==[10,59,21,3,0]:
    print ("Test 4 passed.  Time to count with square function.")
  else:
    print ("Test 4 failed.  Time to count with square function.")

  if timeToCount(lambda k:k * 2, 8)==[20,9,1,0,0]:
    print ("Test 8 passed.  Time to count with linear function. Multiply by 2")
  else:
    print ("Test 8 failed.  Time to count with linear function. Multiply by 2")

  if timeToCount(lambda k:k + 2, 8)==[48,36,0,0,0]:
    print ("Test 9 passed.  Time to count with linear function. Add 2.")
  else:
    print ("Test 9 failed.  Time to count with linear function. Add 2.")
  
  if timeToCount(lambda k:k**k, 3)==[37,48,7,308,12]:
    print ("Test 9 passed.  Time to count with exponential function.")
  else:
    print ("Test 9 failed.  Time to count with exponential function.")

  if timeToCount(lambda k:2**(k-1) ,8)== [15,0,7,26,584942417355]: 
    print ("Test 11 passed. answer part a")
  else:
    print ("Test 11 failed. answer part a")

  if timeToCount(lambda k:2*k - 1,8)== [16,8,1,0,0]: 
    print ("Test 12 passed. Count answer part b")
  else:
    print ("Test 12 failed. Count answer part b")

def underOneDay():
  for x in range(0, 25):
    time = timeToCount(lambda k:k,x)
    if time[3] < 1 and time[4] < 1:
      print("Dimension:",x)
      print("Time:",time)
    else:
      print("OVERTIME")
      print("Dimension:",x)
      print("Overtime time:", time)
      
    

print('\ntestCount:\n')
testCount()
print('\ntestTime:\n')
testTime()
print('\nunderOneDay:\n')
underOneDay()



# # Count the time it takes to count all of the grains
# def timeToCount2(myfun,dimension):
#   #YOUR CODE GOES HERE
#   # One second per grain
#   totalGrains = numberOfGrains(myfun, dimension)
#   seconds = totalGrains
#   minutes = 0
#   hours = 0
#   days = 0
#   years = 0
#   done = False

#   while not done:
#     if seconds >= 60:
#       minutes += 1
#       seconds = seconds - 60
    
#     if minutes >= 60:
#       hours += 1
#       minutes = minutes - 60

#     if hours >= 24:
#       days += 1
#       hours = hours - 24
    
#     if days >= 365:
#       years += 1
#       days = days - 365

#     if seconds < 60 and minutes < 60 and hours < 24 and days < 365:
#       done = True

#   #print(totalSeconds, totalMinutes, totalHours, totalDays, totalYears)
#   return [seconds,minutes,hours,days,years]
