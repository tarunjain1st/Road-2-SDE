'''
Link: https://leetcode.com/problems/out-of-boundary-paths
Q576. Out of Boundary Paths

💡 Approach:
The code employs a Depth-First Search (DFS) approach to explore possible paths in a grid. At each step, it checks if the current move is within the allowed limit. 
If it exceeds, the path is abandoned; if the position is outside the grid, a valid path is found. 
The magic lies in the memoization technique, saving previously computed results to avoid redundant calculations.



📈 Time Complexity: O(m * n * maxMove),
The memoization ensures that we only compute unique subproblems, significantly reducing the overall time spent on calculations.

💾 Space Complexity:  O(m * n * maxMove).
The memoization table, represented by the dp array, stores only necessary information, preventing excessive memory usage. 
This makes the algorithm memory-efficient, especially when dealing with large grids or numerous possible moves.
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Define DFS function with parameters x, y, and moves
        def dfs(x, y, moves):
            # Base case: if moves exceed maxMove, return 0
            if moves > maxMove:
                return 0
            # Base case: if position is outside the grid, return 1 (path found)
            if (x < 0 or y < 0 or x >= m or y >= n):
                return 1
            # Memoization: return precalculated result if available
            if dp[x][y][moves] != -1:
                return dp[x][y][moves]
            
            res = 0
            # Explore all possible moves: right, left, up, and down
            for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                res += dfs(x+i, y+j, moves + 1)
                res = res % MOD
            
            # Save the result in the dp array for future reference
            dp[x][y][moves] = res
            return res
        
        MOD = 10**9 + 7
        dp = [[[-1] * (maxMove + 1) for x in range(n)] for y in range(m)]
        return dfs(startRow, startColumn, 0)

'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(x, y, moves):
            if moves > maxMove: return 0
            if (x<0 or y<0 or x>=m or y>=n): return 1
            res = 0
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                newX, newY = x+i, y+j
                res += dfs(newX, newY, moves+1)
                res = res % (10 ** 9 + 7)
            return res
        return dfs(startRow, startColumn, 0)
'''
