## tugas besar - pengolahan dan visualisasi data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file CSV pake pandas
tes = pd.read_csv('tes.csv')

## Pre-processing data
# Bikin data frame 
dataFrame = pd.DataFrame(tes)

# data cleaning, pembersihan data
dataFrame.isnull().sum() # ngecek ada data yang ilang ngga

## Pengolahan data
rataBerat = np.mean(data['Berat'])
rataTinggi = np.mean(data['Tinggi'])