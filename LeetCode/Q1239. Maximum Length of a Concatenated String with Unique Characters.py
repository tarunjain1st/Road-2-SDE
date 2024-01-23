'''
link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Q1239. Maximum Length of a Concatenated String with Unique Characters

👉 Approach:
In addressing the challenge of finding the maximum length of a concatenated string with unique characters, the approach utilizes backtracking. 
It explores different combinations of words, ensuring uniqueness through a set (unique_chars) and a helper function (is_unique). The code efficiently prunes invalid paths, maintaining linear space complexity.

📈 SC: O(n) - Linear space complexity as the set (unique_chars) stores unique characters.
⏰ TC: Exponential - Due to recursive backtracking, the time complexity exhibits an exponential growth.

Optimizations include pruning invalid paths and avoiding explicit subset generation for enhanced efficiency.
'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        string = set()

        def check_unique(string, s):
            c = Counter(string) + Counter(s)
            return False if max(c.values()) > 1 else True

        def check_subsets(index):
            if index == len(arr):
                return len(string)
            res = 0
            if check_unique(string, arr[index]):
                for c in arr[index]:
                    string.add(c)
                res = check_subsets(index + 1)
                for c in arr[index]:
                    string.remove(c)
            return max(res, check_subsets(index + 1)) 

        return check_subsets(0)
