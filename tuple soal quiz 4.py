#membuat tuple ke dictionary
keys = ("nama", "umur", "kota") #membuat tuple untuk keys
values = ("Budi", 20, "Medan") #membuat tuple untuk values
# mengubah tuple menjadi dictionary
hasil = dict(zip(keys, values)) #menggunakan zip untuk menggabungkan keys dan values menjadidictionary
# menampilkan hasil
print(hasil) #menampilkan dictionary yang telah dibuat dari tuple
#output: {'nama': 'Budi', 'umur': 20, 'kota': 'Medan'}