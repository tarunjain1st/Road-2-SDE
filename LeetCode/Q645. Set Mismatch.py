'''
link: https://leetcode.com/problems/set-mismatch
Q645. Set Mismatch

👉 Approach:
In solving the problem of finding a duplicate and a missing number in an array, the approach involves counting the frequency of each element using a frequency counter. 
Next, it iterates through the range from 1 to n, identifying a missing number when an index is not in the frequency counter, and marking a duplicate when the frequency of an index is 2

📈 SC: O(n) - Utilizes a counter to store the frequency of each number.
⏰ TC: O(n) - Iterates through the array once to find the duplicate and missing numbers.
'''

from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, duplicate, missing = len(nums), None, None

        # Step 1: Count the frequency of each number in the array
        frequency = Counter(nums)

        # Step 2: Iterate over the range of 1 to n (inclusive)
        for i in range(1, n+1):
            # Check if not in frequency counter mark it as missed number
            if i not in frequency:
                missing = i
            # Check if frequency of number is 2 mark it as duplcate number     
            elif frequency[i] == 2:
                duplicate = i
        
        # Step 3: Return the found duplicate and missing numbers
        return duplicate, missing
