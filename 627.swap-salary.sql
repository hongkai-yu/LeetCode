--
-- @lc app=leetcode id=627 lang=mysql
--
-- [627] Swap Salary
--

-- @lc code=start
# Write your MySQL query statement below

UPDATE salary SET sex = (
    CASE WHEN sex = 'f' THEN 'm'
    ELSE 'f'
    END
);

-- @lc code=end

