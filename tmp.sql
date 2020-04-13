In facebook, there is a follow table with two columns: followee, follower.

Please write a sql query to get the amount of each follower’s follower if he/she has one.

For example:

+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+


select followee as follower, count(distinct follower) as num
from
follow
where followee in (select distinct follower from follow)
group by followee;

select 
f1.follower,count(distinct(f2.follower)) num
from
follow f1,follow f2
where
f1.follower=f2.followee
group by
f1.follower


这道题要找出follower的follower数量

先联结两表，这样f2的followee是f1中的follower，

SELECT *
FROM follow f1 JOIN follow f2
ON f1.follower=f2.followee;

然后再找出f2的followee有多少follower就可以了。

SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM follow f1 JOIN follow f2
ON f1.follower=f2.followee
GROUP BY f2.followee;



should output:
+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+


Explaination:
Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is 
E. A does not exist in follower list.


Create table If Not Exists follow (followee varchar(255), follower varchar(255));
Truncate table follow;
insert into follow (followee, follower) values ('A', 'B');
insert into follow (followee, follower) values ('B', 'C');
insert into follow (followee, follower) values ('B', 'D');
insert into follow (followee, follower) values ('D', 'E');
 

 

Note:
Followee would not follow himself/herself in all cases.
Please display the result in follower's alphabet order.
 
