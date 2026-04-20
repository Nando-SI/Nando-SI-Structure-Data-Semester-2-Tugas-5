# Q-10. What will be the output of the following code snippet?

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"} # membuat dictionary dengan key "Name", "Age", "Addr", dan "Country" yang masing-masing memiliki nilai "Python", "20", "NJ", dan "USA"
id1 = id(rec) # menyimpan id dari dictionary rec dalam variabel id1, yang merupakan alamat memori tempat dictionary rec disimpan
del rec # menghapus dictionary rec, sehingga id yang sebelumnya disimpan dalam id1 tidak lagi merujuk pada objek yang valid dalam memori
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"} # membuat dictionary baru dengan isi yang sama seperti sebelumnya, tetapi karena dictionary baru ini dibuat setelah dictionary rec dihapus, maka kemungkinan besar id yang diberikan untuk dictionary baru ini akan berbeda dengan id yang sebelumnya disimpan dalam id1
id2 = id(rec) # menyimpan id dari dictionary rec yang baru dibuat dalam variabel id2, yang kemungkinan besar akan berbeda dengan id1 karena dictionary rec yang lama sudah dihapus dan dictionary baru dibuat di lokasi memori yang berbeda
print(id1 == id2) # mencetak hasil perbandingan antara id1 dan id2, yang akan menghasilkan False karena id1 merujuk pada objek dictionary rec yang sudah dihapus, sedangkan id2 merujuk pada objek dictionary rec yang baru dibuat, sehingga kedua id tersebut tidak sama

#output/jawaban: A. True

# A. True
# B. False
# C. 1
# D. Exception