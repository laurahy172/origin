import pandas as pd
import collections as co
import pickle
nnnn
[‎7/‎18/‎2017 3:23 PM] Wijaya, L.: 
http://matthewrocklin.com/blog/work/2015/03/16/Fast-Serialization 

#--------------------------Dec-Mar----------------------------#
path="C:/Users/laura.han/PycharmProjects/SCB/v9/automation/data/data.pickle"
self=pickle.load(open(path, "rb"))
def preprocess(self,path):
    self['LEV1'] = self.LEV1.map(int)
    self['LEV2'] = self.LEV2.map(str)
    self['LEV3'] = self.LEV3.map(str)
    self['LEV4'] = self.LEV4.map(str)
    self['LEV5'] = self.LEV5.map(str)
    self = self.drop_duplicates()
    self.LEV5.map(float)
    return self

def agg_exact(self):
    self['LEVs'] = self.USERID.map(str)+self.LEV1.map(str) + "_" + self.LEV3.map(str) + "_" + self.LEV4.map(str)
    self.drop(self.columns[[2, 3, 4, 5, 6]], axis=1, inplace=True)
    dict = {str(k): list(v) for k, v in self.groupby("USERID")["LEVs"]}
    return self,dict

df=preprocess(self,path)
exact,dict=agg_exact(df)

c=Counter(dict[c, for c in dict.keys()])
temp=c['10117289043'];type(temp)#list
len(temp)

id=dict.keys()
len(id) #196

c.most_common(3)

#--------------------------1stApril----------------------------#
path2="C:/Users/laura.han/PycharmProjects/SCB/v10/automation/data/data.pickle"
dfnew=DF()
df2=dfnew.preprocess(path2)
exact2,dict2  =   agg_exact(df2)
d=Counter(dict2)
e=c+d
temp=e['10117289043'];type(temp)#list
len(temp)
temp.most_common(2)


exact.LEVs.value_counts()
user_ids=exact.USERID
set([1,2,3])-set([2,3,4])

#------------testing---------
dict1={'red':4, 'blue': 2}
#c = Counter(dict1)
#c2=[{i:Counter(dict1[i])} for i in dict1]


dict2= Counter({'red': 5, 'blue': 5,'yellow':4})
Counter(dict1)+Counter(dict2)
d2=[{i:Counter(dict2[i])} for i in dict2]

Counter(c2)+Counter(d2)


Out[316]: Counter({'blue': [2, 4, 2, 4], 'red': [4, 5]})
for i in

#----------exploratory analysis----------
exacy
