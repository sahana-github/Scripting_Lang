import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('blackfri.csv')

print(df.head(5))
print(df.describe())
print(df.info())

uneededColumns = ['User_ID', 'Product_ID', 'Stay_In_Current_City_Years']
df.drop(uneededColumns, axis=1, inplace=True)

print(df.head(5))

df['City_Category'] = df['City_Category'].fillna('A')

print(df.head(5))

df['City_Category'] = df['City_Category'].map({
    'A': 'Metro City',
    'B': 'Small Town',
    'C': 'Village'
})

print(df.head(5))

df.rename(columns={'Product_Category_1':'Baseball_Caps', 'Product_Category_2':'Wine_Tumblers', 'Product_Category_3':'Pet_Raincoats'}, inplace=True)

print(df.head(5))

df['Marital_Status'] = df['Marital_Status'].map({
    0:'Un-Married',
    1:'Married'
})

print(df.head(10))

print(pd.crosstab(df['Gender'], df.Pet_Raincoats))


ax = sns.countplot(x='Gender', hue='Pet_Raincoats', palette='Set1', data=df)
ax.set(title='Gender v/s Total No of Pet Raincoats bought', xlabel='Gender', ylabel='No of Pet Raincoats')
plt.show()

print(pd.crosstab(df['Gender'], df.City_Category))

ax = sns.countplot(x='Gender', hue='City_Category', palette='Set2', data=df)
ax.set(title='Gender v/s City Category', xlabel='Gender', ylabel='City Category')
plt.show()
