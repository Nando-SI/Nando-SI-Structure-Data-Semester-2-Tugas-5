# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5} # membuat dictionary dengan beberapa key dan value
print(sorted(myDict, key=len)) # mengurutkan key dalam dictionary berdasarkan panjangnya
# output: ['aas', 'udd', 'sseo', 'werwi', 'eooooa']
print(myDict) # mencetak dictionary
# output: {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}