import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import pylab as pl
import numpy as np
import os
%matplotlib inline

data_frame = pd.read_csv("autos.csv",encoding="latin-1")
#data_frame.head()
#data_frame.describe()

missing_values = data_frame.isnull().sum()
#missing_values

cat_val = ["seller","offerType","abtest","gearbox","fuelType","notRepairedDamage","nrOfPictures"]

for col in cat_val:
    print ([col]," : ",data_frame[col].unique())
