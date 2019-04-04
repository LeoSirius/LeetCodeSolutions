题目描述

```

```

sql

```sql
SELECT f.title, f.description FROM film f WHERE f.film_id IN
(SELECT fc.film_id FROM film_category fc WHERE fc.category_id IN
(SELECT c.category_id FROM category c WHERE c.name = 'Action'))
```

