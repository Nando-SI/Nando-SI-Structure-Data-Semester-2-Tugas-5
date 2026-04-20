# Q-6. What will be the output of the following code snippet?

my_dict = {} # membuat dictionary kosong untuk menyimpan nilai
my_dict[(1,2,4)] = 8 # menambahkan entry dengan key (1,2,4) (tuple) dan nilai 8, karena key (1,2,4) dianggap berbeda dengan key 1 (integer) dalam konteks dictionary, maka akan dibuat entry baru
my_dict[(4,2,1)] = 10 # menambahkan entry dengan key (4,2,1) (tuple) dan nilai 10, karena key (4,2,1) dianggap berbeda dengan key 1 (integer) dalam konteks dictionary, maka akan dibuat entry baru
my_dict[(1,2)] = 12 # menambahkan entry dengan key (1,2) (tuple) dan nilai 12, karena key (1,2) dianggap berbeda dengan key 1 (integer) dalam konteks dictionary, maka akan dibuat entry baru

sum = 0 # variabel untuk menyimpan jumlah total nilai dalam dictionary
for k in my_dict: # iterasi melalui setiap key dalam dictionary my_dict
    sum += my_dict[k] # menambahkan nilai dari setiap key ke dalam variabel sum, sehingga sum akan menjadi 1 (nilai dengan key 1) + 8 (nilai dengan key (1,2,4)) + 10 (nilai dengan key (4,2,1)) + 12 (nilai dengan key (1,2)) = 31

print (sum) # mencetak nilai total yang disimpan dalam variabel sum, yang merupakan jumlah dari nilai dengan key 1 (yang bernilai 1), key (1,2,4) (yang bernilai 8), key (4,2,1) (yang bernilai 10), dan key (1,2) (yang bernilai 12), sehingga menghasilkan 31
print(my_dict) # mencetak isi dari dictionary my_dict, yang terdiri dari entry dengan key 1 dan nilai 1, entry dengan key (1,2,4) dan nilai 8, entry dengan key (4,2,1) dan nilai 10, serta entry dengan key (1,2) dan nilai 12

#output/jawaban: 
# B. 30
#     {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}

# A. Syntax error
# B. 30   
#     {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}
# C. 47
#     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# D. 30
#     {[1, 2]: 12, [4, 2, 1]: 10, [1, 2, 4]: 8}