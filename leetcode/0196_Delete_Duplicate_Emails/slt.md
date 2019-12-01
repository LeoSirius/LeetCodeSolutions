### 思路1

使用内联结

```sql
DELETE p1
FROM Person p1 INNER JOIN Person p1
ON p1.Email = p2.Email AND p1.ID > p2.I
```