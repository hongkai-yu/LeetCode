#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
from operator import add
from functools import reduce


class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        for name in path.split('/'):
            if name in ('', '.'):
                pass
            elif name == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(name)
        return '/' + '/'.join(stack)
        

        # if path[-1] != '/':
        #     path += '/'

        # folders = []

        # name = ''
        # for c in path:
        #     if c != '/':
        #         name += c
        #     else:
        #         if name == '.':
        #             pass
        #         elif name == '..':
        #             if folders:
        #                 folders.pop()
        #         elif name == '':
        #             pass
        #         else:
        #             folders.append(name)
        #         name = ''


        # if not folders:
        #     return '/'
        # else:
        #     return reduce(add, map(lambda f: '/' + f, folders))
        #     # res = ''
        #     # for f in folders:
        #     #     res += '/' + f
        #     # return res
        
# @lc code=end

if __name__ == '__main__':
    path = '/home//foo/'
    print(Solution().simplifyPath(path))


