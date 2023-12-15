import pandas as pd
import numpy as np



#  one dimension array

s= pd.Series([1,2,3,4,np.nan,8,9,10])

#  periods is for no .of iterations

d = pd.date_range('20200301',periods=10)
# print(d)


# print(df)

dict1 = {

    'name':list(i for i in 'aman'),
    'marks' : list(range(4))
}

#  to convert the above dict into a csv file 
df = pd.DataFrame(dict1)

#  to export it as a csv we need to:
# index =False is done to avoid indexing
# df.to_csv('file ka naam' , index = false)


df.head(2)
#  first 2 rows

df.describe()
# gives statistical information about the numerical columns

aman = pd.read_csv('aman.csv')

#  changing row elements

aman['speed'][0] = 12

# will just 

aman['speed']

# changing index type

aman.index = ['first']

#  prints the datatypes of all the columns

aman.dtypes







df = pd.DataFrame(np.random.rand(10,4),index =d ,columns=['A','B','C','D'])
#  this means we will be cunstructing a data frame having 10 rows and 4 columns 

#  appending action here

df['A'][0] = 'aman'
 










