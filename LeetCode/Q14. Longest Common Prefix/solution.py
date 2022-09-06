class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minSize = len(strs[0])
        index = 0
        result = ''
        for i in range(len(strs)):
            if minSize >= len(strs[i]):
                minSize = len(strs[i])
                index = i
        if minSize == 0:
            return result
        if len(strs) == 1:
            return strs[0]
        for i in range(minSize):
            temp = strs[index][i]
            for j in range(len(strs)):
                if strs[j][i] != temp:
                    return result
            result += temp
        return result

strs = ["flower","flow","flight"]
solve = Solution()
result = solve.longestCommonPrefix(strs)
print(result)