myDict = {'name': 'Edy', 'age': 26} # membuat dictionary dengan beberapa key dan value
print(myDict.get('name', 26)) # mencetak value dari key 'name' menggunakan method get() dengan default value 26 jika key tidak ditemukan
# Output: Edy
print(myDict.get('city', 27)) # mencetak value dari key 'city' menggunakan method get() dengan default value 27 jika key tidak ditemukan
# Output: 27
print(myDict.get('city')) # mencetak value dari key 'city' menggunakan method get() tanpa default value
# Output: None
print(myDict.items()) # mencetak semua item dalam dictionary menggunakan method items()
# Output: dict_items([('name', 'Edy'), ('age', 26)])
print(myDict.keys()) # mencetak semua key dalam dictionary menggunakan method keys()
# Output: dict_keys(['name', 'age'])
print(myDict.values()) # mencetak semua value dalam dictionary menggunakan method values()
# Output: dict_values(['Edy', 26])
print(myDict.popitem()) # menghapus dan mencetak item terakhir dalam dictionary menggunakan method popitem()
# Output: ('age', 26)
print(myDict) # mencetak dictionary setelah item terakhir dihapus
# Output: {'name': 'Edy'}
print(myDict.setdefault('name', 'added'))# mencetak value dari key 'name' menggunakan method setdefault() dengan default value 'added' jika key tidak ditemukan, namun karena key 'name' sudah ada maka nilai yang dicetak adalah 'Edy'
# Output: Edy
print(myDict.setdefault('name1', 'added')) # mencetak value dari key 'name1' menggunakan method setdefault() dengan default value 'added' jika key tidak ditemukan, karena key 'name1' tidak ada maka nilai yang dicetak adalah 'added' dan key 'name1' dengan value 'added' akan ditambahkan ke dictionary
# Output: added
print(myDict) # mencetak dictionary setelah key 'name1' dengan value 'added' ditambahkan
# Output: {'name': 'Edy', 'name1': 'added'}
print(myDict.pop('name1','not')) # menghapus dan mencetak value dari key 'name1' menggunakan method pop()
# Output: added
print(myDict) # mencetak dictionary setelah key 'name1' dihapus
# Output: {'name': 'Edy'}
newDict = {'a': 1, 'b': 2, 'c': 3} # membuat dictionary baru dengan beberapa key dan value
myDict.update(newDict) # mengupdate dictionary myDict dengan dictionary newDict menggunakan method update()
print(newDict) # mencetak dictionary baru yang telah dibuat
# Output: {'a': 1, 'b': 2, 'c': 3}
print(myDict) # mencetak dictionary myDict setelah diupdate dengan dictionary newDict
# Output: {'name': 'Edy', 'a': 1, 'b': 2, 'c': 3}