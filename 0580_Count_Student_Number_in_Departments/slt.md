### 思路1

left join + group by

注意

- 是department left join student。我们要找出dep的信息，无论有没有对应的stu。
- COUNT()中要是stu的信息，这样才是stu的数量。

```sql
SELECT d.dept_name, COUNT(s.student_id) AS student_number
FROM department d LEFT JOIN student s
ON d.dept_id=s.dept_id
GROUP BY d.dept_id
ORDER BY student_number DESC, d.dept_name;
```
