Write a SQL query to find the highest grade with its
 corresponding course for each student. In case of a tie,
  you should find the course with the smallest course_id.
   The output must be sorted by increasing student_id.

The query result format is in the following example:

Enrollments table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+

选出每个学生的最大分数

SELECT student_id, course_id, MAX(grade)
FROM Enrollments
GROUP BY student_id;

再JOIN两表

SELECT e.student_id, MIN(e.course_id) as course_id, e.grade
FROM Enrollments e JOIN (
    SELECT student_id, course_id, MAX(grade) AS max_grade
    FROM Enrollments
    GROUP BY student_id
) AS t
ON e.student_id=t.student_id AND e.grade=t.max_grade
GROUP BY e.student_id
ORDER BY e.student_id;




Result table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+


Create table If Not Exists Enrollments (student_id int, course_id int, grade int);
Truncate table Enrollments;
insert into Enrollments (student_id, course_id, grade) values ('2', '2', '95');
insert into Enrollments (student_id, course_id, grade) values ('2', '3', '95');
insert into Enrollments (student_id, course_id, grade) values ('1', '1', '90');
insert into Enrollments (student_id, course_id, grade) values ('1', '2', '99');
insert into Enrollments (student_id, course_id, grade) values ('3', '1', '80');
insert into Enrollments (student_id, course_id, grade) values ('3', '2', '75');
insert into Enrollments (student_id, course_id, grade) values ('3', '3', '82');