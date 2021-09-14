### File: Anagrams.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### 
### 
###
### Modification Log:
### 
###

# myfun is a lambda function, dimension is the dimension of the board.
def numberOfGrains(myfun,dimension):
  #YOUR CODE GOES HERE
  
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

  print('Total Grains:', totGrains)
  return totGrains

# Count the time it takes to count all of the grains
def timeToCount(myfun,dimension):
  #YOUR CODE GOES HERE
  # One second per grain
  totalGrains = numberOfGrains(myfun, dimension)
  seconds = totalGrains
  minutes = 0
  hours = 0
  days = 0
  years = 0
  done = False

  while not done:
    if seconds >= 60:
      minutes += 1
      seconds = seconds - 60
    
    if minutes >= 60:
      hours += 1
      minutes = minutes - 60

    if hours >= 24:
      days += 1
      hours = hours - 24
    
    if days >= 365:
      years += 1
      days = days - 365

    if seconds < 60 and minutes < 60 and hours < 24 and days < 365:
      done = True

  #print(totalSeconds, totalMinutes, totalHours, totalDays, totalYears)
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
  #if numberOfGrains(lambda k:k*k,20)==21413400: 
   # print ("Test 3 passed. Number of grains with square function")
  #else:
   # print ("Test 3 failed. Number of grains with square function")


def testTime():
  if timeToCount(lambda k:k,10)==[10,24,1,0,0]:
    print ("Test 3 passed.  Time to count with identity function.")
  else:
    print ("Test 3 failed.  Time to count with identity function.")
  if timeToCount(lambda k:k*k,10)==[10,59,21,3,0]:
    print ("Test 4 passed.  Time to count with square function.")
  else:
    print ("Test 4 failed.  Time to count with square function.")


print('\ntestCount:\n')
testCount()
print('\ntestTime:\n')
testTime()
