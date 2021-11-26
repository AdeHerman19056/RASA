import sqlite3; import re; 
con = sqlite3.connect('/home/ade/Dokumen/Old/NLP/bin/kode');

nim = re.search("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", "09021281924056")[0];
print("Fakultas:\t" + str(con.execute("select nama from fakultas where kode = " + str(nim[0:2]) + ";").fetchall()[0][0]));
#print("Prodi:\t" + str(con.execute("select nama from prodi where kode = " + str(nim[2:2]) + ";").fetchall()[0][0]));
print("Tipe:\t\t" + str(con.execute("select nama from tipe where kode = " + str(nim[4:5]) + ";").fetchall()[0][0]));
print("Jalur:\t\t" + str(con.execute("select nama from jalur where kode = " + str(nim[5:6]) + ";").fetchall()[0][0]));
print("Bulan masuk:\t" + str(nim[6:7]));
print("Tahun masuk:\t" + str(nim[7:9]));
print("Tahun keluar:\t" + str(nim[9:11]));
print("No. urut:\t" + str(nim[11:14]));
#Thanks W3Schools, Geeks for Geeks, dan Dokumentasi