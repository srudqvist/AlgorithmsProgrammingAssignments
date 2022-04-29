### File: JohnsonTrotter.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### 
###
### 
### Modification Log:
### 
###

import time

### --------------------------------------------------- ###
###     PART A, CLASSES AND METHODS                     ###
### --------------------------------------------------- ###

# The Element class takes the value and direction of an Element.
class Element:
    def __init__(self, value, direction):
        self.value = value
        self.direction = direction
    
    # Method to switch the direction of the "arrow"
    # The direction indicates wether the arrow is pointing left or right
    # Let 1 = right and -1 = left
    def changeDirection(self):
        self.direction = self.direction * -1


# The Permutation class takes an array of Elements.
class Permutation:
    def __init__(self, ElementArray):
        self.ElementArray = ElementArray

    # Element is mobile if it is greater than the element it is pointing to
 
    # Use this on an array of elements, give it the position of an element and it will 
    # return true if the element is mobile and false if it is not
    def isMobile(self, pos):

        try:
            element = self.ElementArray[pos]
            # Handles the case where elementLeft has pos -1 which is last in the list
            if pos == 0 and element.direction == -1:
                raise IndexError

            if element.direction == -1:
                elementLeft = self.ElementArray[pos - 1]
                if element.value > elementLeft.value:
                    return True
                elif element.value < elementLeft.value:
                    return False
            elif element.direction == 1:
                elementRight = self.ElementArray[pos + 1]
                if element.value > elementRight.value:
                    return True
                elif element.value < elementRight.value:
                    return False

        # Handles cases where the element is not pointing towards any other element, and therefore is not mobile
        except IndexError:
            return False
                   
    # Use this on an array of elements to find out if there are any mobile elements
    def isAnyMobile(self):
        list = self.ElementArray
        for i in range(0,len(self.ElementArray)):
            if Permutation(list).isMobile(i):
                return True
        return False
            
    # Use this on an array of elements to find the position of the largest mobile element in the list
    def largestMobile(self):
        list = self.ElementArray
        mobileValue = []
        if Permutation(list).isAnyMobile():
            for i in range(0,len(list)):
                if Permutation(list).isMobile(i):
                    position = i
                    mobileValue.append(list[i].value)
            
            largest = max(mobileValue) 
            for i in range(0, len(list)):
                if list[i].value == largest:
                    return i
        else:
            return -1
                
    def nextPermutation(self):
        list = self.ElementArray
        largestMobile = Permutation(list).largestMobile()
        direction = list[largestMobile].direction
        origList = []
        if direction == 1:
            list[largestMobile], list[largestMobile + 1] = list[largestMobile + 1], list[largestMobile]
            return list
        elif direction == -1:
            list[largestMobile - 1], list[largestMobile] = list[largestMobile], list[largestMobile - 1]
            return list
    
    def printElements(self):
        valueList = []
        directionList = []
        for i in range(0,len(self.ElementArray)):
            valueList.append(self.ElementArray[i].value)
            directionList.append(self.ElementArray[i].direction)
            #print(self.ElementArray[i].value, self.ElementArray[i].direction)
        return valueList, directionList


### -------------------------------------------- ###
###     PART B, IMPLEMENT JOHNSON TROTTER        ###
### -------------------------------------------- ###

def permute(n):
    elementList = []
    allPermutations = []
    for i in range(1,n + 1):
        theElement = Element(i, -1)
        elementList.append(theElement)

    # initialized permutation list, this is the first one
    permutationList = Permutation(elementList)
    allPermutations.append(permutationList.printElements()[0])

    while permutationList.isAnyMobile():
        largestMobile = permutationList.largestMobile()
        permValueList = permutationList.printElements()[0]
        newList = permutationList.nextPermutation()
        for i in range(0,len(elementList)):
            if permValueList[i] > permValueList[largestMobile]:
                elementList[i].changeDirection()

        allPermutations.append(permutationList.printElements()[0])


    print(allPermutations)

