import sqlite3
conn = sqlite3.connect('database_fauna.db')
kursor = conn.cursor()

def tampilkan_data_sebelum():
    kursor.execute("SELECT * FROM FAUNA")
    sebelum = kursor.fetchall()
    print('='*5,'TABEL SEBELUM DI DELETE','='*5)
    print('-'*150)
    print("{:<15}{:<25}{:<25}{:<25}{:<25}{:<25}".format("ID FAUNA","NAMA FAUNA","JENIS","ASAL","JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
    print('='*150)
    for baris in sebelum:
        print("{:<15}{:<25}{:<25}{:<25}{:<25}{:<25}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

def tampilkan_data_setelah():
    kursor.execute("DELETE FROM FAUNA WHERE asal = 'Kalimantan'")
    kursor.execute("SELECT * FROM FAUNA")
    sebelum = kursor.fetchall()
    print('='*5,'TABEL SESUDAH DI DELETE','='*5)
    print('-'*150)
    print("{:<15}{:<25}{:<25}{:<25}{:<25}{:<25}".format("ID FAUNA","NAMA FAUNA","JENIS","ASAL","JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
    print('='*150)
    for baris in sebelum:
        print("{:<15}{:<25}{:<25}{:<25}{:<25}{:<25}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))
    
    conn.close()

tampilkan_data_sebelum()
print()
tampilkan_data_setelah()