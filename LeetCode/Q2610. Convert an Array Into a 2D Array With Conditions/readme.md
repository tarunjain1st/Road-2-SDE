# [Question](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions)

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

 

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
  
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= nums.length

# Intuition
We need to create 2D array of unique combinations, where every element of subarray counts exactly once from total number in array list, for doing this either we can use counter of each number with freqency or group of available numbers.

I have tried 3 different ways to slove this list in there order of runtime (increasingly).

* Create groups of element, by picking if not already exits in current group, every element will get placed in a subgroup exactly onces.
* Create frequency map and N subarrays, where N is most common element in input list and further distribute elements taking frequency count as index value in subarray decrementally.
* Create frequency map of elements, while we have elements in map, create subarray of keys by iterating over keys in map till frequency of key greater then zero. append subarray of keys as subresult in 2D array of result. 

<!-- Describe your first thoughts on how to solve this problem. -->

## Approach-1
Create groups of element, by picking if not already exits in current group, every element will get placed in a subgroup exactly onces.
<!-- Describe your approach to solving the problem. -->

## Complexity
- Time complexity:
  * The outer loop iterates through each element in the input list nums, which takes O(n), where n is the length of nums.
  * The inner loop, for each element, iterates through the existing groups in groups. In the worst case, when no match is found, it will iterate through all existing groups, taking O(k), where k is the number of groups.
  * Therefore, the overall time complexity is `O(n * k)`, where n is the length of nums and k is the number of groups in groups.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  * In the worst case, each element in nums forms a new group in groups. 
  * Additionally, each set within groups can contain unique elements, leading to a space complexity within the sets of O(n).
  * Therefore, the worst-case space complexity is `O(n)`, where n is the length of nums.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```Python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        groups=[]
        for num in nums:
            in_group=False
            for group in groups:
                if num not in group:
                    group.add(num)
                    in_group=True
                    break
            if in_group==False:
                groups.append({num})
        return groups          
```

## Approach-2
Create frequency map and N subarrays, where N is most common element in input list and further distribute elements taking frequency count as index value in subarray decrementally.
<!-- Describe your approach to solving the problem. -->

## Complexity
- Time complexity:
  * Constructing the Counter (numFreq) from the input list takes O(n), where n is the length of the input list nums.
  * Initializing the result list with empty sublists takes O(max_frequency), where max_frequency is the maximum frequency of any element in nums.
  * The loop iterates through each element in nums and updates the result list. The worst-case scenario is that each element is added to its respective sublist, taking O(n) in the worst case.
  * Therefore, the overall time complexity is `O(n + max_frequency)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  * The space complexity is dominated by the numFreq Counter, which requires O(n) space to store the frequency of each element in the input list.
  * The result list contains max_frequency sublists, and each sublist stores the occurrences of a unique element. 
  * Therefore, the space complexity for result is ``O(max_frequency)``.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```Python
from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numFreq =  Counter(nums)
        keys=list(numFreq.keys())
        most_common = numFreq.most_common()[0][1]
        result = [list() for x in range(most_common)]
        for num in nums:
            if freq:= numFreq.get(num):
                result[freq-1].append(num)
                numFreq[num]-=1
        return result
```

## Approach-3
Create frequency map of elements, while we have elements in map, create subarray of keys by iterating over keys in map till frequency of key greater then zero. append subarray of keys as subresult in 2D array of result.
<!-- Describe your approach to solving the problem. -->

## Complexity
- Time complexity:
  * Constructing the Counter (numFreq) from the input list takes O(n), where n is the length of the input list nums.
  * The outer while loop continues until numFreq is empty, and in each iteration, it iterates through all keys in the keys list. In the worst case, it goes through each unique element in nums.
  * The inner loop, for each key, checks and appends to the temp list, which takes O(1) on average. However, in the worst case, it could be O(n) if every element is unique.
  * Therefore, the overall time complexity is `O(n^2)` in the worst case.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  * The numFreq Counter requires O(n) space to store the frequency of each element in the input list.
  * The keys list is a list of unique elements, so it also requires O(n) space.
  * The result list stores the sublists, and in the worst case, it might contain n/2 sublists (if each element in nums is unique). 
  * Each sublist may contain unique elements, so in the worst case, the total space is O(n).
  * Therefore, the overall space complexity is `O(n)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```Python
from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numFreq =  Counter(nums)
        keys=list(numFreq.keys())
        result=[]
        while numFreq:
            temp=[]
            for key in keys:
                if numFreq.get(key):
                    temp.append(key)
                    numFreq[key]-=1
                    if numFreq.get(key) == 0:
                        numFreq.pop(key)
            result.append(temp)
        return result        
```
