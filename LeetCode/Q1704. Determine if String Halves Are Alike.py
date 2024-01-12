'''
Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

Approach:
I tried to checks if the first half of a string has the same number of vowels as the second half by iterating through each half, counting vowels, and comparing the counts. 
The updated version can uses a set for faster vowel checking and employs the sum function with generator expressions for a more concise implementation.


⏰ TC: O(n), where n is number of chars in string.
🚀 SC: O(1).
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_diff, size = 0, len(s)

        for char in s[:size//2]:
            if char in vowels:
                vowel_diff+=1
        for char in s[size//2:]:
            if char in vowels:
                vowel_diff-=1

        return True if vowel_diff==0 else False
