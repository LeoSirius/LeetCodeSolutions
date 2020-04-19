Mary is a teacher in a middle school and she has a table seat storing students'' names and their corresponding seat ids.

The column id is continuous increment.
 

Mary wants to change seats for the adjacent students.
 

Can you write a SQL query to output the result for Mary?
 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+


SELECT
    CASE
        WHEN MOD(id,2)!=0 AND id!=cnt THEN id+1
        WHEN MOD(id,2)!=0 AND id=cnt THEN id
        ELSE id-1
    END AS id
, student
FROM seat s JOIN (SELECT COUNT(*) AS cnt FROM seat) AS t
ORDER BY id;

For the sample input, the output is:


 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

