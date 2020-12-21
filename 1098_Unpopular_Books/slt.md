### 思路1

1 LEFT JOIN 两表，并过滤掉一月以内的书，可能存在书没有order的情况

```sql
SELECT *
FROM Books b LEFT JOIN Orders o
ON b.book_id=o.book_id
WHERE 30<DATEDIFF('2019-06-23', b.available_from);
```

2. 分组，并用 IFNULL + NULL + IF  来获得10本以下的数

```sql
SELECT b.book_id, b.name
FROM Books b LEFT JOIN Orders o
ON b.book_id=o.book_id
WHERE 30<DATEDIFF('2019-06-23', b.available_from)
GROUP BY b.book_id
HAVING
  SUM(
    IF(DATEDIFF('2019-06-23', o.dispatch_date)<=365, quantity, 0)
  ) < 10;
```
