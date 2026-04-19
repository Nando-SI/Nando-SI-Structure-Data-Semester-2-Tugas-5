engToSp = {"one":"uno", "two":"dos", "three":"tres"} # membuat dictionary dengan nama engToSp
engToSp["two"] = "dua" # mengubah nilai dengan key "two" pada dictionary engToSp menjadi "dua"
engToSp["four"] = "cuatro" # menambahkan key "four" dengan nilai "cuatro" pada dictionary engToSp
engToSp.pop("two") # menghapus key "two" dan nilainya dari dictionary engToSp
engToSp.popitem() # menghapus item terakhir yang dimasukkan pada dictionary engToSp
engToSp.clear() # menghapus seluruh item pada dictionary engToSp
print(engToSp) # mengakses seluruh nilai pada dictionary engToSp
# output: {}