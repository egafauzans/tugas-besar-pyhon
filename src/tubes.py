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

## Pengolahan data pake numpy

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

