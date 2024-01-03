# [Question Link](https://leetcode.com/problems/number-of-laser-beams-in-a-bank)

# Intuition
Every row can contubute to result, if its next row follows given 2 properties. So, we need to check for each cell with `1` (security device), how many other cells can collaborate to create a laser beam with given security device.  
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
* `Brute-force approach`: 
   * Iterate over every cell in row and column if value is `1`, check of next possible row and column with can contribute to create a laser beam with pairing security devices. 
   * TC: O(R*C^2), where R and C is size of rows and columns.
   * SC: O(1)
   
* `Optimal approach`: 
   * Iterate over rows in a binary string bank, counting the occurrences of '1' in each row and stored count of current/previous and next row consecutively. The total count is the sum of products of '1' counts in consecutive rows.
   * TC: O(N*M), where N and M is size of rows and columns.
   * SC: O(1)
  
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
TC: O(N*M)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
TC: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```Python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows=len(bank)
        if rows<2:
            return 0
        prevCnt=bank[0].count('1')
        nextCnt=bank[1].count('1')
        ans=prevCnt*nextCnt
        for i in range(2, rows):
            if nextCnt: prevCnt=nextCnt
            nextCnt=bank[i].count('1')
            ans+=prevCnt*nextCnt
        return ans

        
```
