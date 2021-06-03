import pandas as pd 
import numpy as np 
import pickle

df = pd.read_csv('heart.csv')

years = (df['age']/365).round(0)

del df['id']
del df['age']

<<<<<<< HEAD
df.drop(df[df['ap_hi']>250].index, inplace = True)
df.drop(df[df['ap_hi']<60].index, inplace = True)
df.drop(df[df['ap_lo']>180].index, inplace = True)
df.drop(df[df['ap_lo']<50].index, inplace = True)
=======
df.drop(df[df['ap_hi']>200].index, inplace = True)
df.drop(df[df['ap_hi']<100].index, inplace = True)
df.drop(df[df['ap_lo']>150].index, inplace = True)
df.drop(df[df['ap_lo']<60].index, inplace = True)
df.drop(df[df['height']<120].index, inplace = True)
df.drop(df[df['weight']<40].index, inplace = True)
>>>>>>> 276b6588ddbc00866f6c6979eee553d326bc3603

df.insert(0,'years',years)
print(df.head())

X = df.iloc[:,:-1].values
Y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=1)

from sklearn.svm import SVC
result = SVC()
result.fit(X_train, Y_train)

model = result
result1 = result.predict(X_test)

from sklearn.metrics import accuracy_score
prediction = accuracy_score(Y_test, result1)
print("Accuracy =", prediction * 100, "%")

pickle.dump(model, open('heart.pkl', 'wb'))