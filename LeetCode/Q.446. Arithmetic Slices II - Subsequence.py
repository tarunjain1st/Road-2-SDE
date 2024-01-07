#Question: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        dp=[defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                freq=dp[j][diff]
                dp[i][diff] += freq+1
                ans += freq
        return ans

'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        dp=[defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                differ = nums[i]-nums[j]
                ans+=dp[j][differ]+1
                dp[i][differ]+=dp[j][differ]+1
        return ans - (n*(n-1)//2)
'''

'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subseqs=[]

        def checkAP(arr):
            diff = arr[1]-arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True

        def genrateSubseqs(index, subseq):
            if index==len(nums):
                subseqs.append(subseq)
            else:
                genrateSubseqs(index+1, subseq+[nums[index]])
                genrateSubseqs(index+1, subseq)
        ans=0
        genrateSubseqs(0,[])
        for subseq in subseqs:
            n=len(subseq)
            if n>=3 and checkAP(subseq): ans+=1
            
        return ans             
'''
