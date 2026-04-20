myDict = {'name': 'Edy', 'age': 26} # membuat dictionary dengan key 'name', value 'Edy', dan 'age', value 26
myDict['address'] = 'London' # menambahkan key 'address' dengan value 'London' ke dalam dictionary
myDict['age'] = 27 # mengubah value pada key 'age' menjadi 27
# delete or remove a dictionary
myDict.pop('name') # menghapus key 'name' beserta value-nya dari dictionary
print(myDict) # menampilkan dictionary setelah key 'name' dihapus
# output:
# {'age': 27, 'address': 'London'}