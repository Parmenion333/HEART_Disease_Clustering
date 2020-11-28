import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("heart.csv")

#print(data.head(5))
print(data.info())
#print(data.describe())

# making dataframe consiting of categorical variables 
df_categorical = data[["sex","fbs","exang","cp","restecg","slope","thal","target"]]

# making dataframe consisting of numerical varibles
df_numeric = data[["age","trestbps","chol","thalach","oldpeak","ca"]]




