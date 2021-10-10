### File: BruteForceStringMatching.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### 
###
### 
### Modification Log:
### 
###


### ---------------------------------------------------
###     PART A BRUTE FORCE STRING MATCHING
### ---------------------------------------------------

''' 
BruteForceStringMatch(T [0..n − 1], P [0..m − 1] ) //Implements brute-force string matching
//Input: An array T [0..n − 1] of n characters representing a text and 
// an array P [0..m − 1] of m characters representing a pattern 
//Output: The index of the first character in the text that starts a
// matching substring or −1 if the search is unsuccessful 
for i ← 0 to n − m do
    j←0
    while j < m and P [j ] = T [i + j ] do
        j←j+1 
    if j =m:
        return i
return −1'''

def testCaseA(testNumber,longText,searchString,expectedResult):
  actualResult = yourFunctionName(longText,searchString)
  if actualResult == expectedResult: 
      print ("Test",testNumber,"passed.")
  else: 
      print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testA():
  testCaseA(1,"Oh I wish I were an aardvark.","were",12) 
  testCaseA(2,"Oh I wish I were an aardvark.","join",-1) 
  testCaseA(3,"She sells sea shells by the seashore.","seashore",28)
