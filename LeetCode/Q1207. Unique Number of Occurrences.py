'''
link: https://leetcode.com/problems/unique-number-of-occurrences
Q1207. Unique Number of Occurrences

Approach:
Initially counted the frequency of each element in the array. Extract the frequencies and check if the number of unique frequencies matches the length of the original array.

⏰ O(N), where N is the length of the input array.
🚀 O(N), as we store the frequencies in a separate list and set.
'''

from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count the frequency of each element in the array
        frequency_counter = Counter(arr)

        # Extract the frequency values
        frequencies = frequency_counter.values()

        # Check if the number of unique frequencies is equal to the length of the array
        return len(set(frequencies)) == len(arr)
