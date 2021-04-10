--
-- @lc app=leetcode id=601 lang=mysql
--
-- [601] Human Traffic of Stadium
--

-- @lc code=start
# Write your MySQL query statement below

with idtable as (
    select id
    from Stadium
    where people >= 100
)

,idconsecutive as (
    select id
    from idtable
    where (id - 2 in (select id from idtable)
            and id - 1 in (select id from idtable))
        or (id + 1 in (select id from idtable)
            and id + 2 in (select id from idtable))
        or (id - 1 in (select id from idtable)
            and id + 1 in (select id from idtable))
)

select id, visit_date, people
from Stadium
where id in (select id from idconsecutive)

-- @lc code=end

