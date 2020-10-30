### 思路1 使用 内联结

```sql
SELECT e1.Name AS Employee
FROM Employee AS e1 JOIN Employee as e2
ON e1.ManagerID = e2.Id and e1.Salary > e2.Salary;
```