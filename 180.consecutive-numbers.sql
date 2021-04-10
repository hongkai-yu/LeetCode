--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--

-- @lc code=start
# Write your MySQL query statement below

select distinct Num ConsecutiveNums
from (
    select Id
        ,Num
        ,Lead(Num, 1) over(order by Id) Nxt1
        ,Lead(Num, 2) over(order by Id) Nxt2
    from Logs
) t
where Num = Nxt1 and Nxt1 = Nxt2

/* select distinct l1.Num as ConsecutiveNums
from Logs l1 
    inner join (select (Id + 1) as Id2, Num from Logs) l2
    on l1.Id = l2.Id2 and l1.Num = l2.Num
    inner join (select (Id + 2) as Id3, Num from Logs) l3
    on l1.Id = l3.Id3 and l1.Num = l3.Num */


-- @lc code=end

