
from flask import Flask,request
import sqlite3

app=Flask(__name__)
@app.get('/')
def game():
   return "hyy"
@app.post('/r')
def game1():
    con=sqlite3.Connection("C:/Users/trc/Desktop/back/db.db")
    cur=con.cursor()

    data=request.get_json()
    name=data["name"]
    rollno=data["rollno"]
    mark=data["mark"]
    students=(name,rollno,mark)
    cur.execute("create table student(name varchar(40),rollno varchar(10),mark int)")
    cur.execute("insert into student values(?,?,?)",students)
    con.commit()
    con.close()
    print(data)
    return "we got the data"
@app.patch("/upd")
def update():
    data =request.get_json();
    updates(data);
    return("updated");
def updates(data):
    con=sqlite3.Connection("C:/Users/trc/Desktop/back/db.db")
    cur=con.cursor()

    query =f'update students set name ="{data["name"]}"where rollmo ="{data["rollno"]}"';
    cur =con.cursor()
    cur.execute(query);
    con.commit();
app.run(debug=True)