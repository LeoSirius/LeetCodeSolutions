### 思路1 直接用left join

```sql
SELECT FirstName, LastName, City, State
FROM Person Left JOIN Address
ON Person.PersonID = Address.PersonID
```