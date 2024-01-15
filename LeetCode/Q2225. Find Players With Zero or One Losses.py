'''
Link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
Q2225. Find Players With Zero or One Losses

Approach:

I have tackled this problem maintaining frequency of win and loss for each matches and unique sorted players, 
for getting players who only wins we can remove loser from all players list, same way we can get player who lost once with their frequency contributions.

⏰ TC: O(N + K log K), where N & K is the number of matches and distinct winners or losers
🚀 SC: O(M), where M is the number of unique players in the matches.
'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losser_freq = Counter(x[1] for x in matches)
        winner_freq = Counter(x[0] for x in matches)

        winners = set(winner_freq) - set(losser_freq)
        lossers = {player for player, freq in losser_freq.items() if freq==1}

        return sorted(winners), sorted(lossers)
