#https://leetcode.com/problems/big-countries/
#595
/* Write your T-SQL query statement below */
SELECT name, population, area
FROM World
WHERE area>3000000
OR population>25000000
