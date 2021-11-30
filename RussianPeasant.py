### File: RussianPeasant.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### 
###
### 
### Modification Log:
### 
###


### --------------------------------------------------- ###
###         The Russian Peasant Algorithm               ###
### --------------------------------------------------- ###

# The algorithm takes n and m as parameters, uses string 
# formatting to make a table for the addends and returns 
# a list with the product and addends count.

def russianMultiply(n, m):
    try:

        addendCount = 0
        product = 0
        print("{:^9}{:^8}{:^8}".format("n","|","m"))
        print("-" * 32)

        # Stop when n is one, if n is even divide by 2
        # if n is odd, add to addendCount and product
        while n >= 1:
            
            if n % 2 == 0:
                print("{:^9}{:^8}{:^8}".format(int(n), "|", m))
                n = n / 2
                m = 2 * m
            else:
                print("{:^9}{:^8}{:^8}{:^8}".format(int(n), "|", m, "("+str(m)+")"))
                addendCount += 1
                product += m
                n = (n-1)/2
                m = m * 2
        print("{:<24}{:^8}".format("","------"))
        print("{:<24}{:^9}".format("",product))
        
        return [product, addendCount]
    except TypeError:
        print("ERROR: This function only takes integers as input.")
    except:
        print("ERROR: Something went wrong, please check the input.")


### -------------------------------------------- ###
###               Test Functions                 ###
### -------------------------------------------- ###

# The test functions for testing the russian peasant algorithm
# TestCase takes the testnumber, n, m and the expected result 
# for the multiplication. The function compares the result with 
# the expected result and prints out wether the test passed or failed
# The test function runs the testCase function and adds the testnumber 
# to a list if it passed, and then compares the list of all tests to 
# the list of the passed tests to then print which tests passed and failed.

def testCase(testNumber, n, m, expectedResult):
    print("\nTest", testNumber)
    print("-" * 32)
    actualResult = russianMultiply(n, m)

    if actualResult == expectedResult:
        #print("Test", testNumber, "passed")
        return True
    else:
        #print("Test", testNumber, "failed. Expected",expectedResult, "but found",actualResult,".")
        return False


def test():
    ### --------------------------------------- ###
    ###               ATTENTION                 ###            
    ### --------------------------------------- ###
    # Any additional test numbers must be added 
    # to the testList to take part in the test.
    testList = [1,2,3,4,5,6]
    passedList = []

    # Should print numbers 50, 25, 12, 6, 3, 1 for n and 
    # 65, 130, 260, 520, 1040, 2080 for m and
    # 130, 1040, 2080 for addends with the product 3250
    if testCase(1, 50, 65, [3250,3]):
        # Bitstring for 50 = 110010 means there will be 3 addends
        passedList.append(1)
    
    if testCase(2, 26, 47, [1222,3]):
        # Bitstring for 26 = 011010 means there will be 3 addends
        passedList.append(2)
    
    if testCase(3, 10, 15, [150,2]):
        # Bitstring for 10 = 001010 means there will be 2 addends
        passedList.append(3)
    
    if testCase(4, 2, 4, [8,1]):
        passedList.append(4)

    if testCase(5, 'a', 'b', None):
        passedList.append(5)
    
    if testCase(6, 1234, 4321, [5332114,5]):
        # Bit string for 1234 = 10011010010, 5 addends.
        passedList.append(6)

    print("\nTest Results:")
    for test in testList:
        if test not in passedList:
            print("Test", test, "failed.")
        else:
            print("Test", test, "passed.")
    


#russianMultiply(2,3)
#print(russianMultiply(50, 65))
test()