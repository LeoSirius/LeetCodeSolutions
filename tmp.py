
import json

with open('t.json') as f:
    rows = json.loads(f.read())['rows']
    print(len(rows))
    for row in rows:
        if 'commerceLocalTerrassePlace' in row.keys():
            if row['commerceLocalTerrassePlace']:
                print(row['commerceLocalTerrassePlace'])