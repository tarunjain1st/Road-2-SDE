'''
link: https://leetcode.com/problems/sum-of-subarray-minimums
Q907. Sum of Subarray Minimums

Approach:
* Used a stack-based algorithm to efficiently calculate the sum of minimum elements in all possible subarrays of a given array. 
* It iterates through the array, maintaining a stack to track the elements and their counts. 
* The stack helps identify the number of subarrays where each element is the minimum.
* By processing the array in both forward and backward directions, the algorithm determines the contribution of each element to the total sum, resulting in an optimal solution.

⏰ TC: O(N), The algorithm makes a single pass through the array, performing constant-time operations for each element.

🚀 SC: O(N), This is primarily due to the additional space required for the stack and the result arrays. 
The algorithm maintains a constant amount of extra space apart from the input array, making it efficient in terms of memory usage.
'''

from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def near_min(start, end, seq, include=False):
            """
            Function to count of subarrays where the current element is the minimum.
            Parameters:
            - start: Starting index for iteration
            - end: Ending index for iteration
            - seq: Sequence for iteration (1 for forward, -1 for backward)
            - include: Flag to include or exclude equal elements while calculating count
            """
            stack, result = [], [None] * N 
            for i in range(start, end, seq):
                count, element = 1, arr[i] 
                if include:
                    # Include element if greater then top of stack
                    while stack and stack[-1][0] > element:
                        count += stack.pop()[1]
                else:
                    # Include element if greater or equal then top of stack
                    while stack and stack[-1][0] >= element:
                        count += stack.pop()[1]
                stack.append((element, count))
                result[i] = count
            return result

        MOD, N = 10**9 + 7, len(arr)
        
        # Calculate contributions from left and right subarrays
        left = near_min(0, N, 1, True)
        right = near_min(N-1, -1, -1)
    
        # Calculate the sum of subarray using the contributions till left and right
        result = sum(( left[i] * right[i] * arr[i] ) % MOD for i in range(N)) % MOD
        return result

# Example usage
sol = Solution()
sample_array = [3, 1, 2, 4]
result = sol.sumSubarrayMins(sample_array)
print(result)
