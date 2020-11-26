import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("heart.csv")

#print(pd.pivot_table(data=data, values=data["chol"], index=data["target"]))
print(data.pivot_table(values=["chol","target"], index="sex"))


print((data["sex"] == 1).count())