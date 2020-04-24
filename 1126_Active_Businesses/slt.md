### 思路1

找到每个event_type的平均

```sql
SELECT event_type, AVG(occurences) AS avg_occurences
FROM Events
GROUP BY event_type;
```

```sql
SELECT e.business_id
FROM Events e JOIN (
    SELECT event_type, AVG(occurences) AS avg_occurences
    FROM Events
    GROUP BY event_type
) t
ON e.event_type=t.event_type
WHERE e.occurences>t.avg_occurences
GROUP BY e.business_id
HAVING COUNT(e.business_id)>1;
```
