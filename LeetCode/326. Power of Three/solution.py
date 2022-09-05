class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            while(n!=1):
                if n%3 != 0:
                    return False
                n = n/3
            return True

        else:
            return False

n = 27
solve = Solution()
result = solve.isPowerOfThree(n)
print(result)