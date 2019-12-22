### 思路1

```sql
SELECT ROUND(
    IFNULL(
        (SELECT COUNT(DISTINCT requester_id, accepter_id) FROM request_accepted) / 
        (SELECT COUNT(DISTINCT sender_id, send_to_id) FROM friend_request)
    , 0), 2)
AS accept_rate;
```
