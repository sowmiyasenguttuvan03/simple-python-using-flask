import sqlite3

con = sqlite3.connect('sample.db', check_same_thread= False)

def getall():
    cur= con.cursor();
    cur.execute("select * from student")
    data=cur.fetchall();
    con.commit();
    return(data);

def Insert(data):
    print(data)
    cur=con.cursor();

    if type(data)==list:
        cur.executemany(f'insert into student values(:id, :name, :dept)',data);
    
    else:
        cur.execute(f'insert into student values("{data["id"]}","{data["name"]}","{data["dept"]}")')
        con.commit();

def upd(data):
    cur=con.cursor();
    cur.execute(f'update student set name="{data["name"]}", dept="{data["dept"]}" where id={data["id"]}');
    con.commit();

def delete(id):
    cur=con.cursor();
    cur.execute(f'delete from student where id={id}');
    con.commit();
