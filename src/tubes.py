## tugas besar
## pengolahan dan visualisasi data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Membaca hasil data dari file CSV pake pandas
# data = pd.read_csv("data.csv")
# lokasi si file csv nya di laptop ega
data = pd.read_csv("C:\\Users\\egafa\\Documents\\Telkom University\\Kuliah smt 3\\pemograman python\\tugas-besar-pyhon\\src\\data.csv")


## Pre-processing data
# Bikin data frame 
dataFrame = pd.DataFrame(data)

# coba coba liat dataframe yang udah dibuat
print(dataFrame)

# data cleaning, pembersihan data
dataFrame.isnull().sum() # ngecek ada data yang ilang ngga

# kalo ada yang ilang ganti jadi 0
data = data.fillna(0)

## Pengolahan data pake numpy

# ubah tipe data jadi integer
for tahun in range(2017, 2020):
    data[str(tahun)] = data[str(tahun)].astype(int)

# ubah angka bulan jadi nama nama bulan
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
data['Bulan'] = [bulan[i-1] for i in data['Bulan']]


## Visualisasi data pake matploylib
# set ukuran
plt.figure(figsize=(10,6))

# garis tiap tahunnya
for tahun in range(2017, 2020):
    plt.plot(data['Bulan'], data[str(tahun)], marker='o')

# kasih nama
plt.title("Kunjungan Candi Borobudur")
plt.xlabel("Bulan")
plt.ylabel("Kunjungan")
plt.legend(range(2017, 2020))

plt.grid(True)

# tampilin grafiknya
plt.show()


