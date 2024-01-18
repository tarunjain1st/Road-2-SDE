'''
link: https://leetcode.com/problems/climbing-stairs
Q70. Climbing Stairs

Approach:
🚀 Just solved the classic climbing stairs problem! 🌟
Optimized Fibonacci-like sequence calculation for climbing 𝑛 stairs, iterative approach with rolling variables, eliminating the need for an array. some might say this is nothing but a dynamic programming pattern.

⏰ O(n) - Iterating through steps once.
🚀 O(1) - Constant space for rolling variables. 💡
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize total_ways to 1 as there's 1 way to climb 0 or 1 stairs
        total_ways = 1

        # Initialize variables for the number of ways to climb 1 and 2 stairs, respectively
        ways_to_reach_prev1 = 1
        ways_to_reach_prev2 = 1

        # Iterate from the 3rd step up to the target step n
        for i in range(2, n+1):
            # Calculate the total number of ways to climb the current step
            total_ways = ways_to_reach_prev1 + ways_to_reach_prev2
            
            # Update variables for the next iteration
            ways_to_reach_prev1, ways_to_reach_prev2 = ways_to_reach_prev2, total_ways

        # Return the total number of ways to climb n stairs
        return total_ways
