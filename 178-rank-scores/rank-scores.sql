-- Write your PostgreSQL query statement below
Select s1.score,
       (Select count(distinct s2.score)
       from Scores s2
       where s2.score >= s1.score) as rank
from Scores s1
order by s1.score DESC;