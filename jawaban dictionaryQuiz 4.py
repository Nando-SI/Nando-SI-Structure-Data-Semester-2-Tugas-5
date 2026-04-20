# Q-4. What will be the output of the following code block?

arr = {} # membuat dictionary kosong untuk menyimpan jumlah buah
arr[1] = 1 # menambahkan entry dengan key 1 dan nilai 1
arr['1'] = 2 # menambahkan entry dengan key '1' (string) dan nilai 2, karena key '1' berbeda dengan key 1 (integer), maka akan dibuat entry baru
arr[1] += 1 # menambahkan 1 pada nilai yang sudah ada dengan key 1, sehingga nilai dengan key 1 menjadi 2

sum = 0 # variabel untuk menyimpan jumlah total nilai dalam dictionary
for k in arr: # iterasi melalui setiap key dalam dictionary arr
    sum += arr[k] # menambahkan nilai dari setiap key ke dalam variabel sum, sehingga sum akan menjadi 2 (nilai dengan key 1) + 2 (nilai dengan key '1') = 4

print(sum) # mencetak nilai total yang disimpan dalam variabel sum, yang merupakan jumlah dari nilai dengan key 1 dan key '1', sehingga menghasilkan 4

#output/jawaban: D. 4

# A. 1 
# B. 2
# C. 3 
# D. 4