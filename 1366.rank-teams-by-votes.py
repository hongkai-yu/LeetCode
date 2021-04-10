#
# @lc app=leetcode id=1366 lang=python3
#
# [1366] Rank Teams by Votes
#

# @lc code=start
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        N = len(votes[0])
        voteCounter = defaultdict(lambda: [0] * N)

        for vote in votes:
            for pos, team in enumerate(vote):
                voteCounter[team][pos] -= 1

        return ''.join(map(lambda x: x[-1],
                           sorted(tuple(votes) + (team,)
                           for team, votes in voteCounter.items())))
        
# @lc code=end

