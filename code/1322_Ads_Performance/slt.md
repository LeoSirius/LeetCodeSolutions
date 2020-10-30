### 思路1

注意最后除了ctr降序，还需要ad_id升序。

```sql
SELECT ad_id,
IFNULL(
    ROUND(
        SUM(action="Clicked") / (SUM(action="Clicked") +  SUM(action="Viewed")) * 100, 
        2)
, 0)
AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id;
```
