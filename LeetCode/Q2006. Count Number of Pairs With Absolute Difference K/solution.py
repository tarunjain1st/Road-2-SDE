class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        for i, ivalue in enumerate(nums[:-1]):
            for jvalue in nums[i+1:]:
                if abs(ivalue-jvalue) == k:
                    count+=1
        return count

nums = [1,2,2,1]
k = 1

solve = Solution()
result = solve.countKDifference(nums,k)
print(result)