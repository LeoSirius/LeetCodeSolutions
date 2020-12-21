### 思路1

注意这里的group by用到了两个字段

s1和s2是笛卡尔积。第二个连接用left join，因为有0的情况

```sql
SELECT s1.student_id, s1.student_name, s2.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students s1 JOIN Subjects s2 LEFT JOIN Examinations e
ON s1.student_id=e.student_id AND s2.subject_name=e.subject_name
GROUP BY s1.student_id, s2.subject_name;
```
