--
-- @lc app=leetcode id=626 lang=mysql
--
-- [626] Exchange Seats
--

-- @lc code=start
# Write your MySQL query statement below
SELECT id, IFNULL(
    CASE WHEN MOD(id, 2) = 1 THEN LEAD(student, 1) OVER(ORDER BY id)
    ELSE LAG(student, 1) OVER(ORDER BY id) END,
    student) student
FROM seat

-- @lc code=end

