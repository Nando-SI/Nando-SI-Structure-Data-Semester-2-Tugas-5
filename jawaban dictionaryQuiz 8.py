# Q-8. What will be the output of the following code block?

dict = {'c': 97, 'a': 96, 'b': 98} # membuat dictionary dengan key 'c', 'a', dan 'b' yang masing-masing memiliki nilai 97, 96, dan 98

for _ in sorted(dict): # iterasi melalui setiap key dalam dictionary yang sudah diurutkan secara alfabetis, sehingga urutan key yang diakses adalah 'a', 'b', dan 'c'
    print (dict[_]) # mencetak nilai dari setiap key yang diakses, sehingga akan mencetak nilai dengan key 'a' (96), nilai dengan key 'b' (98), dan nilai dengan key 'c' (97) dalam urutan tersebut

#output/jawaban: A. 96 98 97

# A. 96 98 97
# B. 96 97 98
# C. 98 97 96
# D. NameError