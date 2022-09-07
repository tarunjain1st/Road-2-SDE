nums = [2,7,11,15]
target = 9
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] ==  target:
                        return[i,j]

'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, value in enumerate(nums):
            if target-value in hashmap:
                return [hashmap[target-value],i]
            else: hashmap[value]=i


solve = Solution()
result = solve.twoSum(nums, target)
print(result)