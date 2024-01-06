'''Question link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
the approach used in the provided code is a greedy algorithm with a priority queue (min-heap). Here's a summary of the approach:

1. Sort the jobs based on their start times, ensuring they are in ascending order.
2. Initialize an empty min-heap (priority queue) to keep track of the end times and maximum profits of the jobs.
3. Iterate through the sorted jobs, and for each job:
  * Pop elements from the min-heap where the end time is less than or equal to the current job's start time.
  * Update the maximum profit by considering the maximum profit obtained so far and the profit of the current job.
  * Push the current job's end time and the updated maximum profit into the min-heap.
4. The final result is the maximum profit obtained after considering all the jobs.

This approach efficiently handles the non-overlapping constraint of jobs and ensures that the algorithm considers the optimal combination of jobs to maximize the total profit.
'''

from heapq import heapify, heappop, heappush
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        min_heap=[]
        heapify(min_heap)
        max_profit=0
        current_end=0

        for start, end, profit in jobs:
            while min_heap and min_heap[0][0] <= start:
                _, maxSoFar =  heappop(min_heap)
                max_profit = max(max_profit, maxSoFar)
            heappush(min_heap, (end, max_profit + profit))
            current_end = max(current_end, end)

        while min_heap:
            _, maxSoFar =  heappop(min_heap)
            max_profit = max(max_profit, maxSoFar)
        
        return max_profit


'''
from heapq import heapify, heappop, heappush
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        dp={}
        
        def checkProfit(i):
            if i==len(jobs): return 0
            if i in dp: return dp[i]
            res = checkProfit(i+1)
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))
            dp[i] = res = max(res, jobs[i][2] + checkProfit(j))
            return res

        return checkProfit(0)
'''
