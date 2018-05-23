Best bet for survival on the titanic?
Here we have a part of a dataset from passengers on the titanic. I'm curious to find out if your gender and your class had anything to do with survival.
Data Dictionary (What the data means, copied from Kaggle.com)
Variable Definition Key survival = Survival 0 = No, 1 = Yes pclass = Ticket class 1 = 1st, 2 = 2nd, 3 = 3rd sex = Sex or Gender Age = Age in years
sibs p= # of siblings / spouses aboard the Titanic
parch = # of parents / children aboard the Titanic
ticket = Ticket number
fare = Passenger fare
cabin = Cabin number
embarked = Port of Embarkation
In [1]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
%matplotlib inline

style.use("ggplot")

import seaborn as sns



#Import the titanic data set and findout how many records we have

df = pd.DataFrame.from_csv('Documents/titanic-data.csv')
len(df)
Out[1]:
891
Of the 891 people who embarked on the titanic according to this data, How many survived? of those, what are the trends among those that survived, and what are the trends among those that didnt?
In [2]:
df.head()
#Getting the different data points
Out[2]:
Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
PassengerId											
1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S
2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th...	female	38.0	1	0	PC 17599	71.2833	C85	C
3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S
4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S
5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S
In [3]:
#Find out how how many records we have
df.count()
Out[3]:
Survived    891
Pclass      891
Name        891
Sex         891
Age         714
SibSp       891
Parch       891
Ticket      891
Fare        891
Cabin       204
Embarked    889
dtype: int64
In [4]:
#Our data appears to have missing values
df.isnull().sum()
Out[4]:
Survived      0
Pclass        0
Name          0
Sex           0
Age         177
SibSp         0
Parch         0
Ticket        0
Fare          0
Cabin       687
Embarked      2
dtype: int64
We're missing 177 age values which is sure to effect our analysis, I'm assuming the cabin values have to do with multiple passengers in one cabin
In [5]:
#Find out how many people survived by adding the survived column
df['Survived'].sum()
Out[5]:
342
In [6]:
#calculating survival rate
df['Survived'].mean()
Out[6]:
0.3838383838383838
We can see that 342 people out of 891, or roughly 38 percent survived. Now we'll need to look for trends among the survivors. Im curious to know if gender affected survival.
In [7]:
df.groupby('Sex').count()
Out[7]:
Survived	Pclass	Name	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
Sex										
female	314	314	314	261	314	314	314	314	97	312
male	577	577	577	453	577	577	577	577	107	577
In [8]:
df.groupby('Sex')["Survived"].sum()
Out[8]:
Sex
female    233
male      109
Name: Survived, dtype: int64
Based off of these numbers alone it appears that females were more than twice as likely to survive than males, there could be a few reasons for this for example, the men could have stayed behind to make sure women boarded any available life boats first etc. Class could have also played a role here, lets find out.
In [9]:
df.groupby('Pclass')["Survived"].sum()
Out[9]:
Pclass
1    136
2     87
3    119
Name: Survived, dtype: int64
This is interesting, almost as many people from class three survived as from class 1, with around 25 percent of survivors coming from class 2, so I think we should look @ the total percentage of men and women passengers from each class for a better idea.
In [10]:
df['Pclass'].value_counts()
Out[10]:
3    491
1    216
2    184
Name: Pclass, dtype: int64
In [11]:
df.groupby('Pclass')["Survived"].mean()
Out[11]:
Pclass
1    0.629630
2    0.472826
3    0.242363
Name: Survived, dtype: float64
Looking at the amount of people in each class we can see that 3rd class had more passengers than both 1st and 2nd classes combined, lets look at the percentages for passenger survival in each class
Above we have the survival percentage for each class,
1st class = 63% 2nd class = 47% 3rd class = 24%
so it appears that you were most likely to survive if you were a 1st class passenger, and we know that females were more than twice as likely to survive as males, so would it be safe to say that your best chance of survival was to be a female in first class?
In [12]:
df.groupby(['Pclass','Sex']).sum()
Out[12]:
Survived	Age	SibSp	Parch	Fare
Pclass	Sex					
1	female	91	2942.00	52	43	9975.8250
male	45	4169.42	38	34	8201.5875
2	female	70	2125.50	37	46	1669.7292
male	17	3043.33	37	24	2132.1125
3	female	72	2218.50	129	115	2321.1086
male	47	6706.42	173	78	4393.5865
According to these numbers, Females were 67% of survivors in first class, 80% in second class, and 61% in third class, so it would appear that there is a correlation between being a female and surviving. Also the highest survival percentage came from the first class, Now all we need to do is visualize this data
In [13]:
sns.factorplot(x="Sex", y="Survived", col="Pclass",
...                    data=df, saturation=.5,
...                    kind="bar", ci=None, aspect=.6)
Out[13]:
<seaborn.axisgrid.FacetGrid at 0x10cd85860>

In [14]:
sns.factorplot(data=df, col='Pclass', x='Sex', y='Age', hue='Survived', 
               kind='violin', size=10, aspect=0.5, s=10)
plt.yticks(np.arange(0,81,10));

The charts above show how much more likely females were to survive than males per class
Based of the limited amount of data that we had, we cant come to a complete, without a shadow of a doubt conclusion, but its safe to say based off of our findings that the best chance for survival on the Titanic were to be a female in first class.
