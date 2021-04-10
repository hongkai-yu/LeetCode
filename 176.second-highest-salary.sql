--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below

SELECT (CASE WHEN (SELECT count(distinct Salary) FROM Employee) < 2 THEN Null
        ELSE (SELECT Salary
             FROM Employee
             ORDER BY Salary DESC
             LIMIT 1 OFFSET 1 
             )
        END) SecondHighestSalary


-- @lc code=end 
