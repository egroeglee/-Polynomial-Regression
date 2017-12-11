# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
# x為因 y為果
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

"""
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:, 3] = labelencoder_x.fit_transform(x[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
x = onehotencoder.fit_transform(x).toarray()

# Avoiding the summy Variable trap
x = x[:, 1:]

# Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
"""

#Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
"""

#Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

#Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)#degree 默認值為2
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

#Visualising the Linear Regression results
plt.scatter(x, y, color='red')#實際結果
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Truth or Bluff(inear regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Visualising the ploynomial regression results
x_grid = np.arange(min(x), max(x), 0.1)#增加線條的曲線度
x_grid = x_grid.reshape(len(x_grid), 1)#變成矩陣
plt.scatter(x, y, color='red')
plt.plot(x_grid, lin_reg_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
plt.title('Truth or Bluff(Polynomial regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression
lin_reg.predict(6.5)
"""
計算該員工的年資&所對應的等級職位，
假設這邊職位等級為6且做了2年(4年後可昇為7)
所以這邊設定為6.5
"""

#Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))
#這邊會算出來該薪水為158862.4526516



