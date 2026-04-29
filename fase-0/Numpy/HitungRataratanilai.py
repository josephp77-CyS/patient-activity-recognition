def list_mahasiswa():
    list_nya=[]
    print("Isi nama depan mahasiswa dan beri spasi untuk nilai nya (Ketik 'done' jika sudah selesai) : ")

    while True:
        input_user = input("> ")
        if input_user.lower() == 'done':
            break
        list_nya.append(input_user)

    return list_nya

data_mahasiswa = list_mahasiswa()
list_nilai = []

print("Data Mahasiswa")
print("-" * 25)

for item in data_mahasiswa:
    pecah = item.split()
    nama = pecah[0]
    nilai = int(pecah[1])
    list_nilai.append(nilai)


    print(f"Mahassiwa {nama} | Nilai: {nilai}")

print("-" * 25)

if len(list_nilai) > 0:
    total = sum(list_nilai)
    rata_rata = total / len(list_nilai)
    print(f"Rata - rata mahasiwa : {rata_rata:.2f}")
else:
    print("No data")

print("-" * 25)
nilaiMax = max(list_nilai)
indeks_nilaiMax = list_nilai.index(nilaiMax)

data_NilaiMax = data_mahasiswa[indeks_nilaiMax].split()
nama_NilaiMax = data_NilaiMax[0]

print(f"Mahasiswa dengan nilai Tertinggi {nama_NilaiMax} {nilaiMax}")





