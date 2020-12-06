import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("heart.csv")
#print(data.head(5))

# correlation matrix of data 
correlation_matrix = data.corr(method = "pearson")
print(correlation_matrix)



#pivot_table index = target (pivot_table agg.func default is np.mean())
pivot_all_var_target = data.pivot_table(values=["fbs","exang","cp","restecg","slope","thal","sex","age","trestbps","chol","thalach","oldpeak","ca"], index="target")
#print(pivot_all_var_target)



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



# Analysis of chol and target
#print(data.pivot_table(values=["chol","target"], index="sex"))
df_chol_target = data[["chol","target"]]
mean_chol_level_with_sickness = df_chol_target[(df_chol_target["target"] == 1)]
mean_chol_level_without_sickness = df_chol_target[(df_chol_target["target"] == 0)]

#print(df_chol_target["chol"].mean(),"chol mean value all patients")
#print(mean_chol_level_with_sickness["chol"].mean(),"chol mean value of target = 1")
#print(mean_chol_level_without_sickness["chol"].mean(),"chol mean value of target = 0")














#target_series = data["target"]
#sex_series = data["sex"]

# pivot_table index = sex
#print(data.pivot_table(values=["fbs","exang","cp","restecg","slope","thal","target","age","trestbps","chol","thalach","oldpeak","ca"], index="sex"))

# Unterschiede von mind. 0.25 bei ca, chol, oldpeak, target??, thal, cp zwischen Männern und Frauen
# pivot_table index = target
#print(data.pivot_table(values=["fbs","exang","cp","restecg","slope","thal","sex","age","trestbps","chol","thalach","oldpeak","ca"], index="target"))
# correlation between sex and target -0.28
#print(sex_series.corr(target_series, method = "pearson"), "correlation between sex and target")





