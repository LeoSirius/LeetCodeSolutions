### 思路1

主题实际测试的数据中是由同一个学生选择同一个课程是由重复数据的，所以需要用distinct。

```sql
SELECT class
FROM courses
GROUP BY class
HAVING COUNT( DISTINCT student) >= 5;
```
