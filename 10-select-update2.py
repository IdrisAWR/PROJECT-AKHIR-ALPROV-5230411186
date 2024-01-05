import sqlite3
conn = sqlite3.connect('database_fauna.db')
kursor = conn.cursor()

nama_fauna = 'Pesut Mahakam'
asal_baru = 'Kalimantan Timur'

kursor.execute("UPDATE FAUNA SET asal = ? WHERE nama_fauna = ? ", (asal_baru, nama_fauna))
conn.commit()

if kursor.rowcount > 0 :
    print(f'Data dengan ID {nama_fauna} berhasil diubah !')
else :
    print(f'Belum berhasil merubah data !')

conn.close()