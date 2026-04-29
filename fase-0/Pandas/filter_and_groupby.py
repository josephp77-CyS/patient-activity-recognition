import pandas as pd

# Buat DataFrame —  seperti tabel Excel
dataset = pd.DataFrame({
    'video_id'  : ['v001','v002','v003','v004','v005'],
    'aktivitas' : ['walking','falling','sitting','walking','falling'],

    'durasi_s'  : [5.2, 3.1, 8.4, 6.0, 2.9],

    'subjek'    : ['S01','S01','S02','S02','S03']
})


print(dataset.head())      # tampilkan 5 baris pertama
print(dataset.shape)       # (5, 4) → 5 baris, 4 kolom
print(dataset.dtypes)      # tipe data tiap kolom
print(dataset.describe())  # statistik ringkas kolom numerik


# Filter: ambil hanya video 'falling'
fall_data = dataset[dataset['aktivitas'] == 'falling']
print(fall_data)

# Groupby: hitung video per aktivitas
jumlah = dataset.groupby('aktivitas').size()
print(jumlah)


# Rata-rata durasi per aktivitas
rata_durasi = dataset.groupby('aktivitas')['durasi_s'].mean()
print(rata_durasi)

# Simpan ke CSV
dataset.to_csv('dataset_aktivitas.csv', index=False)


# Filter: ambil hanya video 'falling'
fall_data = dataset[dataset['aktivitas'] == 'falling']
print(fall_data)

# Groupby: hitung video per aktivitas 
#Ini juga sangat penting dalam mengelompokkan dan mengecek keseimbangan data yang ada 
jumlah = dataset.groupby('aktivitas').size()
print(jumlah)


# Rata-rata durasi per aktivitas
rata_durasi = dataset.groupby('aktivitas')['durasi_s'].mean()
print(rata_durasi)


# Simpan ke CSV
dataset.to_csv('dataset_aktivitas.csv', index=False)