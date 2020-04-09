Create table If Not Exists survey_log (id int, action varchar(255), question_id int, answer_id int, q_num int, timestamp int);
Truncate table survey_log;
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '285', NULL, '1', '123');
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'answer', '285', '124124', '1', '124');
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '369', NULL, '2', '125');
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'skip', '369', NULL, '2', '126');

+------+-----------+--------------+------------+-----------+------------+
| id   | action    | question_id  | answer_id  | q_num     | timestamp  |
+------+-----------+--------------+------------+-----------+------------+
| 5    | show      | 285          | null       | 1         | 123        |
| 5    | answer    | 285          | 124124     | 1         | 124        |
| 5    | show      | 369          | null       | 2         | 125        |
| 5    | skip      | 369          | null       | 2         | 126        |
+------+-----------+--------------+------------+-----------+------------+
Output:
+-------------+
| survey_log  |
+-------------+
|    285      |
+-------------+

SELECT question_id AS survey_log
FROM survey_log
GROUP BY question_id
ORDER BY COUNT(answer_id) / COUNT(IF(action='show', 1, 0)) DESC
LIMIT 1;