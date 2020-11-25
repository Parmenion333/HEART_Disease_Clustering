import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("heart.csv")

# making dataframe consiting of categorical variables 
df_categorical = data[["sex","fbs","exang","cp","restecg","slope","thal","target"]]

# making dataframe consisting of numerical varibles
df_numeric = data[["age","trestbps","chol","thalach","oldpeak","ca"]]

#print(df_categorical.loc[df_categorical["sex"] == 1])

sns.jointplot(x="sex", y="chol", data= data)
#plt.show()

for i in df_categorical.columns:
    sns.jointplot(x="sex", y= i, data=data)
    plt.title(i)
    plt.show()
