# File: Anagrams.py
# Author: Samuel Rudqvist
# CSCI 0262 Algorithms
# This program is an anagram checker. It checks two strings to see
# if they are anagrams.



#The test function conducts a series of tests by calling testPair.

def test():
    testPair(1,'eat','tea',True)
    testPair(2,'Clint Eastwood','Old West Action',True)
    testPair(3,'arranged','deranged',False)
    testPair(4, "32", 32, False)
    
	#YOUR ADDITIONAL TESTS GO HERE
  
#The testPair function takes a test number, two words, and the expected result (true if they are anagrams and false otherwise).  It prints a notice of whether or not the anagram function gave the correct answer for these two words.
def testPair(testNumber,word1,word2,expected):

    if anagram(word1,word2)==expected:
        result = "passed"
    else:
        result = "failed"
    # Added for testing purposes. 
    word1 = str(word1)
    word2 = str(word2)
    print("Test "+str(testNumber)+"  "+result+":"+ word1+" "+word2+" "+str(expected))


#The anagram function takes two words and returns true if they are anagrams and false otherwise.  

def anagram(word1,word2):
	#YOUR CODE GOES HERE

    # Check if the given words are of type string.
    if type(word1) != str:
        print("The first word is not a string, please change word1 to a string.")
        return False

    if type(word2) != str:
        print("The second word is not a string, please change word2 to a string.")
        return False

    # Make sure the words are the same length.
    str1Length = len(word1)
    str2Length = len(word2)
    
    if str2Length != str1Length:
        return False

    # Sort the words and check if they contain the same letters.
    word1 = sorted(word1)
    word2 = sorted(word2)
    
    for i in range(0, str1Length):
        if word1[i] != word2[i]:
            return False
    
    return True



test()