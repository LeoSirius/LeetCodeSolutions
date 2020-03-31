### 思路1 

这道题问题描述不清。根据答案分析，answer rate应该是 (answer cnt) / (show cnt)

```sql
SELECT question_id AS survey_log
FROM survey_log
GROUP BY question_id
ORDER BY COUNT(answer_id) / COUNT(IF(action="show", 1, 0)) DESC
LIMIT 1;
```
