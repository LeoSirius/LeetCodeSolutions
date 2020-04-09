### 思路1

```sql
SELECT c.Name
FROM Candidate c JOIN Vote v
ON c.id=v.CandidateId
GROUP BY v.CandidateId
ORDER BY COUNT(v.CandidateId) DESC
LIMIT 1;
```

### 思路2

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
