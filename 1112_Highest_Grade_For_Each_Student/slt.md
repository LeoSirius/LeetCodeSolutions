### 思路1

选出每个学生的最大分数

```sql
SELECT student_id, course_id, MAX(grade)
FROM Enrollments
GROUP BY student_id;
```

再JOIN两表

```sql
SELECT e.student_id, MIN(e.course_id) as course_id, e.grade
FROM Enrollments e JOIN (
    SELECT student_id, course_id, MAX(grade) AS max_grade
    FROM Enrollments
    GROUP BY student_id
) AS t
ON e.student_id=t.student_id AND e.grade=t.max_grade
GROUP BY e.student_id
ORDER BY e.student_id;
```
