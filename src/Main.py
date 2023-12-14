## tugas besar - pengolahan dan visualisasi data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Membaca data dari file CSV pake pandas
# tes = pd.read_csv()
# lokasi si file csv nya di laptop ega
tes = pd.read_csv("C:\\Users\\egafa\\Documents\\Telkom University\\Kuliah smt 3\\pemograman python\\tugas-besar-pyhon\\src\\tes.csv")

## Pre-processing data
# Bikin data frame 
dataFrame = pd.DataFrame(tes)

# data cleaning, pembersihan data
dataFrame.isnull().sum() # ngecek ada data yang ilang ngga

## Pengolahan data pake numpy
rataBerat = np.mean(tes['Berat'])
rataTinggi = np.mean(tes['Tinggi'])

## Visualisasi data pake matploylib
plt.figure(figsize=(10,5))
plt.plot(tes['Umur'], tes['Tinggi'], label='Tinggi')
plt.plot(tes['Umur'], tes['Berat'], label='Berat')
plt.xlabel('Umur')
plt.ylabel('Nilai')
plt.title('Visualisasi Data')
plt.legend()
plt.show()