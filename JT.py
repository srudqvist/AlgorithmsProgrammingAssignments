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

### ---------------------------------------------------
###     PART A, CLASSES AND METHODS
### ---------------------------------------------------

# The Element class takes the value and direction of an Element.
class Element:
    def __init__(self, value, direction):
        self.value = value
        self.direction = direction
    
    # Method to switch the direction of the "arrow"
    # The direction indicates wether the arrow is pointing left or right
    # Let 1 = right and -1 = left
    
    def changeDirection(self):
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "right"
    
    def getDirection(self):
        return self.direction

    def getValue(self):
        return self.value



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
            if pos == 0 and element.direction == "left":
                raise IndexError

            if element.direction == "left":
                elementLeft = self.ElementArray[pos - 1]
                if element.value > elementLeft.value:
                    return True
                elif element.value < elementLeft.value:
                    return False
            elif element.direction == "right":
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

        if direction == "right":
            list[largestMobile], list[largestMobile + 1] = list[largestMobile + 1], list[largestMobile]
            return list

        elif direction == "left":
            for i in range(0, len(list)):
               pass
            list[largestMobile - 1], list[largestMobile] = list[largestMobile], list[largestMobile - 1]

            return list
    
    def printElements(self):
        valueList = []
        directionList = []
        for i in range(0,len(self.ElementArray)):
            valueList.append(self.ElementArray[i].value)
            directionList.append(self.ElementArray[i].direction)
        return valueList, directionList


### -------------------------------------------- ###
###     PART B, IMPLEMENT JOHNSON TROTTER        ###
### -------------------------------------------- ###

def permute(n):
    print("\nPermute(",n,") called")
    elementList = []
    allPermutations = []
    for i in range(1,n + 1):
        theElement = Element(i, "left")
        elementList.append(theElement)

    permutationList = Permutation(elementList)
    print(permutationList.printElements()[0])
    allPermutations.append(permutationList.printElements()[0])

    while permutationList.isAnyMobile():
        largestMobile = permutationList.largestMobile()
        permValueList = permutationList.printElements()[0]

        newList = permutationList.nextPermutation()
        for i in range(0,len(elementList)):
            if permValueList[i] > permValueList[largestMobile]:
                elementList[i].changeDirection()
            else:
                pass
        allPermutations.append(permutationList.printElements()[0])

    print(allPermutations)

def permute2(n):
    print("\nPermute(",n,") called")
    elementList = []
    for i in range(1,n + 1):
        theElement = Element(i, "left")
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
            else:
                pass
        print(permutationList.printElements()[0])

### -------------------------------------------- ###
###             PART C, TIME STUDIES             ###
### -------------------------------------------- ###

def permuteTime(n):
    startTime = time.time()
    permute(n)
    endTime = time.time()
    print("Printing the permutations of", n, "elements took", endTime - startTime, "seconds.")

def permuteTime2(n):
    startTime = time.time()
    permute2(n)
    endTime = time.time()
    print("Printing the permutations of", n, "elements took", endTime - startTime, "seconds.")

permuteTime(3)
#permuteTime2(3)



### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###
###                             TESTS PART A                                          ###
### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###

# -------------------------------- #
# Test code for the Element class  #
# -------------------------------- #
def ElementClassTests():
    myElement = Element(1, "right")
    myElement2 = Element(3, "left")
    myElement3 = Element(4, "right")
    myElement4 = Element(7, "left")
    myElement5 = Element(2, "right")

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

#ElementClassTests()

# ------------------------------------ #
# Test code for the Permutation class  #
# ------------------------------------ #
def PermutationClassTests():
    myElement = Element(1, "right")
    myElement2 = Element(3, "left")
    myElement3 = Element(4, "right")
    myElement4 = Element(7, "left")
    myElement5 = Element(2, "right")
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

    def anyMobileTests():
        print("\nTests 2 C):")
        if myPerm.isAnyMobile():
            print("There is a mobile element in the list.")
        else:
            print("There are no mobile elements in the list.")

    def largestMobileTests():
        print("\nTests 2 D):")
        if myPerm.largestMobile() == -1:
            print("There are no mobile elements in the list.")
        else:
            print("The largest mobile element is found at position", myPerm.largestMobile())

    # Only works until the largest element is moved to an extremity
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
#PermutationClassTests()     # Put a comment in front to disable all tests
