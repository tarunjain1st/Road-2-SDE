# Intuition
We used sorting here, to get maximum number of child who can get cookies. it's required to compare both values to satify the need in minimum order.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
As we need to pick minimum size cookies and child greed to fulfill the requirment, 
* sort both the array of greed(g) and cookies(s) 
* iterated over array comparing element till any one array reaches to its size.
* in each pass we need to check if we can assign a cookie to child with same to less greed.

# Complexity
- Time complexity:
  * TC for sort in O(NLogN)
  * TC for iterative over the array is O(N)
  * So overall complexity is NLogN + N => O(NLogN)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  * SC -> O(1), no auxiliary memory is used.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```Python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookieIndex, greedIndex = 0, 0
        while cookieIndex < len(s) and greedIndex < len(g):
            if g[greedIndex] <= s[cookieIndex]:
                greedIndex+=1
            cookieIndex+=1
        return greedIndex
```
