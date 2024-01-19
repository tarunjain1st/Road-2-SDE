'''
link: https://leetcode.com/problems/minimum-falling-path-sum
Q931. Minimum Falling Path Sum

Approach:
* Utilizes dynamic programming to find the minimum falling path sum in a given matrix.
* Starts from the bottom row and iterates upwards, calculating the minimum path sum at each step.

⏰ O(n^2), where n is the size of the matrix.
🚀 O(n^2), as we use a 2D array to store intermediate results.
'''
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[n-1] = matrix[n-1][:]

        # Iterate from the second-to-last row to the first row
        for i in range(n-2, -1, -1):
            for j in range(n):
                # Calculate the minimum falling path sum
                cur = dp[i+1][j]
                if j+1 < n: cur = min(cur, dp[i+1][j+1])
                if j-1 >= 0: cur = min(cur, dp[i+1][j-1])
                dp[i][j] = cur + matrix[i][j]
                
        # Return the minimum falling path sum from the first row
        return min(dp[0])
