CREATE TABLE IF NOT EXISTS student (student_id INT,student_name VARCHAR(45), gender VARCHAR(6), dept_id INT);
CREATE TABLE IF NOT EXISTS department (dept_id INT, dept_name VARCHAR(255));
Truncate table student;
insert into student (student_id, student_name, gender, dept_id) values ('1', 'Jack', 'M', '1');
insert into student (student_id, student_name, gender, dept_id) values ('2', 'Jane', 'F', '1');
insert into student (student_id, student_name, gender, dept_id) values ('3', 'Mark', 'M', '2');
Truncate table department;
insert into department (dept_id, dept_name) values ('1', 'Engineering');
insert into department (dept_id, dept_name) values ('2', 'Science');
insert into department (dept_id, dept_name) values ('3', 'Law');

Here is an example input:
student table:

| student_id | student_name | gender | dept_id |
|------------|--------------|--------|---------|
| 1          | Jack         | M      | 1       |
| 2          | Jane         | F      | 1       |
| 3          | Mark         | M      | 2       |
department table:

| dept_id | dept_name   |
|---------|-------------|
| 1       | Engineering |
| 2       | Science     |
| 3       | Law         |
The Output should be:

| dept_name   | student_number |
|-------------|----------------|
| Engineering | 2              |
| Science     | 1              |
| Law         | 0              |


left join + group by
SELECT d.dept_name, COUNT(s.student_id) AS student_number
FROM department d LEFT JOIN student s
ON d.dept_id=s.dept_id
GROUP BY d.dept_id
ORDER BY student_number DESC, d.dept_name;