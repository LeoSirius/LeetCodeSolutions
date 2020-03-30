### 思路1 

首先在Vote表中用GROUP BY选出最多的人的ID

```sql
    SELECT CandidateId
    FROM Vote
    GROUP BY CandidateId
    ORDER BY COUNT(*) DESC LIMIT 1
```

再用Cadidate表和这个表联结

```sql
SELECT c.Name
FROM Candidate c JOIN
(
    SELECT CandidateId
    FROM Vote
    GROUP BY CandidateId
    ORDER BY COUNT(*) DESC LIMIT 1
) AS t ON c.id=t.CandidateId;
```
