import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv("heart.csv")

#print(data.head(5))
#print(data.info())
#print(data.describe())

# making dataframe consiting of categorical variables 
df_categorical = data[["sex","fbs","exang","cp","restecg","slope","thal","target"]]

# making dataframe consisting of numerical varibles
df_numeric = data[["age","trestbps","chol","thalach","oldpeak","ca"]]

#df_categorical.head(5)

# catgorical variables visualisation with histogramms - witouht any for loops due to individual designation

"""plt.hist(df_categorical["sex"], color = "blue")
plt.xlabel("Women - Men")
plt.ylabel("Number")
plt.title("Gender distribution")
plt.show()

plt.hist(df_categorical["fbs"], color = "yellow")
plt.xlabel("false - true")
plt.ylabel("Number")
plt.title("Fasting blood sugar")
plt.show()

plt.hist(df_categorical["exang"], color = "purple")
plt.xlabel("false - true")
plt.ylabel("Number")
plt.title("Exercise induced angina")
plt.show()

plt.hist(df_categorical["cp"], color = "green")
plt.xlabel("from 0 to 3")
plt.ylabel("Number")
plt.title("Chest pain type")
plt.show()

plt.hist(df_categorical["slope"], color = "brown")
plt.xlabel("descending - flat - ascending")
plt.ylabel("Number")
plt.title("ST segment slope")
plt.show()

plt.hist(df_categorical["thal"], color = "pink")
plt.xlabel("NaN - fixed - normal - reversable")
plt.ylabel("Number")
plt.title("Thallium")
plt.show()

plt.hist(df_categorical["restecg"], color = "black")
plt.xlabel("...")
plt.ylabel("Number")
plt.title("Rest ECG")
plt.show()"""

"""plt.hist(df_categorical["target"], color = "red")
plt.xlabel("no disease - disease")
plt.ylabel("Number")
plt.title("Disease")
plt.show()"""

# jointplot comparing all categorical variables depending on gender

""" for i in df_categorical.columns:
    sns.jointplot(x="sex", y= i, data=data)
    plt.title(i)
    plt.show() """


# jointplot comapring all numerical variables depending on gender

""" for a in df_numeric.columns:
    sns.jointplot(x=df_categorical["sex"], y= a, data=data)
    plt.title(a)
    plt.show() """

