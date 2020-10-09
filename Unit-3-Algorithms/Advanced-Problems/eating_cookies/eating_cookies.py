'''
Input: an integer
Returns: an integer
'''

# First pass solution:
# def eating_cookies(n):
#     def cookies(cks_to_be_eaten, total_cks):
#         # "how many ways" tells me I can use recursion, its a combination problem
#         # base cases:
#         # if cookie monster eats 
#         if cks_to_be_eaten > total_cks:
#             return 0
#         if cks_to_be_eaten == total_cks:
#             return 1
#         return cookies(cks_to_be_eaten+1, total_cks) + cookies(cks_to_be_eaten+2, total_cks) + cookies(cks_to_be_eaten+3, total_cks)

#     return cookies(0, n)

cache = {}

# Optimized for large inputs:
def eating_cookies(n, idk={}):
    # base cases:
    # if no cookie, no way to eat it
    # if theres 1 cookie, only 1 way to eat it
    # if theres 2, 2 ways to eat it
    # if theres 3, 4 ways to eat it
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4

    if n not in cache:
        cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3) 
        
    return cache[n] 


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
