class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        temp = ''
        for i in range(len(s)):
            temp = s[i]
            
            for j in range(i+1,len(s)):
                if s[j] not in temp:
                    temp = temp + s[j]
                else:
                    break
                                
            if len(result) < len(temp):
                result = temp
            
        return len(result)

strs = "pwwkew"

solve = Solution()
result = solve.lengthOfLongestSubstring(strs)
print(result)