### 思路1

先找出有5个下属的经理的Id

```sql
SELECT ManagerId
FROM Employee
GROUP BY ManagerId
HAVING COUNT(ManagerId)>=5;
```

用WHERE IN子查询，找出经理的名字

```sql
SELECT Name
FROM Employee
WHERE Id IN (
SELECT ManagerId
FROM Employee
GROUP BY ManagerId
HAVING COUNT(DISTINCT Id)>=5);
```

或联结原表，找出经理的名字

```sql
SELECT e1.Name
FROM Employee e1 JOIN
(
SELECT ManagerId
FROM Employee
GROUP BY ManagerId
HAVING COUNT(ManagerId)>=5) AS t
ON e1.Id=t.ManagerId;
```
