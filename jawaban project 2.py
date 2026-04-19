# Membuat dictionary untuk penyimpanan barang
penyimpanan = {
    "Laptop": {"harga": 8000000, "jumlah": 10}, # key "Laptop" value dictionary {"harga": 8000000, "jumlah": 10}
    "Smartphone": {"harga": 5000000, "jumlah": 20}, # key "Smartphone" value dictionary {"harga": 5000000, "jumlah": 20}
    "Tablet": {"harga": 3000000, "jumlah": 15}, # key "Tablet" value dictionary {"harga": 3000000, "jumlah": 15}
    "Gamepad": {"harga": 2000000, "jumlah": 25}, # key "Gamepad" value dictionary {"harga": 2000000, "jumlah": 25}
    "Keyboard": {"harga": 500000, "jumlah": 30} # key "Keyboard" value dictionary {"harga": 500000, "jumlah": 30}
}

# Menampilkan semua data barang
print("Daftar Barang:")
for nama_barang, data in penyimpanan.items(): #mengambil nama barang dan data dari dictionary
    print(f"-{nama_barang}: Harga = {data['harga']}, Jumlah = {data['jumlah']}") #menampilkan nama barang, harga, dan jumlah

# Menghitung total nilai persediaan untuk setiap barang
total_nilai = 0
for data in penyimpanan.values(): #mengambil data dari dictionary
    total_nilai += data["harga"] * data["jumlah"] #menghitung total nilai dengan mengalikan harga dan jumlah, lalu menambahkannya ke total_nilai

print("Total nilai persediaan:", total_nilai) #menampilkan total nilai persediaan dengan hasil perhitungan

# mencari barang dengan jumlah paling sedikit
barang_tersedikit = min(penyimpanan.items(), key=lambda item: item[1]["jumlah"]) #mencari nama barang dengan jumlah paling sedikit menggunakan fungsi min dan lambda untuk mengakses jumlah dalam dictionary
print("Barang dengan jumlah paling sedikit:", barang_tersedikit[0], "(", barang_tersedikit[1]["jumlah"], ")") #menampilkan nama barang dengan jumlah paling sedikit beserta jumlahnya

# mencari barang dengan harga paling mahal
barang_termahal = max(penyimpanan.items(), key=lambda item: item[1]["harga"]) #mencari nama barang dengan harga paling mahal menggunakan fungsi max dan lambda untuk mengakses harga dalam dictionary
print("Barang dengan harga paling mahal:", barang_termahal[0], "(", barang_termahal[1]["harga"], ")") #menampilkan nama barang dengan harga paling mahal beserta harganya

# update jumlah barang tertentu
barang = input("masukkan nama barang yang ingin diupdate jumlahnya: ") # meminta input nama barang yang ingin diupdate jumlahnya dari pengguna
jumlah_baru = int(input("masukkan jumlah baru: ")) # meminta input jumlah baru dari pengguna
if barang in penyimpanan: #memeriksa apakah nama barang yang diinputkan ada dalam dictionary
    penyimpanan[barang]["jumlah"] = jumlah_baru #jika ada, update jumlah barang dengan nilai baru
    print("Jumlah barang berhasil diupdate!") #menampilkan pesan bahwa jumlah barang berhasil diupdate
else:
    print("Barang tidak ditemukan!") #menampilkan pesan bahwa barang tidak ditemukan

# menambahkan barang baru ke dalam dictionary
nama_baru = input("masukkan nama barang baru: ") # meminta input nama barang baru dari pengguna
harga_baru = int(input("masukkan harga barang baru: ")) # meminta input harga barang
jumlah_baru = int(input("masukkan jumlah barang baru: ")) # meminta input jumlah barang

penyimpanan[nama_baru] = {"harga": harga_baru, "jumlah": jumlah_baru} # menambahkan barang baru ke dalam dictionary dengan nama sebagai key dan harga serta jumlah sebagai value dalam bentuk dictionary
print("Barang baru berhasil ditambahkan!") # menampilkan pesan bahwa barang baru berhasil ditambahkan

# menampilkan semua data barang setelah penambahan
print("Daftar Barang setelah penambahan:")
for nama_barang, data in penyimpanan.items(): #mengambil nama barang dan data dari dictionary
    print(f"-{nama_barang}: Harga = {data['harga']}, Jumlah = {data['jumlah']}") #menampilkan nama barang, harga, dan jumlah setelah penambahan

    #output:
#Daftar Barang:
#-Laptop: Harga = 8000000, Jumlah = 10
#-Smartphone: Harga = 5000000, Jumlah = 20
#-Tablet: Harga = 3000000, Jumlah = 15
#-Gamepad: Harga = 2000000, Jumlah = 25
#-Keyboard: Harga = 500000, Jumlah = 30
#Total nilai persediaan: 290000000
#Barang dengan jumlah paling sedikit: Laptop ( 10 )
#Barang dengan harga paling mahal: Laptop ( 8000000 )
#masukkan nama barang yang ingin diupdate jumlahnya: Tablet
#masukkan jumlah baru: 20
#Jumlah barang berhasil diupdate!
#masukkan nama barang baru: Headset
#masukkan harga barang baru: 200000
#masukkan jumlah barang baru: 15
#Barang baru berhasil ditambahkan!
#Daftar Barang setelah penambahan:
#-Laptop: Harga = 8000000, Jumlah = 10
#-Smartphone: Harga = 5000000, Jumlah = 20
#-Tablet: Harga = 3000000, Jumlah = 20
#-Gamepad: Harga = 2000000, Jumlah = 25
#-Keyboard: Harga = 500000, Jumlah = 30
#-Headset: Harga = 200000, Jumlah = 15