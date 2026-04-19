# membuat disctionary dengan data mahasiswa
data_mahasiswa = {
    "Andi": (80,75,90), # key "Andi" value tuple (80, 75, 90)
    "Budi": (70,80,85), # key "Budi" value tuple (70, 80, 85)
    "Citra": (90,95,85), # key "Citra" value tuple (90, 95, 85)
    "Dewi": (85,80,90), # key "Dewi" value tuple (85, 80, 90)
    "zaki": (50,60,70) # key "zaki" value tuple (50, 60, 70)
}
# menghitung nilai akhir untuk setiap mahasiswa
nilai_akhir = {} #membuat dictionary kosong untuk menyimpan nilai akhir setiap mahasiswa

for nama, nilai in data_mahasiswa.items(): #mengambil nama dan nilai dari dictionary
    tugas, uts, uas = nilai
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4) #menghitung nilai akhir dengan rumus tugas 30%, uts 30%, uas 40%

# menentukan grade berdasarkan nilai akhir
    if akhir >= 85: #jika nilai akhir lebih besar atau sama dengan 85
        grade = "A" #maka grade A
    elif akhir >= 70: #jika nilai akhir lebih besar atau sama dengan 70
        grade = "B" #maka grade B
    elif akhir >= 60: #jika nilai akhir lebih besar atau sama dengan 60
        grade = "C" #maka grade C
    else: #jika nilai akhir < 60
        grade = "D" #jika nilai akhir kurang dari 60 maka grade D

    nilai_akhir[nama] = akhir
    print("nama:", nama) #menampilkan nama setiap mahasiswa
    print("nilai akhir:", round(akhir, 1)) #menampilkan nilai akhir setiap mahasiswa dengan pembulatan 1 desimal
    print("grade:", grade) #menampilkan grade setiap mahasiswa
    print() #menambahkan baris kosong untuk memisahkan setiap mahasiswa

mahasiswa_nilai_tertinggi = max(nilai_akhir, key=nilai_akhir.get) #mencari nama mahasiswa dengan nilai akhir tertinggi
print("nilai tertinggi", mahasiswa_nilai_tertinggi, "(", round(nilai_akhir[mahasiswa_nilai_tertinggi], 1), ")") #menampilkan nama mahasiswa dengan nilai akhir tertinggi beserta nilainya dengan pembulatan 1 desimal
#Output:
#nama: Andi
#nilai akhir: 82.5
#grade: B

#nama: Budi
#nilai akhir: 79.0
#grade: B

#nama: Citra
#nilai akhir: 89.5
#grade: A

#nama: Dewi
#nilai akhir: 85.5
#grade: A

#nama: zaki
#nilai akhir: 61.0
#grade: C

#nilai tertinggi Citra (89.5)