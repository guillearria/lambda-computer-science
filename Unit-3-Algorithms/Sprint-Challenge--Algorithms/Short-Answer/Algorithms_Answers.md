#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) At first this pseudocode seems like it would be of runtime O(n^3) because as n increases, so does the amount of while loops by n^3, however, since n^2 is added every time I believe the final time complexity to be: O(n).

b) In this case, the code would run n times every single time no matter what due to the for loop. Then the while loop would cause the code to run what I believe to be n/2 times. Meaning the final time complexity is: O(n^2).

c) I'm assuming since there is no input size of n, the time complexity would be O(1).

## Exercise II

<!-- throwing eggs off n-story building, many eggs -->
<!-- eggs only break at floor equal or greater to f -->
<!-- strategy to determine f such that dropped + broken eggs is minimized -->

I understand this question now and I believe a good solution for this would be similar to a binary search. These would be the steps:

1. Create a sorted list with individual n-stories as value: ie. range(1, n+1)
1. Find the middle item in the list
1. If egg breaks at middle value:
  - Check if egg breaks at (middle value - 1):
    * If it does not, then middle value is our desired f value
    * If it does, we're too high, eliminate all values after middle value (RHS), repeat from step 2
1. If egg does not break at middle value:
  - Check if egg breaks at (middle value + 1):
    * If it does, (middle value + 1) is our desired f value
    * If it does not, we're too low, eliminate all values before middle value (LHS), repeat from step 2