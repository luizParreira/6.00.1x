
# Assume 's' is a given
# Find the largest sequence of string that is in alphabetical order

# Ex. s = 'azcbobobegghakl'
# Sould Return 'beggh'
# AND
# s = 'abcbcd' -> 'abc'

# 1 -> Slice the string from beginning to end
# 2 -> Test whether the values are in alphabetical order
#   2.1 -> If True they are keep going ahead and keeping track of the Longest substring and its sliceable indexes
#   2.2 -> If False then set the last index of the current substring to be the first one


def alphabetical_substring(s):
    
    idx = 1
    i = 0
    biggest = s[0]
    statement = True
    while statement:
        if s[idx - 1] <= s[idx]:  
            if len(s[i : idx +1]) > len(biggest):
                biggest = s[i : idx+1]
            idx += 1
        else:
            i = idx
            idx += 1
        if idx == len(s):
            statement = False
    return "Longest substring in alphabetical order is: " + biggest

print alphabetical_substring('abcbcd')
print alphabetical_substring('azcbobobegghakl')      

    



