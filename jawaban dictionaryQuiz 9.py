# Q-9. What will be the output of the following code snippet?

rec = {"Name" : "Python", "Age":"20"} # membuat dictionary dengan key "Name" dan "Age" yang masing-masing memiliki nilai "Python" dan "20"
r = rec.copy() # membuat salinan dari dictionary rec dan menyimpannya dalam variabel r, sehingga r memiliki isi yang sama dengan rec tetapi merupakan objek yang berbeda dalam memori
print(id(r) == id(rec)) # mencetak hasil perbandingan antara id dari r dan id dari rec, yang akan menghasilkan False karena r dan rec adalah objek yang berbeda dalam memori meskipun memiliki isi yang sama

#output/jawaban: B. False

# A. True
# B. False
# C. 0
# D. 1