def permute2(n):
    print("\nPermute(",n,") called")
    elementList = []
    for i in range(1,n + 1):
        theElement = Element(i, -1)
        elementList.append(theElement)

    # initialized permutation list, this is the first one
    permutationList = Permutation(elementList)
    print(permutationList.printElements()[0])

    while permutationList.isAnyMobile():
        largestMobile = permutationList.largestMobile()
        permValueList = permutationList.printElements()[0]
        newList = permutationList.nextPermutation()
        for i in range(0,len(elementList)):
            if permValueList[i] > permValueList[largestMobile]:
                elementList[i].changeDirection()

        print(permutationList.printElements()[0])

### -------------------------------------------- ###
###             PART C, TIME STUDIES             ###
### -------------------------------------------- ###

def permuteTime(n):
    startTime = time.time()
    permute(n)
    endTime = time.time()
    totTime = endTime - startTime
    print("Printing the permutations of", n, "elements took", totTime, "seconds.")
    return totTime

def permuteTime2(n):
    startTime = time.time()
    permute2(n)
    endTime = time.time()
    totTime = endTime - startTime
    print("Printing the permutations of", n, "elements took", totTime, "seconds.")
    return totTime





### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###
###                             TESTS PART A                                          ###
### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###

# -------------------------------- #
# Test code for the Element class  #
# -------------------------------- #


def ElementClassTests():
    print("\n###---------------------------------------------------###")
    print("###                ELEMENT TESTS START                ###")
    print("###---------------------------------------------------###")
    print("All tests use the same list unless stated otherwise.\n")
    myElement = Element(1, 1)
    myElement2 = Element(3, -1)
    myElement3 = Element(4, 1)
    myElement4 = Element(7, -1)
    myElement5 = Element(2, 1)

    print("\nBefore changing any directions")
    print("Value1:", myElement.value, "Direction1:", myElement.direction)
    print("Value2:", myElement2.value, "Direction2:", myElement2.direction)
    print("Value3:", myElement3.value, "Direction3:", myElement3.direction)
    print("Value4:", myElement4.value, "Direction4:", myElement4.direction)
    print("Value5:", myElement5.value, "Direction5:", myElement5.direction)
    myElement.changeDirection()
    myElement2.changeDirection()
    myElement3.changeDirection()
    myElement4.changeDirection()
    myElement5.changeDirection()
    
    print("\nAfter changing the direction on all elements")
    print("Value1:", myElement.value, "Direction1:", myElement.direction)
    print("Value2:", myElement2.value, "Direction2:", myElement2.direction)
    print("Value3:", myElement3.value, "Direction3:", myElement3.direction)
    print("Value4:", myElement4.value, "Direction4:", myElement4.direction)
    print("Value5:", myElement5.value, "Direction5:", myElement5.direction)
    myElement2.changeDirection()
    myElement3.changeDirection()
    print("\nAfter changing the direction again on two elements")
    print("Value1:", myElement.value, "Direction1:", myElement.direction)
    print("Value2:", myElement2.value, "Direction2:", myElement2.direction)
    print("Value3:", myElement3.value, "Direction3:", myElement3.direction)
    print("Value4:", myElement4.value, "Direction4:", myElement4.direction)
    print("Value5:", myElement5.value, "Direction5:", myElement5.direction)
    print("\n###---------------------------------------------------###")
    print("###                 ELEMENT TESTS END                 ###")
    print("###---------------------------------------------------###\n")
   

