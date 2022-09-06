class Solution:
    def isValid(self, s: str) -> bool:
        stack = [None]
        for i in s:
            if i in ['(','{','['] :
                stack.append(i)
            elif i==')' and stack[-1]=='(' or i==']' and stack[-1]=='[' or i=='}' and stack[-1]=='{' :
                stack.pop() 
            else: stack.append(i)
        return stack.pop() is None
        
strs = "{}{}"
solve = Solution()
result = solve.isValid(strs)
print(result)