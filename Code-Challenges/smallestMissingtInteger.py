import random

"""Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000]."""

# V1, O(N**2), HIGH CORRECTNESS, LOW PERFORMANCE
# def solution(A):
#     """
#     Given array A, returns smallest positive integer, > 0, that does not occur in array A.
    
#     Cases:
#         len(A) = 0, always returns 1
#         len(A) > 0
    
#     A - array of N integers
#     """
#     # if len A is 0, return 1
#     # else:
#         # get min and max of array
#         # if both are < 0, return 1
#         # else:
#             # iterate through range(1,max+1):
#                 # if num not in A:
#                     # return num
#             # return max + 1 if list is good
            
#     if len(A) == 0:
#         return 1
#     else:
#         if min(A) < 0 and max(A) < 0:
#             return 1
#         else:
#             for n in range(1, max(A)+1):
#                 if n not in A: # INEFFICIENT LOOKUP, CONVERT TO SET
#                     return n
#             return max(A)+1


# V2, time efficient
# Testing for the presence of a number in a set is FAST in Python
def solution(A):
    """
    Given array A, returns smallest positive integer, > 0, that does not occur in array A.
    
    Cases:
        len(A) = 0, always returns 1
        len(A) > 0
    
    A - array of N integers
    """
    a = set(A)
    smallest_int = 1
    while smallest_int in a:
        smallest_int += 1
    return smallest_int

test_arr = list(range(1, 100000+1))
random.shuffle(test_arr)
print(solution(test_arr))