# ------------------------------------ #
# Test code for the Permutation class  #
# ------------------------------------ #
def PermutationClassTests():
    print("\n###---------------------------------------------------###")
    print("###             PERMUTATION TESTS START               ###")
    print("###---------------------------------------------------###")
    print("All tests use the same list unless stated otherwise.\n")
    myElement = Element(1, 1)
    myElement2 = Element(3, -1)
    myElement3 = Element(4, 1)
    myElement4 = Element(7, -1)
    myElement5 = Element(2, 1)
    elementList = [myElement, myElement2, myElement3, myElement4, myElement5]
    original = [myElement, myElement2, myElement3, myElement4, myElement5]
    myPerm = Permutation(elementList)
    # Tests to make sure the list is initialized properly
    # 2 a)
    def initTests():
        print("\nTests 2 A):")
        print("The values of the Elements in the list:")
        print(myPerm.printElements()[0])
        print("\nThe directions of the Elements in the list:")
        print(myPerm.printElements()[1])

    # Tests to make sure the isMobile function works properly
    # 2 b)
    def isMobileTests():
        print("\nTests 2 B):")
        for i in range(0, len(elementList)):
            if myPerm.isMobile(i):
                print("The element at index", i, "is mobile.")
            else:
                print("The element at index", i, "is not mobile.")

    # Tests to make sure the isAnyMobile function works properly
    # 2 c)
    def anyMobileTests():
        print("\nTests 2 C):")
        if myPerm.isAnyMobile():
            print("There is a mobile element in the list.")
        else:
            print("There are no mobile elements in the list.")

    # Tests to make sure the largestMobile function works properly
    # 2 d)
    def largestMobileTests():
        print("\nTests 2 D):")
        if myPerm.largestMobile() == -1:
            print("There are no mobile elements in the list.")
        else:
            print("The largest mobile element is found at position", myPerm.largestMobile())

    # Tests to make sure the nextPermutation function works properly
    # 2 e)
    # This test only works until the largest mobile element is moved to an extremety
    # The Johnson Trotter algorithm adresses this issue by changing direction on elements
    def nextPermutationTests():
        print("\nTests 2 E):")
        originalList = []
        returnedList = myPerm.nextPermutation()
        valueList = []
        for i in range(0, len(returnedList)):
            originalList.append(original[i].value)
            valueList.append(returnedList[i].value)
        
        print("Original List:   ", originalList)
        print("Next Permutation:",valueList)   

        valueList = []  
        returnedList = myPerm.nextPermutation()
        for i in range(0, len(returnedList)):
            valueList.append(returnedList[i].value)   
        print("Next Permutation:",valueList)    

        valueList = []  
        returnedList = myPerm.nextPermutation()
        for i in range(0, len(returnedList)):
            valueList.append(returnedList[i].value)   
        print("Next Permutation:",valueList)     
           
        
    initTests()
    isMobileTests()
    anyMobileTests()
    largestMobileTests()
    nextPermutationTests()
    print("\n###---------------------------------------------------###")
    print("###                      TESTS END                    ###")
    print("###---------------------------------------------------###\n")

   

### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###
###                             TESTS PART B                                          ###
### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###

# print statements added for readability in the test results
def testPermute():
    permute(1)
    print()
    permute(2)
    print()
    permute(3)
    print()
    permute(4)
    print()
    permute(5)

def testPermute2():
    permute2(1)
    print()
    permute2(2)
    print()
    permute2(3)
    print()
    permute2(4)
    print()
    permute2(5)

### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###
###                             TESTS PART C                                          ###
### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###

def permuteTimeTest():
    try:
        totalTime1 = 0
        totalTime2 = 0
        totalTime3 = 0
        totalTime4 = 0
        totalTime5 = 0
        totalTime6 = 0
        testAll = False
        print("Since some time tests take a long time, choose...")
        #numElements = input("For what 'n' do you want to run a time test? (type 'all' to get n=6-10) ")
        testAll = True
        for i in range(6, 11):
            print("i:", i)
            if i == 6:
                totalTime1 = permuteTime(i)
            elif i == 7:
                totalTime2 = permuteTime(i)
            elif i == 8:
                totalTime3 = permuteTime(i)
            elif i == 9:
                totalTime4 = permuteTime(i)
            elif i == 10:
                totalTime5 = permuteTime(i)
        if testAll:
            # print("Total time for 6 elements:", totalTime1, "seconds")
            # print("Total time for 7 elements:", totalTime2, "seconds")
            # print("Total time for 8 elements:", totalTime3, "seconds")
            # print("Total time for 9 elements:", totalTime4, "seconds")
            # print("Total time for 10 elements:", totalTime5, "seconds")
            return totalTime1, totalTime2, totalTime3, totalTime4, totalTime5
    except:
        print("Invalid input.")
        print("Make sure the input is an int or a string containing the letter 'a'.")

