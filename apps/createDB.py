
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");
c = conn.cursor()
#创建数据表
c.execute('''CREATE TABLE WEBSHELL
       (ID INT PRIMARY KEY     NOT NULL,
       ADDRESS           TEXT    NOT NULL,
       PASSWORD            TEXT     NOT NULL);
''')
#插入测试数据
c.execute("INSERT INTO WEBSHELL (ID,ADDRESS,PASSWORD) \
      VALUES (2, 'http://39.108.36.103:9999/upload/tinmin.php','tinmin')");

print("Table created successfully");
conn.commit()
conn.close()