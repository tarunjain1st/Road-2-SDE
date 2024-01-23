'''
link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Q1239. Maximum Length of a Concatenated String with Unique Characters

👉 Approach:
In addressing the challenge of finding the maximum length of a concatenated string with unique characters, the approach utilizes backtracking. 
It explores different combinations of words, ensuring uniqueness through a set (unique_chars) and a helper function (is_unique). The code efficiently prunes invalid paths, maintaining linear space complexity.

📈 SC: O(n) - Linear space complexity as the set (unique_chars) stores unique characters.
⏰ TC: Exponential - Due to recursive backtracking, the time complexity exhibits an exponential growth.

Optimizations include pruning invalid paths and avoiding explicit subset generation for enhanced efficiency.
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

