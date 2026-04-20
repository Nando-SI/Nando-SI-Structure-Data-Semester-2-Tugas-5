# Q-5. What will be the output of the following code block?

init_tuple = [(0, 1), (1, 2), (2, 3)] # membuat list yang berisi tiga tuple, dimana setiap tuple terdiri dari dua elemen yaitu pasangan angka yang berurutan, dan menyimpan list tersebut dalam variabel init_tuple
result = sum(n for _, n in init_tuple) # menggunakan fungsi sum() untuk menghitung jumlah dari elemen kedua (n) dalam setiap tuple yang terdapat dalam list init_tuple, dengan menggunakan generator expression untuk iterasi melalui setiap tuple dalam init_tuple dan mengambil elemen kedua (n) dari setiap tuple, sehingga menghasilkan jumlah dari 1 + 2 + 3 = 6

print(result) # mencetak nilai yang disimpan dalam variabel result, yang merupakan hasil dari penjumlahan elemen kedua dari setiap tuple dalam list init_tuple, sehingga menghasilkan 6

#output/jawaban: B. 6

# A. 3
# B. 6
# C. 9
# D. Nothing gets printed.