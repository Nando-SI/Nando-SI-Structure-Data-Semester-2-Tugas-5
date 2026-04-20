myDict = {'name': 'Edy', 'age': 26} # membuat dictionary dengan beberapa key dan value
print(myDict) # mencetak dictionary yang telah dibuat
# Output: {'name': 'Edy', 'age': 26}
newDict = {}.fromkeys([1,2,3], 0) # membuat dictionary baru dengan menggunakan method fromkeys() yang mengambil list sebagai key dan nilai default 0
print(newDict) # mencetak dictionary baru yang telah dibuat dengan method fromkeys()
# Output: {1: 0, 2: 0, 3: 0}