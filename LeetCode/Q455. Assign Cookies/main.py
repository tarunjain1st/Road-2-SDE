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
        
