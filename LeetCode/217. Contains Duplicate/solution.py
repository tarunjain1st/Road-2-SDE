'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        isTrue = False
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i] += 1
        print(hashmap)
        for i in hashmap:
            if hashmap[i]>1:
                isTrue = True
        return isTrue
'''
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        return any(x > 1 for x in hashmap.values())


nums = [1,2,3,4]
solve = Solution()
result = solve.containsDuplicate(nums)
print(result)