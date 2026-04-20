# Q-8. What will be the output of the following code block?

init_tuple = ('Python') * 3 # membuat tuple dengan elemen 'Python' yang diulang sebanyak 3 kali, namun karena tidak menggunakan tanda koma untuk menunjukkan bahwa ini adalah sebuah tuple, maka hasilnya akan menjadi string 'PythonPythonPython' yang merupakan hasil pengulangan string 'Python' sebanyak 3 kali

print(type(init_tuple)) # mencetak tipe data dari variabel init_tuple menggunakan fungsi type(), yang akan menghasilkan <class 'str'> karena init_tuple adalah sebuah string yang merupakan hasil pengulangan string 'Python' sebanyak 3 kali, bukan sebuah tuple

# output/jawaban: B. <class ‘str’>

# A. <class ‘tuple’>
# B. <class ‘str’>
# C. <class ‘list’>
# D. <class ‘function’>