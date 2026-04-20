newTuple = ('a', 'b', 'c', 'd', 'e') # membuat tuple dengan menggunakan tanda kurung dan elemen dipisahkan dengan koma
newTuple1 = tuple('abcde') # membuat tuple dengan menggunakan fungsi tuple() dan memasukkan string sebagai argumen, setiap karakter dalam string akan menjadi elemen dalam tuple
print(newTuple) # mencetak tuple yang telah dibuat
# output:
# ('a', 'b', 'c', 'd', 'e')

for index in range(len(newTuple)): # menggunakan loop for untuk mengakses setiap elemen dalam tuple dengan menggunakan indeks
    print(newTuple[index]) # mencetak elemen tuple pada indeks yang sedang diakses
# Output:
# a
# b
# c
# d
# e