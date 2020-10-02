# Write a function that counts unique characters in a given string Note: spaces and special characters (!"/@;&) may count as a unique character

# Example:
# Input: "HeLlo WorLd"
# Output: 8

# Good questions to ask when in an interview:
# Are uppercase and lowercase of the same letter considered a unique character? (In this case yes)
# Are alphanumerical numbers only being counted? Or special characters as well?

def uniqueCharacters(s):
    return len(set([char for char in s]))

# Example tests:
print(uniqueCharacters("hello"))  # 4
print(uniqueCharacters("HeLlo WorLd"))  # 9
print(uniqueCharacters("gOoD MORninG"))  # 10
print(uniqueCharacters("Do Special Characters Count???"))  # 18
