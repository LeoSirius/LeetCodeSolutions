Table: Candidate

+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+  
Table: Vote

+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id is the auto-increment primary key,
CandidateId is the id appeared in Candidate table.
Write a sql to find the name of the winning candidate, the above example will return the winner B.

+------+
| Name |
+------+
| B    |
+------+
Notes:

You may assume there is no tie, in other words there will be only one winning candidate.

SELECT COUNT(DISTINCT v.CandidateId)
FROM Candidate c JOIN Vote v
ON c.id=v.CandidateId;

获胜者是 Vote 表中出现最多次的 CandidateId。因此可以先按照 CandidateId 分组，
然后按照每个分组的计数给分组排序，使用 limit 1 取第一名即可。获得第一名的 CandidateId 之后，
与 Candidate 表连接即可取得获胜者的名字。



SELECT CandidateId
FROM Vote
GROUP BY CandidateId
ORDER BY COUNT(*) DESC LIMIT 1;

SELECT c.Name
FROM Candidate c JOIN
(
    SELECT CandidateId
    FROM Vote
    GROUP BY CandidateId
    ORDER BY COUNT(*) DESC LIMIT 1
) AS t ON c.id=t.CandidateId;



Create table If Not Exists Candidate (id int, Name varchar(255));
Create table If Not Exists Vote (id int, CandidateId int);
Truncate table Candidate;
insert into Candidate (id, Name) values ('1', 'A');
insert into Candidate (id, Name) values ('2', 'B');
insert into Candidate (id, Name) values ('3', 'C');
insert into Candidate (id, Name) values ('4', 'D');
insert into Candidate (id, Name) values ('5', 'E');
Truncate table Vote;
insert into Vote (id, CandidateId) values ('1', '2');
insert into Vote (id, CandidateId) values ('2', '4');
insert into Vote (id, CandidateId) values ('3', '3');
insert into Vote (id, CandidateId) values ('4', '2');
insert into Vote (id, CandidateId) values ('5', '5');

