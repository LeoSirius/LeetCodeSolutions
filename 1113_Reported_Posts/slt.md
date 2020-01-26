### 思路1

主要注意post_id存在duplicate, COUNT的时候注意去重

```sql
SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE action='report' AND extra IS NOT NULL AND action_date='2019-07-04'
GROUP BY extra;
```
