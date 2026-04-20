# Q-4. What will be the output of the following code block?

init_tuple_a = 1, 2 # membuat tuple dengan elemen 1 dan 2 yang disimpan dalam variabel init_tuple_a, menggunakan tanda koma untuk menunjukkan bahwa ini adalah sebuah tuple
init_tuple_b = (3, 4) # membuat tuple dengan elemen 3 dan 4 yang disimpan dalam variabel init_tuple_b, menggunakan tanda kurung untuk menunjukkan bahwa ini adalah sebuah tuple

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]] # menggunakan list comprehension untuk mencetak hasil penjumlahan antara init_tuple_a dan init_tuple_b, yang akan menghasilkan tuple baru yang merupakan gabungan dari kedua tuple tersebut, sehingga menghasilkan (1, 2, 3, 4), kemudian fungsi sum() digunakan untuk menghitung jumlah dari elemen-elemen dalam tuple tersebut, sehingga menghasilkan 10

#output/jawaban: C. 10

# A. Nothing gets printed.
# B.  4
# C. 10
# D. TypeError: unsupported operand type