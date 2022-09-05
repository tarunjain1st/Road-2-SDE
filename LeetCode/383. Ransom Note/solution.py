class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == magazine:
            return True
        temp = list(ransomNote)
        for i in magazine:
            if i in temp and temp:
                temp.remove(i)                
        if len(temp) == 0:
            return True
        else:
            return False

ransomNote = "aa"
magazine = "aab"
solve = Solution()
result = solve.canConstruct(ransomNote, magazine)
print(result)