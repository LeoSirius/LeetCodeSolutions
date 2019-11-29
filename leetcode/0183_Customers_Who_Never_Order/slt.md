### 思路1 left join 并用 is null过滤

```sql
SELECT Name AS Customers
FROM Customers LEFT JOIN Orders
ON Customers.Id=Orders.CustomerId
WHERE Orders.CustomerId IS NULL;
```
