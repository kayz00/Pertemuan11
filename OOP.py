import mysql.connector

# Encapsulation: Koneksi Database
class Database:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

# Model: Representasi Produk
class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def simpan(self, db):
        query = "INSERT INTO produk (nama, harga) VALUES (%s, %s)"
        db.execute_query(query, (self.nama, self.harga))

# Main Program
db = Database(host="localhost", user="root", password="", database="toko")

# Simpan Data ke Tabel
produk1 = Produk("Laptop", 15000000)
produk1.simpan(db)

# Ambil Data dari Database
produk_list = db.fetch_all("SELECT * FROM produk")
for produk in produk_list:
    print(produk)
