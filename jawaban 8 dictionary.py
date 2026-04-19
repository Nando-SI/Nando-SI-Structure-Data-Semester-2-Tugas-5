engToSp = {"one":"uno", "two":"dos", "three":"tres"} # membuat dictionary dengan nama engToSp
engToSp["two"] = "dua" # mengubah nilai pada key "two" menjadi "dua"
print(engToSp["two"]) # mengakses nilai dengan key "two" pada dictionary engToSp
# output: 'dua'
# jika dijalankan sebelum mengubah nilai dengan key "two", maka outputnya akan "syntaxerror" karena nilai awal dari key "two" adalah 'dos' pada dictionary engToSp.
# sehingga jika kita ingin mengubah nilai dengan key "two", maka kita harus menuliskan kode untuk mengubah nilai tersebut sebelum mengaksesnya.