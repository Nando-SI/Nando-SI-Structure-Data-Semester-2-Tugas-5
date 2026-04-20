# Q-7. What will be the output of the following code block?

l = [1, 2, 3] # membuat list dengan elemen 1, 2, dan 3 yang disimpan dalam variabel l
init_tuple = ('Python',) * (l.__len__() - l[::-1][0]) # membuat tuple dengan elemen 'Python' yang diulang sebanyak (panjang list l - elemen terakhir dari list l), dimana panjang list l adalah 3 dan elemen terakhir dari list l adalah 3, sehingga menghasilkan tuple ('Python', 'Python')

print(init_tuple) # mencetak nilai yang disimpan dalam variabel init_tuple, yang merupakan tuple dengan elemen 'Python' yang diulang sebanyak 2 kali, sehingga menghasilkan ('Python', 'Python')

#output/jawaban: A. ()

# A. ()
# B. (‘Python’)
# C. (‘Python’, ‘Python’)
# D. Runtime Exception.