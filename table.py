import sqlite3
con = sqlite3.connect('sample.db')
cur=con.cursor();
cur.execute("""create table student(id int,name varchar(30), dept varchar(50))""");
con.commit();
con.close();