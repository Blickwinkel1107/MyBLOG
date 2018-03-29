from django.db import connection

c = connection.cursor()
c.execute('select * from articles')
vec = c.fetchall()

print(vec)