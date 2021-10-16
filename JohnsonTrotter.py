### File: JohnsonTrotter.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### 
###
### 
### Modification Log:
### 
###


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
            print("Direction has been changed to", self.direction)
        elif self.direction == -1:
            self.direction = 1
            print("Direction has been changed to", self.direction)
    
    def getDirection(self):
        return self.direction
    
    #def setDirection(self, direction):
     #   self.direction = direction


# Test code for the Element class
myElement = Element(1, 1)
myElement2 = Element(2, -1)
myElement3 = Element(3, 1)
myElement4 = Element(4, -1)
myElement5 = Element(5, 1)

print("Value:", myElement.value)
print("Direction:", myElement.direction)
myElement.changeDirection()
print("Direction:", myElement.direction)


# The Permutation class takes an array of Elements.
class Permutation:
    def __init__(self, ElementArray):
        self.ElementArray = ElementArray

    # Element is mobile if it is greater than the element it is pointing to
 
    # Use this on an array of elements, give it the position of an element and it will 
    # return true if the element is mobile and false if it is not
    def isMobile(self, pos):
        #print(self.ElementArray)
        print("isMobile Called")
        try:
            element = self.ElementArray[pos]
            print("Element Value:", element.value)
            print("Element Direction:", element.direction)
            print("Element Position:", pos)


            # Handles the case where elementLeft has pos -1 which is last in the list
            if pos == 0 and element.direction == -1:
                print("IndexError Raised")
                raise IndexError

            if element.direction == -1:
                #print("Direction is:", self.ElementArray[pos].direction)
                #print(elementLeft.value)
                elementLeft = self.ElementArray[pos - 1]
                if element.value > elementLeft.value:
                    print("The element", element.value, "is mobile, pointing to the left")
                    return True
                elif element.value < elementLeft.value:
                    print("The element", element.value, "is not mobile, pointing to the left")
                    return False
            elif element.direction == 1:
                print("Direction is:", self.ElementArray[pos].direction)
                elementRight = self.ElementArray[pos + 1]
                if element.value > elementRight.value:
                    print("The element", element.value, "is mobile, pointing to the right")
                    return True
                elif element.value < elementRight.value:
                    print("The element", element.value, "is not mobile, pointing to the right")
                    return False

        # Handles cases where the element is not pointing towards any other element, and therefore is not mobile
        except IndexError:
            print("Index error, meaning the element is pointing towards nothing")
            return False
            

        
    # Use this on an array of elements to find out if there are any mobile elements
    def isAnyMobile(self):
        list = self.ElementArray
        for i in range(0,len(self.ElementArray)):
            print()
            print(i)
            if Permutation(list).isMobile(i):
            #if self.ElementArray.isMobile(i):
                print("There is a mobile element in the list")
                return True
                #break
        print("No mobile element found in the list")
        return False
            
    # Use this on an array of elements to find the largest mobile element in the list
    def largestMobile(self):
        print("\nLargest Mobile Called")
        list = self.ElementArray
        mobileList = []
        for i in range(0,len(list)):
            print(i)
            if Permutation(list).isMobile(i):
                position = i
                mobileList.append(list[i])
                print("Element", i, "is mobile")
            else:
                print("Element", i, "is not mobile")
        for i in range(0, len(mobileList)):
            print(mobileList[i].value)
            if 
                
    
    def printArray(self):
        for i in range(0,len(self.ElementArray)):
            print(self.ElementArray[i].value, self.ElementArray[i].direction)

    
    
# Test Code for Permutation class
myPerm = Permutation([myElement, myElement2, myElement3, myElement4, myElement5])
print("myPerm:", myPerm)
myPerm.printArray()
#myPerm.isMobile(4)

myElement6 = Element(13, -1)
myElement7 = Element(12, -1)
myElement8 = Element(11, -1)
myElement9 = Element(10, -1)

myElement10 = Element(4, -1)
myElement11 = Element(2, -1)
myElement12 = Element(5, -1)
myElement13 = Element(10, -1)

myPerm2 = Permutation([myElement6,myElement7, myElement8, myElement9])
myPerm3 = Permutation([myElement10, myElement11, myElement12, myElement13])
myPerm2.isAnyMobile()
myPerm3.largestMobile()
