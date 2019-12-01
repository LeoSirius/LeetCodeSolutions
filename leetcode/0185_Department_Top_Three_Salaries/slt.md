### 思路1

先用内联结构建一个(机构名, 员工名, 工资)的表。再利用子查询，同部门工资大于的数量小于3，自然就是这个部门的前三。卧槽。

```sql
SELECT d.name as Department, e.name AS Employee, e.salary as Salary
FROM Employee as e inner join Department as d
ON e.DepartmentId=d.Id
WHERE (
  SELECT count(distinct Salary)
  FROM Employee
  WHERE Salary > e.Salary AND DepartmentId=e.DepartmentId
)<3
ORDER BY e.DepartmentId, e.Salary DESC;
```
