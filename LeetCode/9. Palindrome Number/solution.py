class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        temp=0
        n=len(str(num))
        for i in range(n):
            digit = num%10
            temp+=pow(10,n-i-1)*digit
            num=num//10
        return x==temp

x = 121
solve = Solution()
result = solve.isPalindrome(x)
print(result)