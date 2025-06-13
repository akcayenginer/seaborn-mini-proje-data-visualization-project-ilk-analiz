import seaborn as sns
import numpy as np
al=sns.load_dataset("iris")
f=al.head()
print(f)

print(al.groupby('species').mean())#specila gore ortama değer
print(al.groupby('species').sum())
print(al.groupby('species').std())
print(al.groupby('species').count())
print(al.groupby('species').max())
print(al.groupby('species').min())
print(al.groupby('species').mean().loc['setosa'])
s=al.info()
print(s)
d=al.describe()
print(d)
sns.pairplot(al,hue='species',corner=True,palette="Set2",kind="kde",diag_kind="hist")
#örnek: petal genişliği türlere gore boxplot
sns.boxplot(data=al,x='species',y=
  'petal_width',hue='species',palette='Set2')
#örnek: speal uzunlugu türlere gore boxplot
sns.boxplot(data=al,x='species',y='speal_length',hue='species',palette='set2')
#örnek:speal genişliği türlere gore boxplot
sns.boxplot(data=al,x='species',y='speal_width',hue='species',palette='Set2')
#örnek: petal uzunlugu türlere gore boxplot
sns.boxplot(data=al,x='species',y='petal_length',hue='species',palette='Set2')

