import numpy as np

kepala_y = np.array([0.10,0.11,0.12,0.55,0.60,0.58])

kaki_y   = np.array([0.85,
                     0.86,
                     0.84,
                     0.70,
                     0.72,
                     0.69])
frame_id = np.arange(1, 7)   


jarak_vertikal = kaki_y - kepala_y
print(f"Jarak kepala-kaki tiap frame : {jarak_vertikal}")

is_falling = jarak_vertikal < 0.3

frame_jatuh = frame_id[is_falling]
print(f"Frame yang terdeteksi jatuh: {frame_jatuh}")

jumlah_jatuh = len(frame_jatuh)

presentase = (jumlah_jatuh/len(frame_id)) * 100
print(f"Persentase frame yang jatuh : {presentase:.1f}%")

