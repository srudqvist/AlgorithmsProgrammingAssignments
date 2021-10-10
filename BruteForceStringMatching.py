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


def stringMatching(longText, searchString):
    try:
        if longText.isspace():
            print("Check the input, longText is only spaces.")
        if longText == "":
            print("No long string")
            return -1
        if searchString == "":
            print("No search string")
            return -1

        longTextLength = int(len(longText))
        searchStringLength = int(len(searchString))
        stringLength = longTextLength - searchStringLength

        # Loop search through the longText string looking for the characters in searchString.
        for posInText in range(0, stringLength):
            stringIndex = 0
            while stringIndex < searchStringLength and searchString[stringIndex] == longText[posInText + stringIndex]:
                stringIndex = stringIndex + 1
            
            if stringIndex == searchStringLength:
                return posInText
        return -1
        
    except:
        print("Check the input, this function only takes strings")
        print("Returned -1 since this test should fail since there is no string matching")
        return -1
            
### ---------------------------------------------------
###     PART B FIND THE LAST OCCURENCE
### ---------------------------------------------------

def findLast(longText, searchString):
    try:
        if longText.isspace():
            print("Check the input, longText is only spaces.")
        if longText == "":
            print("Check the input, there is no long string.")
            return -1
        if searchString == "":
            print("Check the input, there is no search string.")
            return -1

        longTextLength = int(len(longText))
        searchStringLength = int(len(searchString))
        stringLength = longTextLength - searchStringLength
        lastOccurrence = 0
        for posInText in range(0, stringLength):
            stringIndex = 0
            
            while stringIndex < searchStringLength and searchString[stringIndex] == longText[posInText + stringIndex]:
                stringIndex = stringIndex + 1
            
            # lastOccurence is the last occurrence that has been reached so far.
            if stringIndex == searchStringLength:
                lastOccurrence = posInText

            # When the entire string has been looped through, check if there has been an occurence
            # if not, return -1.
            if posInText == stringLength - 1:
                if lastOccurrence == 0:
                    return -1
                return lastOccurrence
                
        return -1
    except:
        print("Check the input, this function only takes strings")
        print("Returned -1 since this test should fail since there is no string matching")
        return -1


def testCaseA(testNumber,longText,searchString,expectedResult):
  actualResult = stringMatching(longText,searchString)
  if actualResult == expectedResult: 
      print ("Test",testNumber,"passed.")
  else: 
      print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testA():
  testCaseA(1,"Oh I wish I were an aardvark.","were",12) 
  testCaseA(2,"Oh I wish I were an aardvark.","join",-1) 
  testCaseA(3,"She sells sea shells by the seashore.","seashore",28)
  testCaseA(4, "Testing a STr1nG with uppercase and numbers", "string", -1)
  testCaseA(5, 123456, 23, -1)
  

def testCaseB(testNumber,longText,searchString,expectedResult):
  actualResult = findLast(longText,searchString)
  if actualResult == expectedResult: 
    print ("Test",testNumber,"passed.")
  else: 
    print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)


def testB():
  testCaseB(1,"Oh I wish I were an aardvark.","I w",10) 
  testCaseB(2,"Oh I wish I were an aardvark.","anteater",-1) 
  testCaseB(3,"She sells sea shells by the seashore.","sea",28)
  testCaseB(4, "So so So so So So soSo many occurrences here", "So", 20)
  testCaseB(5, "", "", -1)



testA()
testB()