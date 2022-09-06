class Solution:
    def reverse(self, x: int) -> int:

        num=abs(x)
        temp=0
        n=len(str(num))
        for i in range(n):
            digit = num%10
            temp+=pow(10,n-i-1)*digit
            num=num//10
        
        if temp >= 2**31-1 or temp <= -2**31: return 0
        else: return -temp if x<0 else temp

x = 123

solve = Solution()
result = solve.reverse(x)
print(result)