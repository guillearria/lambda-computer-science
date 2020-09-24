''' 
isValidAnagram

Description: 
Given two strings, write a function to determine if the second string
is an ANAGRAM of the first. The number of letters must match (frequency pattern).
Return True or False

Anagram - a word, phrase, or name formed by rearranging the letters of another, 
such as cinema, formed from iceman.
'''

def isValidAnagram(str1, str2):
    # split both strings into letters
    # organize alphabetically
    # compare and return result
    return sorted(str1) == sorted(str2)

# tests
print(isValidAnagram('','')) # true
print(isValidAnagram('aaz', 'zza')) # false
print(isValidAnagram('anagram', 'nagaram')) # false
print(isValidAnagram('cinema', 'iceman')) # true