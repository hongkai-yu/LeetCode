--
-- @lc app=leetcode id=177 lang=mysql
--
-- [177] Nth Highest Salary
--

-- @lc code=start
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary
      from Employee e1
      where N-1 = (select count(distinct Salary)
                    from Employee e2
                    where e1.Salary < e2.Salary)
      
  );
END
-- @lc code=end

