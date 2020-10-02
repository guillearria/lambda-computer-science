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

uniqueCharacters("hello") # 4

uniqueCharacters("HeLlo WorLd") # 8

uniqueCharacters("gOoD MORninG") # 10

uniqueCharacters("Do Special Characters Count???") # 16