from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/saurabh/Desktop/Data"
git_dir = "/Users/saurabh/Desktop/Github/PubPol590"
csv_file_good = "sample_data_clean.csv"
csv_file_bad = "/sample_data_clean.csv"

# commenttttttts

df = pd.read_csv(os.path.join(main_dir, csv_file_bad))
df = pd.read_csv(os.path.join(main_dir, csv_file_good))

## strings
string1 = "hello world "
string2 = "not sure why the above isn't working"
string3 = u'eep'

type(string1) # type str
type(string2) # type str
type(string3) # type unicode

#numeric
int1 = 342
float1 = 34.23
long1 = 3.870498720984701823475432

#logic
bool1 = True
bool2 = False

# creating lists and tuples
### lists can be changed but tuples cannot

list1 = []
list1
list2 = [1, 2, 3]
list2[1] = 5 # remember that lists are arrays, and like java, start with index 0

tup1 = (1, 2, 3) # tupples are noted by () and not [].  Also 0 index based.
tup1[2] 

##converting between lists and tupples
list2 = list(tup1) # name = list/tupple(nameofchanged)

## lists can be changed and/or extended
list2.append([3, 90]) # out: [1, 5, 5, [3, 90]]


list2 = [8, 3, 20]
list2.extend([4,2,19]) # output: [8, 3, 20, 4, 2, 19]
list3 = [1, 2, 3, 5]
len(list3) # output: 4

#converting lists to series and dataframe
list4 = range(4, 14) # range(n,m) -- gives a list from n to m-1
list4 # output: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list5 = range(5) 
list5 # output: [0, 1, 2, 3, 4]

## list to series
s1 = Series(list4)
s2 = Series(list5)

## lists to DataFrame...think of DataFrame like matrix and list like vector
list6 = [1, 2, 3, 4, 5]
list7 = [2, 3, 4, 5, 6]
zip(list6, list7) # out: [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
list8 = ['a', 'b', 'c', 'd', 'e']
zip1 = zip(list6, list8, list7)

df1 = DataFrame(zip1) # creates matrix

df2 = DataFrame(zip1, columns = ['one', 'two', 'three'])

df2['one'] # outputs the labeled column of the DataFrame only.

## Getting a subset of a DataFrame
df2[['two', 'three']][3:5] # gets rows labeled as two and three, and returns their values from row 3 and 4.

## makedataframe using dict notation

df3 = DataFrame({ 'one' : list6, 9 : list7})







