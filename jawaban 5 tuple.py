newTuple = ('a', 'b', 'c', 'd', 'e') # membuat tuple dengan menggunakan tanda kurung dan elemen dipisahkan dengan koma
newTuple1 = tuple('abcde') # membuat tuple dengan menggunakan fungsi tuple() dan memasukkan string sebagai argumen, setiap karakter dalam string akan menjadi elemen dalam tuple
print(newTuple) # mencetak tuple yang telah dibuat
# output:
# ('a', 'b', 'c', 'd', 'e')

#  How to search for an element in Tuple?
print('a' in newTuple) # menggunakan operator 'in' untuk memeriksa apakah elemen 'a' ada dalam tuple newTuple
# output:
# True

def searchInTuple(pTuple, element): # mendefinisikan fungsi searchInTuple yang menerima sebuah tuple (pTuple) dan elemen yang ingin dicari (element)
    for i in pTuple: # melakukan iterasi melalui setiap elemen dalam tuple pTuple
        if i == element: # melakukan iterasi melalui setiap elemen dalam tuple pTuple, jika elemen yang sedang
            return pTuple.index(i) #
    return 'The element does not exist' # mendefinisikan fungsi searchInTuple yang menerima sebuah tuple (pTuple) dan elemen yang ingin dicari (element). Fungsi ini akan melakukan iterasi melalui setiap elemen dalam tuple, jika elemen yang dicari ditemukan, fungsi akan mengembalikan indeks dari elemen tersebut menggunakan metode index(). Jika elemen tidak ditemukan setelah iterasi selesai, fungsi akan mengembalikan pesan bahwa elemen tersebut tidak ada.

print(searchInTuple(newTuple, 'c')) # memanggil fungsi searchInTuple dengan tuple newTuple dan elemen 'c' untuk mencari indeks dari elemen tersebut dalam tuple
# output:
# 2