def permuteTimeTest2():
    try:
        totalTime1 = 0
        totalTime2 = 0
        totalTime3 = 0
        totalTime4 = 0
        totalTime5 = 0
        totalTime6 = 0
        testAll = False
        print("Since some time tests take a long time, choose...")
        #numElements = input("For what 'n' do you want to run a time test? (type 'all' to get n=6-10) ")
        
        testAll = True
        for i in range(6, 11):
            print("i:", i)
            if i == 6:
                totalTime1 = permuteTime2(i)
            elif i == 7:
                totalTime2 = permuteTime2(i)
            elif i == 8:
                totalTime3 = permuteTime2(i)
            elif i == 9:
                totalTime4 = permuteTime2(i)
            elif i == 10:
                totalTime5 = permuteTime2(i)
        
        if testAll:
            # print("Total time for 6 elements:", totalTime1, "seconds")
            # print("Total time for 7 elements:", totalTime2, "seconds")
            # print("Total time for 8 elements:", totalTime3, "seconds")
            # print("Total time for 9 elements:", totalTime4, "seconds")
            # print("Total time for 10 elements:", totalTime5, "seconds")
            return totalTime1, totalTime2, totalTime3, totalTime4, totalTime5
    except:
        print("Invalid input.")
        print("Make sure the input is an int or a string containing the letter 'a'.")
        #permuteTimeTest2()

def compareTimes():
    withArray = 0
    noArray = 0
    # with array times
    startTime = time.time()
    for i in range(0,5):
        inArray = 0
        outArray = 0
        time1, time2, time3, time4, time5 = permuteTimeTest()
        time6, time7, time8, time9, time10 = permuteTimeTest2()

        print(time1, time2, time3, time4, time5)
        if time1 < time6:
            print("in array is faster 1")
            inArray += 1
        elif time6 < time1:
            print("no array is faster 1")
            outArray += 1
        
        if time2 < time7:
            print("in array is faster 2")
            inArray += 1
        elif time7 < time2:
            print("no array is faster 2")
            outArray += 1
        
        if time3 < time8:
            print("in array is faster 3")
            inArray += 1
        elif time8 < time3:
            print("no array is faster 3")
            outArray += 1
        
        if time4 < time9:
            print("in array is faster 4")
            inArray += 1
        elif time9 < time4:
            print("no array is faster 4")
            outArray += 1

        if time5 < time10:
            print("in array is faster 5")
            inArray += 1
        elif time10 < time5:
            print("no array is faster 5")
            outArray += 1
        
        if inArray > outArray:
            withArray += 1
        elif outArray > inArray:
            noArray += 1
    endTime = time.time()
    if withArray > noArray:
        print("With array was faster")
    elif noArray > withArray:
        print("Without array was faster")
    totTime = endTime - startTime
    minCount = 0
    # while totTime >= 60:
    #     minCount = minCount + 1
    #     totTime = totTime - 60
    print("With array times:")
    print("n = 6:", time1)
    print("n = 7:", time2)
    print("n = 8:", time3)
    print("n = 9:", time4)
    print("n = 10:", time5)
    print("\nWithout array times")
    print("n = 6:", time6)
    print("n = 7:", time7)
    print("n = 8:", time8)
    print("n = 9:", time9)
    print("n = 10:", time10)

    print("Total test time: ", totTime, "seconds" )



### ----------------------------- ###
###       CALL TEST FUNCTIONS     ###
### ----------------------------- ###

#ElementClassTests()
#PermutationClassTests()  
#testPermute()
testPermute2()
#permuteTimeTest()
#permuteTimeTest2()
#compareTimes()

# myElement6 = Element(13, -1)
# myElement7 = Element(12, -1)
# myElement8 = Element(11, -1)
# myElement9 = Element(10, -1)

# myElement10 = Element(4, -1)
# myElement11 = Element(14, 1)
# myElement12 = Element(5, -1)
# myElement13 = Element(13, -1)

# myPerm2 = Permutation([myElement6,myElement7, myElement8, myElement9])
# myPerm3 = Permutation([myElement10, myElement11, myElement12, myElement13])
# myPerm2.isAnyMobile()
# myPerm3.largestMobile()
# myPerm3.nextPermutation()
# #myPerm2.nextPermutation()
# #myPerm.nextPermutation()
