import sqlite3
conn = sqlite3.connect("database_fauna.db")
kursor = conn.cursor()

kursor.execute("SELECT * FROM FAUNA ORDER BY jml_skrng DESC ")
baris_tabel = kursor.fetchall()
print('='*5,'TABEL JUMLAH FAUNA DARI TERBESAR','='*5)
print('-'*150)
print("{:<15}{:<25}{:<25}{:<25}{:<25}{:<25}".format("ID FAUNA","NAMA FAUNA","JENIS","ASAL","JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
print('='*150)
for baris in baris_tabel:
    print("{:<15}{:<25}{:<25}{:<25}{:<25}{:<25}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

conn.close()