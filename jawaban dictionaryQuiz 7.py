# Q-7. What will be the output of the following code snippet?

box = {} # membuat dictionary kosong untuk menyimpan nilai
jars = {} # membuat dictionary kosong untuk menyimpan nilai
crates = {} # membuat dictionary kosong untuk menyimpan nilai
box['biscuit'] = 1 # menambahkan entry dengan key 'biscuit' dan nilai 1 ke dalam dictionary box
box['cake'] = 3 # menambahkan entry dengan key 'cake' dan nilai 3 ke dalam dictionary box
jars['jam'] = 4 # menambahkan entry dengan key 'jam' dan nilai 4 ke dalam dictionary jars
crates['box'] = box # menambahkan entry dengan key 'box' dan nilai box (yang merupakan dictionary) ke dalam dictionary crates
crates['jars'] = jars # menambahkan entry dengan key 'jars' dan nilai jars (yang merupakan dictionary) ke dalam dictionary crates
print(len(crates[box])) # mencoba mengakses nilai dengan key box (yang merupakan dictionary) dalam dictionary crates, namun karena key box tidak ada dalam dictionary crates, maka akan menghasilkan Key Error

#output/jawaban: D. Type Error

# A. 1
# B. 3
# C. 4
# D. Type Error