''' 
isValidAnagram

Description: 
Given two strings, write a function to determine if the second string is
an ANAGRAM of the first. The number of letters must match (frequency pattern).
Return True or False

Anagram - a word, phrase, or name formed by rearranging the letters of 
another, such as cinema, formed from iceman.

Two words are anagrams of each other if they contain the same number of 
characters and the same characters.
'''

def isValidAnagram(str1, str2):
    # split both strings into letters
    # organize alphabetically
    # compare and return result
    return sorted(str1.lower()) == sorted(str2.lower())

# tests
print(isValidAnagram('','')) # true
print(isValidAnagram('aaz', 'zza')) # false
print(isValidAnagram('anagram', 'nagaram')) # true
print(isValidAnagram('cinema', 'iceman')) # true

print(isValidAnagram('cinemA', 'iceman')) # true
print(isValidAnagram('cinemA ', 'iceman')) # false
print(isValidAnagram('cinemA ', 'iceman ')) # true