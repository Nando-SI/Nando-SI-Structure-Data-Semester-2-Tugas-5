myTuple = (1,4,3,2,5) # membuat tuple dengan 5 elemen 
myTuple1 = (1,2,6,9,8,7) # membuat tuple dengan 6 elemen

print(myTuple + myTuple1) # menggabungkan kedua tuple dengan operator + dan mencetak hasilnya
# Output: (1, 4, 3, 2, 5, 1, 2, 6, 9, 8, 7)
print(myTuple * 4) # mengulangi tuple sebanyak 4 kali dengan operator * dan mencetak hasilnya
# Output: (1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5)
print(2 in myTuple1) # memeriksa apakah angka 2 ada dalam tuple1 dan mencetak hasilnya
# Output: True
print(myTuple1.count(2)) # menghitung jumlah kemunculan angka 2 dalam tuple1
# Output: 1
print(myTuple1.index(2)) # mencari indeks pertama dari angka 2 dalam tuple1
# Output: 1