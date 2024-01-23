'''
link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Q1239. Maximum Length of a Concatenated String with Unique Characters

✨ Approach:
The solution leverages a recursive approach for generating subsets and dynamically updating the maximum length.
The has_unique function efficiently checks for unique characters, enabling a more concise implementation.

⏱️ Time Complexity: O(2^n), due to the recursive nature of subset generation. However, early termination occurs when duplicate characters are encountered, optimizing certain cases.
💾 Space Complexity: O(n), where n is the length of the input array. This arises from the recursive call stack.

🧐 Insights:
The algorithm showcases a trade-off between simplicity and efficiency.
Optimal for small inputs, but may experience performance issues with larger datasets due to its exponential time complexity.
Dynamic programming or bitwise manipulation could offer alternative approaches for further optimization.
'''

from collections import Counter
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def is_vaild(str1, str2):
            # Check if two strings have unique characters
            combined_freq = Counter(str1) + Counter(str2)
            return max(combined_freq.values()) <= 1

        def max_len_subset(index, string):
            # Recursive function to generate subsets and find maximum length
            if index == N:
                return len(string)

            # Exclude the stringent string and move to the next index
            res = max_len_subset(index + 1, string)

            # Include the stringent string if it has unique characters
            if is_vaild(string, arr[index]):
                res = max(res, max_len_subset(index + 1, string + arr[index]))
                
            return res

        N = len(arr)
        return max_len_subset(0, '')

# Example usage:
# solution = Solution()
# result = solution.maxLength(["un", "iq", "ue"])
# print(result)

