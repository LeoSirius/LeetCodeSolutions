### 思路1

我们有数据

```sql
+----+--------+-----------+
| id | sub_id | parent_id |
+----+--------+-----------+
|  1 |      1 |      NULL |
|  2 |      2 |      NULL |
|  3 |      1 |      NULL |
|  4 |     12 |      NULL |
|  5 |      3 |         1 |
|  6 |      5 |         2 |
|  7 |      3 |         1 |
|  8 |      4 |         1 |
|  9 |      9 |         1 |
| 10 |     10 |         2 |
| 11 |      6 |         7 |
+----+--------+-----------+
```

```sql
MariaDB [test]> SELECT DISTINCT a.sub_id AS post_id, b.sub_id AS sub_id
    -> FROM Submissions a LEFT JOIN Submissions b
    -> ON a.sub_id=b.parent_id
    -> WHERE a.parent_id IS NULL;
+---------+--------+
| post_id | sub_id |
+---------+--------+
|       1 |      3 |
|       2 |      5 |
|       1 |      4 |
|       1 |      9 |
|       2 |     10 |
|      12 |   NULL |
+---------+--------+
```

注意这里一定要用left join，不然12就没有了。最后再用group。注意count一定要是COUNT(sub_id)，不然12的结果就是1，但正确的应该是0。

```sql
SELECT post_id, COUNT(sub_id) AS number_of_comments
FROM (
SELECT DISTINCT a.sub_id AS post_id, b.sub_id AS sub_id
FROM Submissions a LEFT JOIN Submissions b
ON a.sub_id=b.parent_id
WHERE a.parent_id IS NULL
) AS t
GROUP BY post_id;
```