### 思路1

```sql
SELECT
ROUND(
(SELECT COUNT(*) FROM Delivery WHERE order_date=customer_pref_delivery_date) / 
(SELECT COUNT(*) FROM Delivery) * 100
, 2) AS immediate_percentage;
```
