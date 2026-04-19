#dictionary bersarang da tuple
# membuat dictionary yang berisi nama mahasiswa dan nilai mereka dalam bentuk tuple
nilai_mahasiswa = { 
    "Andi": (80, 85, 90), # key "Andi" value tuple (80, 85, 90)
    "Budi": (75, 70, 80), # key "Budi" value tuple (75, 70, 80)
    "Citra": (85, 90, 95) # key "Citra" value tuple (85, 90, 95)
}
# menghitung rata-rata nilai untuk setiap mahasiswa
for nama, nilai in nilai_mahasiswa.items(): #mengambil nama dan nilai dari dictionary
    rata_rata = sum(nilai) / len(nilai) #menghitung rata-rata dengan menjumlahkan nilai dan membaginya dengan jumlah nilai
    print(f"Rata-rata nilai {nama}: {rata_rata}") #menampilkan hasil rata-rata nilai untuk setiap mahasiswa
#Output:
#Rata-rata nilai Andi: 85.0
#Rata-rata nilai Budi: 75.0
#Rata-rata nilai Citra: 90.0