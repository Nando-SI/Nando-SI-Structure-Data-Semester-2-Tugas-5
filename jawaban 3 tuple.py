newTuple = ('a', 'b', 'c', 'd', 'e') # membuat tuple dengan menggunakan tanda kurung dan elemen dipisahkan dengan koma
newTuple1 = tuple('abcde') # membuat tuple dengan menggunakan fungsi tuple() dan memasukkan string sebagai argumen, setiap karakter dalam string akan menjadi elemen dalam tuple
print(newTuple) # mencetak tuple yang telah dibuat
# output:
# ('a', 'b', 'c', 'd', 'e')

#  Traverse through tuple
for i in newTuple:
    print(i)
# Output:
# a
# b
# c
# d
# e