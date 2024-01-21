'''
link: https://leetcode.com/problems/house-robber
Q98. House Robber

👉 Approach:
Dynamic programming breaks down the problem into smaller sub-problems and reuses solutions to avoid redundant calculations. 
Here, we explore two choices at each house - robbing it or skipping it - maximizing the loot.

🧠 Insight: The magic lies in the memoization technique, caching results to eliminate recalculations. 
This transforms a potentially exponential time complexity into a linear one, making the solution efficient.

⏰ TC: O(N), where N is the number of houses.
🚀 SC: O(N), where N is the number of houses.
'''

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}

        def rob_helper(house):
            # Base case: If the current house is beyond the last one, return 0
            if house >= N: return 0

            # Check if the result for the current house is already memoized
            if house in memo: return memo[house]

            # Calculate the maximum amount that can be robbed
            result = max(
                # Skip current house
                rob_helper(house + 1),
                # Rob current house and skip the next one
                nums[house] + rob_helper(house + 2)   
            )

            # Memoize the result for the current house
            memo[house] = result
            return result

        # Start the recursive process from the first house
        return rob_helper(0)

# Example usage:
# solution = Solution()
# result = solution.rob([2, 7, 9, 3, 1])
# print(result)
