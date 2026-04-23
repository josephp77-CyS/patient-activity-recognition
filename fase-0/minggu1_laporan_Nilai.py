def predikat(n):
    if n >= 85: return "A"
    elif n >= 70: return "B"
    elif n >= 55: return "C"
    else: return "D"

def input_mahasiswa():
    data = []
    print("Ketik nama dan nilai (cth: Andi 85). Ketik 'done' jika selesai.")
    while True:
        teks = input("> ")
        if teks.lower() == 'done':
            break
        bagian = teks.split()
        if len(bagian) < 2:        
            print("Format salah. Cth: Andi 85")
            continue
        try:
            nama  = bagian[0]
            nilai = int(bagian[1])
            data.append({'nama': nama, 'nilai': nilai})
        except ValueError:
            print("Nilai harus angka. Coba lagi.")
    return data

data = input_mahasiswa()

if not data:
    print("Tidak ada data.")
else:
    list_nilai = [d['nilai'] for d in data]  

    print("\n===== LAPORAN NILAI UJIAN =====")
    for d in data:
        p = predikat(d['nilai'])
        print(f"{d['nama']:<10}: {d['nilai']}  ({p})")

    rata  = sum(list_nilai) / len(list_nilai)
    i_max = list_nilai.index(max(list_nilai))
    i_min = list_nilai.index(min(list_nilai))
    lulus = sum(1 for n in list_nilai if n >= 70)

    print(f"\nRata-rata kelas : {rata:.2f}")
    print(f"Nilai tertinggi : {data[i_max]['nama']} ({max(list_nilai)})")
    print(f"Nilai terendah  : {data[i_min]['nama']} ({min(list_nilai)})")
    print(f"Lulus           : {lulus} mahasiswa")
    print(f"Tidak lulus     : {len(data)-lulus} mahasiswa")