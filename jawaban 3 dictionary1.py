myDict = {'name': 'Edy', 'age': 26} # membuat dictionary dengan key 'name', value 'Edy', dan 'age', value 26
myDict['address'] = 'London' # menambahkan key 'address' dengan value 'London' ke dalam dictionary
myDict['age'] = 27 # mengubah value pada key 'age' menjadi 27

#  Traverse through a dictionary
def traverseDict(dict): # membuat fungsi traverseDict yang menerima parameter dict
    for key in dict: # melakukan iterasi pada setiap key dalam dictionary
        print(key, dict[key]) # mencetak key dan value yang sesuai dengan key tersebut
        
traverseDict(myDict) # memanggil fungsi traverseDict dengan argumen myDict untuk menampilkan seluruh key dan value dalam dictionary
# output:
# name Edy
# age 27
# address London