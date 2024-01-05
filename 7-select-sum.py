import sqlite3
conn = sqlite3.connect("database_fauna.db")
kursor = conn.cursor()

kursor.execute("SELECT SUM (jml_skrng) FROM FAUNA")
hasil = kursor.fetchone()[0]
print('-'*55)
print(f'| Jumlah keseluruhan total populasi adalah {hasil} ekor |')
print('-'*55)
conn.close()