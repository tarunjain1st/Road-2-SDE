# [Q2870. Minimum Number of Operations to Make Array Empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty)

# Intuition
The goal is to find the minimum number of operations required to make all numbers in a given list divisible by 3. The approach involves examining the frequency of each number in the list and determining the minimum operations needed for groups of numbers with the same frequency. 
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach

`Bruteforce Approach`
After creating frequency map of numbers in list, we can try all possible path, so either we can pick 2 or 3 in recursively call with frequency subtracting choice from it, maintaining minimum count, if any call reaches to 1 return -1 as answer, this approach is very time consuming we can impoving it using DP as we can see for below cases

|case|answer|
|-|-|
|1|-1|
|2|1|
|3|1|
|4|2|
|5|2|
|6|2|
|7|3|

`Optimal Approach`
In this approach we maintain count the frequency of each number in the list using a Counter. Iterate through the frequency values, calculate the minimum operations for each group of numbers with the same frequency, and accumulate these values. Return the total minimum operations. Special case: If any number appears only once, return -1, as it cannot be made divisible by 3 with operations.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
O(N)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
O(K), where K is the number of unique elements in the input list
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```Python
from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans=0
        for val in freq.values():
            if val==1: return -1
            ans+=ceil(val/3)
        return ans
```
