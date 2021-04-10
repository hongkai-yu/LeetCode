#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        lo, hi = 0, len(people) - 1

        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
        return len(people) - 1 - hi
            
        # boats = [None for _ in range(len(people))]
        # people.sort(reverse = True)

        # for person in people:
        #     for i in range(len(boats)):
        #         if not boats[i]:
        #             boats[i] = person
        #             break
        #         elif boats[i] == -1:
        #             pass
        #         elif boats[i] + person <= limit:
        #             boats[i] = -1
        #             break
        #         else:
        #             pass
        # # print(boats)
        # return len([boat for boat in boats if boat])
# @lc code=end

