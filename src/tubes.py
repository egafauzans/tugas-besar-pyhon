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

# data cleaning, pembersihan data
dataFrame.isnull().sum() # ngecek ada data yang ilang ngga

print(dataFrame)

## Pengolahan data pake numpy


## Visualisasi data pake matploylib
