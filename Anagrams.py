### File: Anagrams.py
### Author: Samuel Rudqvist
### CSCI 0262 Algorithms
### This program is an anagram checker. It checks two strings to see
### if they are anagrams.
###
### Modification Log:
### 2021/08/30: Created the file, copied test functions from Dr. Browning. def anagram() is ready to be tested.
### 2021/08/31: Improvements in error handling has been made. User now gets a message saying what word is not a string.
###             

"""
Should header be done like this?
"""

#The test function conducts a series of tests by calling testPair.

def test():
    testPair(1,'eat','tea',True)
    testPair(2,'Clint Eastwood','Old West Action',True)
    testPair(3,'arranged','deranged',False)
    testPair(4, "32", 32, False)
    testPair(5, "BigAndSmall", "bIGaNDsMALL", True)
    testPair(6, "Nag a ram", "anagram", True)
    testPair(7, "Slot Machines", "Cash lost in me", True)
    testPair(8, "football", "laundry basket", False)




    
	#YOUR ADDITIONAL TESTS GO HERE
  
#The testPair function takes a test number, two words, and the expected result (true if they are anagrams and false otherwise).  It prints a notice of whether or not the anagram function gave the correct answer for these two words.
def testPair(testNumber,word1,word2,expected):

    if anagram(testNumber,word1,word2)==expected:
        result = "passed"
    else:
        result = "failed"
    # Added for testing purposes. Is this okay??
    word1 = str(word1)
    word2 = str(word2)
    print("Test "+str(testNumber)+"  "+result+":"+ word1+" "+word2+" "+str(expected))


#The anagram function takes two words and returns true if they are anagrams and false otherwise.  
def anagram(testNumber,word1,word2):    # Is this okay??
	#YOUR CODE GOES HERE
    try:
        # Check if the given words are of type string.
        if type(word1) != str:
            print("\nThe first word in test", testNumber, "is not a string, please change word1 to a string.\n")
            return False

        if type(word2) != str:
            print("\nThe second word in test", testNumber, "is not a string, please change word2 to a string.\n")
            return False

        # Make all the letters in the words lower case.
        word1 = word1.lower()
        word2 = word2.lower()

        # Ignore spaces.
        word1 = word1.replace(" ", "")
        word2 = word2.replace(" ", "")

        # Get the length of the words.
        str1Length = len(word1)
        str2Length = len(word2)

        # Sort the words
        word1 = sorted(word1)
        word2 = sorted(word2)
        
        # Check if the words are the same length.
        if str2Length != str1Length:
            return False
        
        # Check if the words contain the same letters.
        for i in range(0, str1Length):
            if word1[i] != word2[i]:
                return False
        
        return True
        
    except:
        print("\nSomething went wrong, please check all of the inputs and make sure they are strings.\n")
        ans = str(input("Run again anyways?(y/n) "))
        if y in ans:
            test()
        else:
            quit()



test()