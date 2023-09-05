#STUDENT MANAGEMENT SYSTEM
import sqlite3

conn=sqlite3.connect('test1.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS STUDENT
            (ID INT PRIMARY KEY  NOT NULL,
            NAME  TEXT NOT NULL,
            BRANCH  TEXT  NOT NULL,
            SECTION TEXT NOT NULL,
            SEM INT NOT NULL);''')

print("Table STUDENT created successfully")

conn.execute("INSERT INTO STUDENT (ID,NAME,BRANCH,SECTION,SEM)\
         VALUES(1,'Anmol Muskan','CCE','A',5)");

conn.execute("INSERT INTO STUDENT (ID,NAME,BRANCH,SECTION,SEM)\
         VALUES(2,'Ayush Anand','CSE','A',8)");

conn.execute("INSERT INTO STUDENT (ID,NAME,BRANCH,SECTION,SEM)\
         VALUES(3,'Shivapriya S','EEE','B',5)");

conn.execute("INSERT INTO STUDENT (ID,NAME,BRANCH,SECTION,SEM)\
         VALUES(4,'Sakshi Sinha','CSE','A',8)");

conn.execute("INSERT INTO STUDENT (ID,NAME,BRANCH,SECTION,SEM)\
         VALUES(5,'Riyaa Ganla','IT','C',5)");

conn.execute("INSERT INTO STUDENT (ID,NAME,BRANCH,SECTION,SEM)\
         VALUES(6,'Dwight Schrute','EEE','A',1)");

conn.execute("INSERT INTO STUDENT (ID,NAME,BRANCH,SECTION,SEM)\
         VALUES(7,'Jim Halpert','CCE','B',3)");

print("After insert")
cursor=conn.execute("SELECT id,name,branch,section,sem from STUDENT")
for row in cursor:
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("BRANCH = ",row[2])
    print("SECTION = ",row[3])
    print("SEM = ",row[4],"\n")


conn.execute('''CREATE TABLE IF NOT EXISTS COURSE
           (CID INT PRIMARY KEY NOT NULL,
           CNAME TEXT NOT NULL,
           DEPT  TEXT NOT NULL,
           CREDITS INT NOT NULL);''')

print("Table COURSE created successfully")

conn.execute("INSERT INTO COURSE (CID,CNAME,DEPT,CREDITS)\
         VALUES(1,'DS',ICT,4)");
conn.execute("INSERT INTO COURSE (CID,CNAME,DEPT,CREDITS)\
         VALUES(2,'OOP',ICT,4)");
conn.execute("INSERT INTO COURSE (CID,CNAME,DEPT,CREDITS)\
         VALUES(3,'DS',CSE,4)");
conn.execute("INSERT INTO COURSE (CID,CNAME,DEPT,CREDITS)\
         VALUES(4,'DS',CSE,4)");
conn.execute("INSERT INTO COURSE (CID,CNAME,DEPT,CREDITS)\
         VALUES(5,'LCT',EEE,3)");
conn.execute("INSERT INTO COURSE (CID,CNAME,DEPT,CREDITS)\
         VALUES(6,'DMPA',ICT,3)");

