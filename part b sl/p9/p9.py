import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.csv')




print("======Data Headers Before Dropping Columns=======")
print(df.head(5))
df.describe()
df.info()
print("======Data Headers after Dropping Columns=======")
df.drop(['Sepal_Length'], inplace=True,axis=1)
print(df.head(5))

"""ndf = pd.DataFrame(columns=['Class','Petal_Width'])
ndf.groupby(['Class'],as_index=False).mean()"""

plt.figure(figsize=[12,6]) # to create a wider graph\n",
ax = sns.countplot(data = df,hue = 'Class',palette='Set1',x = ' Sepal_Width')
ax.set(title='Flowers of each specie',xlabel='Sepal Width',ylabel='No. of flowers')
plt.tight_layout()
plt.show()
interval = (0,1,2,4)
category = ['<1','1 to 2','>2']
df['Petal_Catg'] = pd.cut(df[' Petal_Width'],interval,labels=category)
ax = sns.countplot(data = df,x = 'Petal_Catg',hue='Class',palette='YlOrRd')
ax.set(title='Petal Width',xlabel='Category of Petals',ylabel='No. of flowers')
plt.show()



plt.figure(figsize=[12,6])
ax = sns.countplot(data = df[df['Class'] == 'Iris-setosa'],x = ' Sepal_Width',palette='Set1')
ax.set(title='Iris-setosa',xlabel='Sepal Width',ylabel='No. of flowers')
plt.show()


