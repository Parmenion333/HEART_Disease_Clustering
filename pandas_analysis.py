import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("heart.csv")

#print(pd.pivot_table(data=data, values=data["chol"], index=data["target"]))
print(data.pivot_table(values=["chol","target"], index="sex"))


print((data["sex"] == 1).count())

target_series = data["target"]
sex_series = data["sex"]

# pivot_table index = sex
print(data.pivot_table(values=["fbs","exang","cp","restecg","slope","thal","target","age","trestbps","chol","thalach","oldpeak","ca"], index="sex"))

# Unterschiede von mind. 0.25 bei ca, chol, oldpeak, target??, thal, cp zwischen Männern und Frauen
# pivot_table index = target
print(data.pivot_table(values=["fbs","exang","cp","restecg","slope","thal","sex","age","trestbps","chol","thalach","oldpeak","ca"], index="target"))
# correlation between sex and target -0.28
print(sex_series.corr(target_series, method = "pearson"), "correlation between sex and target")

# correlation matrix of data 
# print(data.corr(method = "pearson"))