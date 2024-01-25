'''
link: https://leetcode.com/problems/longest-common-subsequence
Q1143. Longest Common Subsequence

🚀 Unlocking the Secrets of Longest Common Subsequence! 🚀
Ever wondered how computers find the longest common subsequence between two strings efficiently? Let's take a peek behind the scenes without diving into specific programming languages.

🔍 Approach: 
The algorithm employs a dynamic programming technique, breaking down the problem into simpler sub-problems. 
It's like solving a puzzle, where each piece contributes to the final picture

🛠️ How it Works: 
For two given strings, the algorithm recursively explores their characters. When a match is found, it increments the count and moves on to the next characters. 
If no match, it considers the maximum count without one of them. This process continues until it exhausts both strings.
In essence, this algorithm showcases the elegance of dynamic programming, efficiently solving a problem by breaking it down into manageable parts. 
Understanding the logic behind it provides a valuable glimpse into the world of algorithmic thinking.

⏰ TC: O(N * M),
The time complexity is O(n * m), where 'n' and 'm' are the lengths of the input strings. 
Memoization efficiently avoids redundant calculations, making the algorithm faster than naive approaches.

📈 SC: O(N * M),
To optimize memory usage, the algorithm utilizes a memoization table, storing previously computed results. 
This reduces redundant calculations and keeps space complexity at O(n * m), where 'n' and 'm' are the lengths of the input strings.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def findLCSLength(n, m):
            # Base case: if either string is empty, return 0
            if n < 0 or m < 0:
                return 0
            
            # If the result for the current state is already computed, return it
            if dp[n][m] != -1:
                return dp[n][m]
            
            # If the current characters equal, add 1 and move to the next state
            if text1[n] == text2[m]:
                dp[n][m] = findLCSLength(n-1, m-1) + 1
                
            # consider the maximum LCS skipping current characters from both strings
            else:
                dp[n][m] = max(findLCSLength(n, m-1), findLCSLength(n-1, m))
            
            return dp[n][m]


        len_text1, len_text2 = len(text1), len(text2)        
        # Initialize a memoization table with -1 values
        dp = [[-1] * len_text2 for _ in range(len_text1)]
        return findLCSLength(len_text1-1, len_text2-1)

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)         
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
'''
                    
