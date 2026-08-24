import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''create table if not exists students
                  (id integer primary key autoincrement,
                    name text not null,
                    age integer not null,
                    grade text not null)''')


cursor.execute("""insert into students (name, age, grade) values
 ("Alice", 14, "8th")
""")
cursor.execute("""select * from students""")

cursor.execute("""
delete from students where id = 5
""")

cursor.execute("""select * from students""")

results = cursor.fetchall()
print(results)


conn.commit()
conn.close()