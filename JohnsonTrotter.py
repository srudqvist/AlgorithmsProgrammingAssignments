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
        if self.direction == 1:
            self.direction = -1
            #print("Direction has been changed to", self.direction)
        elif self.direction == -1:
            self.direction = 1
            #print("Direction has been changed to", self.direction)
    
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
        #print(self.ElementArray)
        #print("isMobile Called")
        try:
            element = self.ElementArray[pos]
            #print("Element Value:", element.value)
            #print("Element Direction:", element.direction)
            #print("Element Position:", pos)


            # Handles the case where elementLeft has pos -1 which is last in the list
            if pos == 0 and element.direction == -1:
                #print("IndexError Raised")
                raise IndexError

            if element.direction == -1:
                #print("Direction is:", self.ElementArray[pos].direction)
                #print(elementLeft.value)
                elementLeft = self.ElementArray[pos - 1]
                if element.value > elementLeft.value:
                    #print("The element", element.value, "is mobile, pointing to the left")
                    return True
                elif element.value < elementLeft.value:
                    #print("The element", element.value, "is not mobile, pointing to the left")
                    return False
            elif element.direction == 1:
                #print("Direction is:", self.ElementArray[pos].direction)
                elementRight = self.ElementArray[pos + 1]
                if element.value > elementRight.value:
                    #print("The element", element.value, "is mobile, pointing to the right")
                    return True
                elif element.value < elementRight.value:
                    #print("The element", element.value, "is not mobile, pointing to the right")
                    return False

        # Handles cases where the element is not pointing towards any other element, and therefore is not mobile
        except IndexError:
            #print("Index error, meaning the element is pointing towards nothing")
            return False
                   
    # Use this on an array of elements to find out if there are any mobile elements
    def isAnyMobile(self):
        list = self.ElementArray
        for i in range(0,len(self.ElementArray)):
            #print()
            #print(i)
            if Permutation(list).isMobile(i):
                #print("There is a mobile element in the list")
                return True
                #break
        #print("No mobile element found in the list")
        return False
            
    # Use this on an array of elements to find the position of the largest mobile element in the list
    def largestMobile(self):
        #print("\nLargest Mobile Called")
        list = self.ElementArray
        mobileValue = []
        if Permutation(list).isAnyMobile():
            for i in range(0,len(list)):
                #print("i",i)
                if Permutation(list).isMobile(i):
                    position = i
                    mobileValue.append(list[i].value)
                    #print("Element", i, "is mobile")
                else:
                    pass
                    #print("Element", i, "is not mobile")
            #print("all mobiles:", mobileValue)
            
            largest = max(mobileValue) 
            #print("largest",largest)
            for i in range(0, len(list)):
                if list[i].value == largest:
                    #print(i, "is the position of the largest element")
                    return i
                else:
                    pass
                    #print(i, "is not the position of the largest element")
        else:
            #print("No mobile elements")
            return -1
                
    def nextPermutation(self):
        #print("Next Permutation Called")
        list = self.ElementArray
        largestMobile = Permutation(list).largestMobile()
        #print("Largest mobile1:", list[largestMobile].value)
        direction = list[largestMobile].direction
        origList = []
        if direction == 1:
            #print("Direction was to the right (1)")
            for i in range(0, len(list)):
               #print(list[i].value)
               pass
            list[largestMobile], list[largestMobile + 1] = list[largestMobile + 1], list[largestMobile]
            #print("Swapped", list[largestMobile].value, "and", list[largestMobile + 1].value)
            #for i in range(0, len(list)):
                #print(list[i].value)
            return list
        elif direction == -1:
            #print("Direction was to the left (-1)")
            #print("Original List")
            for i in range(0, len(list)):
               #print(list[i].value)
               pass
            list[largestMobile - 1], list[largestMobile] = list[largestMobile], list[largestMobile - 1]
            #print("Swapped", list[largestMobile - 1].value, "and", list[largestMobile].value)
            #for i in range(0, len(list)):
             #   print(list[i].value)
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
    print("\nPermute(",n,") called")
    elementList = []
    allPermutations = []
    for i in range(1,n + 1):
        #print(Element(i, -1))
        theElement = Element(i, -1)
        elementList.append(theElement)

    # initialized permutation list, this is the first one
    permutationList = Permutation(elementList)
    print(permutationList.printElements()[0])

    while permutationList.isAnyMobile():
        #print("there are mobile elements")
        largestMobile = permutationList.largestMobile()
        permValueList = permutationList.printElements()[0]

        newList = permutationList.nextPermutation()
        #print("new Permutation value List:", permutationList.printElements()[0])
        #print("new Permutation direction List:", permutationList.printElements()[1])
        
        #largestMobile = permutationList.largestMobile()

        #print(permutationList.printElements()[0])
        #newList = permutationList.nextPermutation()
        for i in range(0,len(elementList)):
            #print("i:",i)
            #print("value:",permValueList[i])

            if permValueList[i] > permValueList[largestMobile]:
                #print(permValueList[i])
                #print(permValueList[largestMobile])
                elementList[i].changeDirection()
                #print("directionhas been changed at index", i)
            else:
                pass
                #print("There were no elements larger than the largest mobile")
        allPermutations.append(permutationList.printElements()[0])


    print(allPermutations)
    #print(permutationList.printElements()[0])
    #print(permutationList.printElements()[1])
        
    #print(valueList)

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

#permuteTime(10)
permuteTime2(10)



### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###
###                             TESTS PART A                                          ###
### --------------------------------------------------------------------------------- ###
### --------------------------------------------------------------------------------- ###

# -------------------------------- #
# Test code for the Element class  #
# -------------------------------- #
def ElementClassTests():
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

#ElementClassTests()

# ------------------------------------ #
# Test code for the Permutation class  #
# ------------------------------------ #
def PermutationClassTests():
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

# permute(1)
# permute(2)
# permute(3)
# permute(4)
# #permute(5)
# permute2(1)
# permute2(2)
# permute2(3)
# permute2(4)
# #permute(5)

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
