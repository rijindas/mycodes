import pandas as pd
from sklearn.decomposition import PCA

data = pd.read_csv("C:/Users/Riji/Desktop/new_customers.csv",skiprows = 1, header = None)
pca = PCA()
Data = pca.fit_transform(data)
data = pca.transform(Data)
print(data)
print("The results displayed")