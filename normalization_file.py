import pandas as pd
import numpy as np

data = pd.read_csv("heart.csv")
#print(data.head(5))

data_num = data[["age","trestbps","chol","thalach","oldpeak","ca","cp"]]


# Normalization session length
class Normalization:

    def __init__(self, min_v, max_v, series):
        self.min_v = min_v
        self.max_v = max_v
        self.series = series
        self.list = []

    def normalizator(self):
        for value in self.series:
            norm_value = ((value - self.min_v)/(self.max_v - self.min_v))

            self.list.append(norm_value)
        
        series_norm = pd.Series(self.list)

        return series_norm 


# Normalization age
age_instance = Normalization(data_num["age"].min(), data_num["age"].max(), data_num["age"])
age_length_norm = age_instance.normalizator()

# Normalization trestbps
trestbps_instance = Normalization(data_num["trestbps"].min(), data_num["trestbps"].max(), data_num["trestbps"])
trestbpsp_norm = trestbps_instance.normalizator()

# Normalization chol
chol_instance = Normalization(data_num["chol"].min(), data_num["chol"].max(), data_num["chol"])
chol_norm = chol_instance.normalizator()

# Normalization thalach
thalach_instance = Normalization(data_num["thalach"].min(), data_num["thalach"].max(), data_num["thalach"])
thalach_norm = thalach_instance.normalizator()

# Normalization oldpeak
oldpeak_instance = Normalization(data_num["oldpeak"].min(), data_num["oldpeak"].max(), data_num["oldpeak"])
oldpeak_norm = oldpeak_instance.normalizator()

# Normalization ca
ca_instance = Normalization(data_num["ca"].min(), data_num["ca"].max(), data_num["ca"])
ca_norm = ca_instance.normalizator()

# Normalization cp
cp_instance = Normalization(data_num["cp"].min(), data_num["cp"].max(), data_num["cp"])
cp_norm = cp_instance.normalizator()

# new normalized dataframe
data_num_norm_normfile = pd.concat([age_length_norm,trestbpsp_norm,chol_norm,thalach_norm,oldpeak_norm,ca_norm,cp_norm], axis=1)
data_num_norm_normfile.columns = ["age","trestbps","chol","thalach","oldpeak","ca","cp"]