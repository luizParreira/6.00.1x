# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    
    if aStr == "":   
        print aStr
        return aStr
    return reverseString(aStr[1:]) + aStr[0]


#print 'abc'[:-1]
print reverseString('abc')

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """

    if (x or word) == "":
        return False
    if not x[0] in word :
        return False
    if len(x) == 1:
        return True
    if word.find(x[0]) > word.find(x[1]):
        return False
    return x_ian(x[1:], word)
    
print x_ian('eric', 'meritocracy')
print x_ian('eric', 'cerium')
print x_ian('john', 'mahjong')
print
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    #print text
    if text == "": return ""
    if lineLength == 0: return text
    return  ' '.join(text.split(' ')[:lineLength]) +"\n" + insertNewlines(' '.join(text.split(' ')[lineLength:]), lineLength )
  
    
print insertNewlines("Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed a class. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.", 5)
