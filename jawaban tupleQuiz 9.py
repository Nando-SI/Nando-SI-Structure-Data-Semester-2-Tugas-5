# Q-9. What will be the output of the following code block?

init_tuple = (1,) * 3 # membuat tuple dengan elemen 1 yang diulang sebanyak 3 kali, sehingga menghasilkan tuple (1, 1, 1)
init_tuple[0] = 2 # mencoba untuk mengubah elemen pertama dari tuple init_tuple menjadi 2, namun karena tuple adalah tipe data yang tidak dapat diubah (immutable), maka akan terjadi error TypeError yang menyatakan bahwa objek 'tuple' tidak mendukung penugasan item
print(init_tuple) # mencetak nilai yang disimpan dalam variabel init_tuple, namun karena terjadi error pada baris sebelumnya, maka kode ini tidak akan dieksekusi dan tidak akan menghasilkan output apapun

#output/jawaban: D. TypeError: ‘tuple’ object does not support item assignment

# A. (1, 1, 1)
# B. (2, 2, 2)
# C. (2, 1, 1)
# D. TypeError: ‘tuple’ object does not support item assignment