# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    """ Returns true if the passed-in number is even.

    num - int, must be a whole number
    """
    remain = num%2
    is_even = not bool(remain)

    return is_even

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

result = is_even(num)

if result:
    print("Even!")
else:
    print("Odd")
