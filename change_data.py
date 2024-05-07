# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/147uB3GaCaKu0zGqrenlvPVVHEMGcH2DP
"""

import pandas as pd
import numpy as np

data = pd.read_csv('titanic.csv')

data.info()

data

df = data.dropna(subset=['Age']).copy()

df.drop('Cabin', axis=1, inplace=True)

df["Sex"] = np.where(df["Sex"] == "female", 0, 1)

#--------------------------------------------------second changes---------------------------------------

from sklearn.preprocessing import OneHotEncoder

onehotencoder = OneHotEncoder(sparse = False, drop='first')
encoded_df = pd.DataFrame(onehotencoder.fit_transform(df[['Embarked']]))

encoded_df.columns = onehotencoder.get_feature_names_out()
df_onehot = df.join(encoded_df)
df_onehot.drop('Embarked', axis = 1, inplace = True)

df_onehot.to_csv('titanic.csv', index=False)
