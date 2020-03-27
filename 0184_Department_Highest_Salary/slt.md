### 思路1 

利用子查询先找出每个部门的最高工资，再联结两个表查询

```sql
SELECT MAX(e.Salary), e.DepartmentId
FROM Employee e
GROUP BY e.DepartmentId;
```

```sql
SELECT
d.Name AS Department,
e.Name AS Employee,
e.Salary
FROM Employee e JOIN Department d
ON e.DepartmentId=d.Id
WHERE (e.Salary, e.DepartmentId) IN (
    SELECT MAX(e.Salary), e.DepartmentId
    FROM Employee e
    GROUP BY e.DepartmentId
);
```
