#Question link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

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
