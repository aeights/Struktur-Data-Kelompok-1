import sqlite3

connect=sqlite3.connect("D:/Data/[Informatika]/Semester 3/Struktur Data/Struktur-Data-Kelompok-1/account.db")
getdata=connect.cursor()
getdata.execute("INSERT INTO akun values('afif1','123')")
data=getdata.execute("SELECT * FROM akun")
connect.commit()
row=data.fetchall()
print(row)