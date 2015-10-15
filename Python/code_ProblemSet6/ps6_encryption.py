# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShift(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    lettersUpper = list(string.ascii_uppercase)
    lettersLower = list(string.ascii_lowercase)
    res = {}
    b =  0
    for i in range(len(lettersUpper)):
        if (i + shift) >= (len(lettersUpper)):
            res[lettersUpper[i]] =  lettersUpper[b]
            b += 1
        else:
            res[lettersUpper[i]] =  lettersUpper[i + shift]
    b = 0 
    for i in range(len(lettersLower)):
        if (i + shift) >= (len(lettersLower)):
            res[lettersLower[i]] =  lettersLower[b]
            b += 1
        else: 
            res[lettersLower[i]] =  lettersLower[i + shift]
    return res 




def isNotValid(letter):
    punc = list(string.punctuation)
    nums = range(0,10)
    space = [" "]

    return letter in (punc or nums or space)

                 
def applyCoder(text, coder):
    """

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    
    textList = list(text)
    r = ""
    for i in range(len(textList)):
        r += textList[i] if isNotValid(textList[i]) else coder.get(textList[i], textList[i])
    return r 

#print applyCoder("Khoor, zruog!", buildCoder(23))

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift)) # Remove this comment when you code the function

# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    
    1 - Switch the text with values between 0 and 26
    2 - Apply shift on text with shift = 0...26
    3 - Check if each word is valid, and count the valid words for each shift try
    4 - Return the number that returned the largest number of valid words

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    max = 0
    r = 0
    for i in range(26):
        shifted = applyShift(text, i)
        wordsShifted = shifted.split(" ")
        j = 0
        for word in wordsShifted:
            if isWord(wordList, word):
                j += 1
        if j > max:
            max = j
            r = i
    return r 

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    w = loadWords()
    s = getStoryString()
    b = findBestShift(w,s)
    return applyShift(s, b)
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
