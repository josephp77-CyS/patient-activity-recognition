# Data mahasiswa dan nilai
mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fani"]
nilai     = [78, 85, 62, 90, 55, 88]

def predikat(n):
    if n >= 85:
        return "A"
    elif n >= 70:
        return "B"
    elif n >= 55:
        return "C"
    else:
        return "D"


print("===== LAPORAN NILAI UJIAN =====")

for i in range(len(mahasiswa)):
    p = predikat(nilai[i])
    print(f"{mahasiswa[i]:<8}: {nilai[i]}  ({p})")


rata_rata = sum(nilai) / len(mahasiswa)      
idx_max   = nilai.index(max(nilai)) 


idx_min   = nilai.index(min(nilai))                    
lulus = 0
for i in range(len(mahasiswa)):
    if nilai[i] >= 70:
        lulus += 1




# Cetak hasil
print()
print(f"Rata-rata kelas : {rata_rata:.2f}")
print(f"Nilai tertinggi : {mahasiswa[idx_max]} ({max(nilai)})")
print(f"Nilai terendah  : {mahasiswa[idx_min]} ({min(nilai)})")  
print(f"Lulus           : {lulus} mahasiswa")
print(f"Tidak lulus     : {len(mahasiswa) - lulus } mahasiswa")