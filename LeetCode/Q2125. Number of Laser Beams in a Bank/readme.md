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
SC: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Brute-Force Code
```Python      
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows=len(bank)
        cols=len(bank[0])
        ans=0
        row, nRow = 0, 1
        while nRow < rows:
            flag=False
            for col in range(cols):
                for nCol in range(cols):
                    if bank[row][col] == '1' and bank[nRow][nCol]=='1':
                        ans+=1
                    if bank[nRow][nCol]=='1':
                        flag=True
            if flag:
                row=nRow
            nRow+=1
        return ans
```

# Code
```Python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows=len(bank)
        bankSecDevice = []
        ans=0
        for i in range(rows):
            if cnt:= bank[i].count('1'):
                bankSecDevice.append(cnt)
        for i in range(len(bankSecDevice)-1):
            ans+=bankSecDevice[i]*bankSecDevice[i+1]
        return ans      
```

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

```Python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows=len(bank)
        ans=0
        row, nRow = 0, 1
        while nRow < rows:
            curCount=bank[row].count('1')
            nxtCount=bank[nRow].count('1')
            if nxtCount>0:
                row=nRow
            nRow+=1
            ans+=curCount*nxtCount
        return ans      
```

```Python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows=len(bank)
        cols=len(bank[0])
        ans=0
        row, nRow = 0, 1
        while nRow < rows:
            flag=False
            curCount=0
            nxtCount=0
            for col in range(cols):
                if bank[row][col] == '1':
                    curCount+=1
            for nCol in range(cols):
                if bank[nRow][nCol]=='1':
                    nxtCount+=1
                    flag=True
            if flag:
                row=nRow
            nRow+=1
            ans+=curCount*nxtCount
        return ans     
```
