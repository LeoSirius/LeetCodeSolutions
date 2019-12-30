### 思路1

实际测试的数据中是有同一个学生选择同一个课程，的重复数据，所以需要用distinct。

```sql
SELECT class
FROM courses
GROUP BY class
HAVING COUNT( DISTINCT student) >= 5;
```
