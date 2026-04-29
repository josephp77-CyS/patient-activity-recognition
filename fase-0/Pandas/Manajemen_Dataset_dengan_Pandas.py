import pandas as pd


datasetPrimer = pd.DataFrame({
    'video_id'     : ['v001', 'v002', 'v003', 'v004', 'v005', 'v006', 'v007', 'v008', 'v009', 'v010', 'v011', 'v012', 'v013', 'v014', 'v015', 'v016', 'v017', 'v018', 'v019', 'v020'],
    'aktivitas'    : ['walking', 'lying', 'falling', 'sitting', 'lying', 'sitting', 'sitting', 'sitting', 'sitting', 'walking',  'lying', 'falling', 'falling', 'walking', 'falling', 'lying', 'walking', 'falling', 'lying', 'walking'],
    'subjek'       : ['S01', 'S01', 'S02','S02', 'S03','S01', 'S04', 'S05','S01', 'S02', 'S03','S01', 'S03', 'S04','S02', 'S03','S02', 'S03','S02', 'S03'],
    'durasi_detik' : [3.0, 4.5, 3.0, 6.7, 10.5, 8.0, 9.1, 10.1, 3.0, 4.5, 5.3, 6.7, 7.5,3.0, 4.5,3.0, 4.5, 3.1, 9.1, 10.1],
    'kualitas'     : ['good', 'medium', 'poor', 'good','medium','good','poor','poor','poor','poor','medium','good','poor','medium','medium','good','medium','medium','good','poor']
})
print('==' * 26)
print(datasetPrimer.head())     
print('==' * 26)
print(f'{datasetPrimer.shape}  >> jumlah baris dan kolom')  
print('==' * 26)   
print(f'{datasetPrimer.dtypes} >> Jenis type data tiap kolom') 
print('==' * 26) 
print(datasetPrimer.describe()) 
print('==' * 26)

jumlah = datasetPrimer.groupby('aktivitas').size()
print(f'{jumlah}\nJumlah dari masing - masing aktivitas yaitu sebanyak 5 yang menunjukan data sudah seimbang')
print('==' * 26)

rata_rata_durasi_aktivitas = datasetPrimer.groupby('aktivitas')['durasi_detik'].mean()
print(rata_rata_durasi_aktivitas)
print('==' * 26)

video_poor = datasetPrimer[datasetPrimer['kualitas'] == 'poor']
persentase_poor = (len(video_poor) / len(datasetPrimer)) * 100
print(f'{video_poor}\nVideo yang masih memiliki kualitas poor dan harus dilakukan perekaman ulang')
print(f'dengan persentase : {persentase_poor}% dari total data kualitas video yang ada')
print('==' * 26)

print("=== Verifikasi Kolom Kategori ===")
print("Subjek unik  :", datasetPrimer['subjek'].unique())
print("Aktivitas unik:", datasetPrimer['aktivitas'].unique())
print("Kualitas unik :", datasetPrimer['kualitas'].unique())
print('==' * 26)
datasetPrimer.to_csv('Dataset_Primer.csv', index=False)

dP_cek =pd.read_csv('Dataset_Primer.csv')
print(f"CSV disimpan - {dP_cek.shape[0]} Baris, {dP_cek.shape[1]} Kolom")
print(dP_cek.head(3))





