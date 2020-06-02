import requests

headers = {'Authorization': 'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTEzMzkzMDIsImR0YWJsZV91dWlkIjoiNWNmMjY4Yzk1M2MzNGQyYzgyZTI4OWU2MjM4Yjg5ZTciLCJ1c2VybmFtZSI6ImY5MWE5YzgyMGIyODQyNDliM2JiMzM5NmRjNjViZDY0QGF1dGgubG9jYWwiLCJwZXJtaXNzaW9uIjoicncifQ.qcNe0zIckDdEjc9omN2k1IHF7_GDKCdKoHNxCmnu7NI'}
url = 'http://127.0.0.1:5000/api/v1/dtables/5cf268c953c34d2c82e289e6238b89e7/append-csv/'
data = {
    'table_name': 'Book1',
}
# f = open('/Users/leo/Downloads/Book1.csv')
# content = f.read()
# print('content = {}'.format(content))
files = {
    'csv_file': '/Users/leo/Downloads/Book1.csv'
}

print('files = {}'.format(files))

try:
    res = requests.post(url, headers=headers, data=data, files=files)
except Exception as e:
    print("E = {}".format(e))

print(res.status_code)
print(res.text)
# f.close()