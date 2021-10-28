

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

print(df.head(5))

print(df.info())
print(df.describe())

removingColumns = ['lunch']
df.drop(removingColumns, inplace=True, axis=1)

print(df.head(5))

df['parental level of education'] = df['parental level of education'].fillna('not applicable')

print(df.head(5))

df['race/ethnicity'] = df['race/ethnicity'].map({
    'group A':'Asian Student',
    'group B':'African Student',
    'group C':'Afro-Asian Student',
    'group D':'American Student',
    'group E':'European Student'
})

print(df.head(5))

ax = sns.countplot(x='gender', hue='test preparation course', palette='Set3', data=df)
ax.set(title='Gender v/s Test Preparation Course', xlabel='Gender', ylabel='Test Preparation Course')
plt.show()

ax = sns.countplot(x='gender', hue='race/ethnicity', palette='Set1', data=df)
ax.set(title='Gender v/s Student Group', xlabel='Gender', ylabel='Student Group')
plt.show()

interval = (0, 40, 50, 60, 75, 100)
categories = ['Fail', 'Third Class', 'Second Class', 'First Class', 'Distinction']

df['Math_Cuts'] = pd.cut(df.mathscore, interval, labels=categories)
ax = sns.countplot(x='Math_Cuts', hue='gender', palette='Set2', data=df)
ax.set(title="Math Result v/s Gender", xlabel='Math Result', ylabel='Gender')
plt.show()

df['Read_Cuts'] = pd.cut(df['reading score'], interval, labels=categories)
ax = sns.countplot(x='Read_Cuts', hue='gender', palette='Set2', data=df)
ax.set(title="Reading Result v/s Gender", xlabel='Reading Result', ylabel='Gender')
plt.show()

df['Write_Cuts'] = pd.cut(df['writing score'], interval, labels=categories)
ax = sns.countplot(x='Write_Cuts', hue='gender', palette='Set2', data=df)
ax.set(title="Writing Result v/s Gender", xlabel='Writing Result', ylabel='Gender')
plt.show()

    
