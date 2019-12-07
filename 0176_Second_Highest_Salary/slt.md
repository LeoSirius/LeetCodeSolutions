### 思路1 使用max

注意这道题如果只有一个记录，需要是NULL。max在没有匹配结果的时候，会是NULL

```sql
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
```

如果保证输入的表中记录不止一个，则用limit最简单

```sql
# Write your MySQL query statement below
SELECT Salary as SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;
```