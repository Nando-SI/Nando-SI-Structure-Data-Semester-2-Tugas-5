# Q-5. What will be the output of the following code snippet?

my_dict = {} # membuat dictionary kosong untuk menyimpan nilai
my_dict[1] = 1 # menambahkan entry dengan key 1 dan nilai 1
my_dict['1'] = 2 # menambahkan entry dengan key '1' (string) dan nilai 2, karena key '1' berbeda dengan key 1 (integer), maka akan dibuat entry baru
my_dict[1.0] = 4 # menambahkan entry dengan key 1.0 (float) dan nilai 4, karena key 1.0 dianggap sama dengan key 1 (integer) dalam konteks dictionary, maka nilai dengan key 1 akan diperbarui menjadi 4

sum = 0 # variabel untuk menyimpan jumlah total nilai dalam dictionary
for k in my_dict: # iterasi melalui setiap key dalam dictionary my_dict
    sum += my_dict[k] # menambahkan nilai dari setiap key ke dalam variabel sum, sehingga sum akan menjadi 4 (nilai dengan key 1) + 2 (nilai dengan key '1') = 6
    
print (sum) # mencetak nilai total yang disimpan dalam variabel sum, yang merupakan jumlah dari nilai dengan key 1 (yang diperbarui menjadi 4) dan key '1' (yang bernilai 2), sehingga menghasilkan 6

#output/jawaban: D. 6

# A. 7
# B. Syntax error
# C. 3
# D. 6