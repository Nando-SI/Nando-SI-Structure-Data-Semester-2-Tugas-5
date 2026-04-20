x, y, z = (10,15,20,25,30,35,40)[0::3] # slicing dengan step 3
print(x,y,z) # mencetak nilai x, y, z
# Output: 10 25 40

x = 3 # nilai awal x
y = -6 # nilai awal y

x, y = (y, x)[::-1] # membalik urutan tuple (y, x) menjadi (x, y) dan mengassign kembali ke x dan y
print(x, y) # mencetak nilai x dan y setelah pertukaran
# Output: 3 -6