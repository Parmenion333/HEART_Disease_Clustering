import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("heart.csv")
pd.set_option("display.max_rows", 5, "display.max_columns", None)
print(data.head(5))

# Analysis of sex, age and sickness
df_sex_age_target = data[["sex","age","target"]]
#print(df_sex_age_target.head(5))

men_with_sickness = df_sex_age_target[(df_sex_age_target["sex"] == 1) & (df_sex_age_target["target"] == 1)]
#print(men_with_sickness.head(5))
#print(men_with_sickness["sex"].count(), " number of men with sickness")
#print(men_with_sickness["age"].mean(), " mean age of men with sickness")

women_with_sickness = df_sex_age_target[(df_sex_age_target["sex"] == 0) & (df_sex_age_target["target"] == 1)]
#print(women_with_sickness["sex"].count(), "number of women with sickness")
#print(women_with_sickness["age"].mean(), " mean age of women with sickness")

#print(pd.pivot_table(data=data, values=data["chol"], index=data["target"]))
print(data.pivot_table(values=["chol","target"], index="sex"))


target_series = data["target"]
sex_series = data["sex"]

# pivot_table index = sex
print(data.pivot_table(values=["fbs","exang","cp","restecg","slope","thal","target","age","trestbps","chol","thalach","oldpeak","ca"], index="sex"))

# Unterschiede von mind. 0.25 bei ca, chol, oldpeak, target??, thal, cp zwischen Männern und Frauen
# pivot_table index = target
#print(data.pivot_table(values=["fbs","exang","cp","restecg","slope","thal","sex","age","trestbps","chol","thalach","oldpeak","ca"], index="target"))
# correlation between sex and target -0.28
#print(sex_series.corr(target_series, method = "pearson"), "correlation between sex and target")

# correlation matrix of data 
print(data.corr(method = "pearson"))
#iininnn


