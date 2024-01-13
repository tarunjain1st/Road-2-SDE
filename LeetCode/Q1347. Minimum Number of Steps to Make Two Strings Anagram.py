'''
link: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
Q1347. Minimum Number of Steps to Make Two Strings Anagram

Approach:
This question i solved using an array (size 26 lowercase chars) to represent the frequency difference between characters in two strings s and t. 
This approach efficiently captures the excess occurrences of characters in one string compared to the other.

⏰ TC: O(N + M), where N & M is length of both strings.
🚀 SC: O(1), because array of constant 26 length.
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * 26
        for charS, charT in zip(s,t):
            indexS = ord(charS) - ord('a')
            indexT = ord(charT) - ord('a')
            freq[indexS] += 1 
            freq[indexT] -= 1

        count = sum(val for val in freq if val>0)
        return count
