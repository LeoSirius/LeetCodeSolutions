### 思路1

找到所有是spam的report

```sql
SELECT *
FROM Actions
WHERE extra='spam';
```

LEFT JOIN 关联两表

```sql
SELECT *
FROM (
    SELECT *
    FROM Actions
    WHERE extra='spam'
) AS t LEFT JOIN Removals r
ON t.post_id=r.post_id;
```

找到按日期分组每组年内部的比例。注意两个表都要去重

```sql
SELECT 
    COUNT(DISTINCT r.post_id) / COUNT(DISTINCT t.post_id) AS daily_percent
FROM (
    SELECT *
    FROM Actions
    WHERE extra='spam'
) AS t LEFT JOIN Removals r
ON t.post_id=r.post_id
GROUP BY action_date;
```

```sql
SELECT ROUND(AVG(daily_percent)*100, 2) AS average_daily_percent
FROM (
    SELECT 
        COUNT(DISTINCT r.post_id) / COUNT(DISTINCT t.post_id) AS daily_percent
    FROM (
        SELECT *
        FROM Actions
        WHERE extra='spam'
    ) AS t LEFT JOIN Removals r
    ON t.post_id=r.post_id
    GROUP BY action_date
) AS t;
```
