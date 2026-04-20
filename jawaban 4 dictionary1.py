myDict = {'name': 'Edy', 'age': 26} # membuat dictionary dengan key 'name', value 'Edy', dan 'age', value 26
myDict['address'] = 'London' # menambahkan key 'address' dengan value 'London' ke dalam dictionary
myDict['age'] = 27 # mengubah value pada key 'age' menjadi 27

#  Searching a dictionary
def searchDict(dict, value): # membuat fungsi searchDict yang menerima parameter dict dan value
    for key in dict: # melakukan iterasi pada setiap key dalam dictionary
        if dict[key] == value: # jika value pada key tersebut sama dengan value yang dicari
            return key, value # mengembalikan key dan value yang sesuai dengan value yang dicari
    return 'The value does not exist' # jika value yang dicari tidak ditemukan dalam dictionary, mengembalikan pesan 'The value does not exist'
print(searchDict(myDict, 27)) # memanggil fungsi searchDict dengan argumen myDict dan 27 untuk mencari key yang memiliki value 27 dalam dictionary
# output:
# ('age', 27)