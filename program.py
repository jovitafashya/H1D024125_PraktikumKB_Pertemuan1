import random
import statistics

nama_mahasiswa = []
nilai_mahasiswa = []

jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nData mahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nilai = int(input("Nilai: "))
    
    nama_mahasiswa.append(nama)
    nilai_mahasiswa.append(nilai)

print("\n=== HASIL NILAI ===")
for i in range(jumlah):
    print(f"{nama_mahasiswa[i]} - {nilai_mahasiswa[i]}")
    
    if nilai_mahasiswa[i] >= 80:
        print("Grade: A")
    elif nilai_mahasiswa[i] >= 70:
        print("Grade: B")
    elif nilai_mahasiswa[i] >= 60:
        print("Grade: C")
    else:
        print("Grade: D")

rata_rata = statistics.mean(nilai_mahasiswa)
nilai_tertinggi = max(nilai_mahasiswa)
nilai_terendah = min(nilai_mahasiswa)

mahasiswa_beruntung = random.choice(nama_mahasiswa)

print("\n=== ANALISIS ===")
print(f"Rata-rata nilai: {rata_rata}")
print(f"Nilai tertinggi: {nilai_tertinggi}")
print(f"Nilai terendah: {nilai_terendah}")
print(f"Mahasiswa beruntung: {mahasiswa_beruntung}")