### 思路1

用左联结

```sql
SELECT Employee.name, Bonus.bonus
FROM Employee LEFT JOIN Bonus ON Employee.empId=Bonus.empId
WHERE bonus < 1000 or bonus IS NULL;
```