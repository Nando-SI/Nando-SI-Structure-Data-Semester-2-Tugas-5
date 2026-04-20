# Q-3. What will be the output of the following code block?

fruit = {} # membuat dictionary kosong untuk menyimpan jumlah buah

def addone(index): # fungsi untuk menambahkan jumlah buah berdasarkan index
    if index in fruit: # jika index sudah ada dalam dictionary, tambahkan 1 pada jumlahnya
        fruit[index] += 1 # jika index belum ada dalam dictionary, buat entry baru dengan jumlah 1
    else: # jika index belum ada dalam dictionary, buat entry baru dengan jumlah 1
        fruit[index] = 1 # menambahkan entry baru dengan jumlah 1
        
addone('Apple') # menambahkan 'Apple' ke dalam dictionary, sehingga jumlahnya menjadi 1
addone('Banana') # menambahkan 'Banana' ke dalam dictionary, sehingga jumlahnya menjadi 1
addone('apple') # menambahkan 'apple' ke dalam dictionary, karena 'apple' berbeda dengan 'Apple' (case-sensitive), maka akan dibuat entry baru dengan jumlah 1
print (len(fruit)) # mencetak jumlah entry dalam dictionary, yang terdiri dari 'Apple', 'Banana', dan 'apple', sehingga menghasilkan 3

#output/jawaban: C. 3

# A. 1 
# B. 2
# C. 3 
# D. 4