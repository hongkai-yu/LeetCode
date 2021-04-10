#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        parent = folder[0] + '/'
        res = [folder[0]]

        for f in folder[1:]:
            if parent == f[:len(parent)]:
                pass
            else:
                res.append(f)
                parent = f + '/'
        return res

            
        
# @lc code=end

