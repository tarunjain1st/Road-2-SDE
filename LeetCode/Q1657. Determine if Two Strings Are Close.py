'''
link: https://leetcode.com/problems/determine-if-two-strings-are-close/
Q1657. Determine if Two Strings Are Close

Approach:
 To determine if two words are 'close strings' – a term defined as having the same length, sharing the same set of characters, and exhibiting similar character frequency distributions. 
 Leveraged Python's collections module for efficient character counting and sorting, ensuring a clean and intuitive solution. 

⏰ TC: O(NlogN), for sorting where N is length of alike string.
🚀 SC: O(1), because frequency counter of constant 26 lowercase letters.
'''

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if the lengths are equal
        if len(word1) != len(word2):
            return False

        # Check if the sets of characters are equal
        if set(word1) != set(word2):
            return False

        # Get the frequency distributions of characters in both words
        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())

        # Compare the sorted frequency distributions
        return freq1 == freq2

# Example usage:
# solution = Solution()
# result = solution.closeStrings("abc", "bca")
# print(result)
