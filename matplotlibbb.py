import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt


#
# data_ = pd.read_csv('s:/csvfiles/ipl-matches.csv')
# print(data_.WinningTeam.value_counts().head(1))
#
#
# date = np.arange(0,10000)
#
# a = np.random.randint(low=0,high=date.shape[0],size=100)
# # print(plt.hist(a,rwidth=0.1,color='black'))
#
# a = [100,200,200,400,500]
# subjects = ['english','hindi','kannda','account','social'
#             ]
#
# print(plt.style.available)
# plt.style.use('seaborn')
# plt.pie(a,labels=subjects,explode=[0,0,0,0.5,0])
#
# plt.savefig('likebaby.png')
# import os
#
# print('likebaby.png' in os.listdir(os.getcwd()))
#
#
# #
# iris = pd.read_csv('S:/csvfiles/iris.csv')
# iris = (iris.sample(5).replace({'Iris-setosa':0,
#                                 'Iris-virginica':1,
#                                 'Iris-versicolor':2}))
# print(iris.shape)
#
#
# iriss = pd.DataFrame([*iris.Id],columns=['Id']).head(10)
#
# print(pd.concat([iris,iriss])['Id'].size)

# print(iris)
# colors = ['r','g','b','y','p']
# plt.scatter(iris.SepalLengthCm,iris.PetalLengthCm,c=['g'],alpha=0.2)




# for x in ((zip(iris.SepalLengthCm,iris.PetalLengthCm))):
#     plt.text(x=x[0],y=x[1],s='like')
#
# plt.xticks(rotation='vertical')
# plt.axhline(4.9)
# plt.axvline(5.6)


# a = np.array([1,2,3,4])
#
# print(a[np.isnan(np.where(a%2==0,True,np.nan))==False])

# figure,subplott = plt.subplots(nrows=2,ncols=2)
# figure.show()
# print(figure,subplott,sep='\n')
#
# print(iris)
# subplott.scatter(iris.SepalLengthCm,iris.PetalLengthCm)
# plt.show()




#
#
# # bar = plt.bar(df.season,df.Fours,width=0.2,color=['y','g','r','b','b'])
# #
#
# # a = [10,15,33,44,49,51,70,80,60,66]
# #
# # histogram = plt.hist(df.Fours,width=10,bins=[1563,1700,2054])
# # plt.show()
#


df = pd.read_csv('s:/csvfiles/fours-sixes.csv')
df2  = pd.read_csv('s:/csvfiles/batter (1).csv')
df3 = pd.read_csv('s:/csvfiles/vk.csv')
df4 = pd.read_csv('s:/csvfiles/gayle-175.csv')
df5  = pd.read_csv('s:/csvfiles/batsman_season_record.csv')
df6 = pd.read_csv('s:/csvfiles/iris.csv')

# print(df5)
# # iris = (df6.sample(5))
# # iris2 = iris.replace({'Iris-setosa':0,'Iris-virginica':1,'Iris-versicolor':2})
# # plt.bar(df5.batsman,df5['2015'],width=0.2,color='black',label='2015')
# # plt.bar(df5.batsman,df5['2016'],bottom=df5['2015'],width=0.2,color='red',label=2016)
# # plt.bar(df5.batsman,df5['2017'],bottom=df5['2016']+df5['2015'],color='green',width=0.2,label=2017)
# # plt.legend()
# # print(pd.pivot(df5,index='2015',columns='batsman'))
# # pie = plt.pie(df5['2015'],labels=df5.batsman,autopct='%0.1f%%',explode=[0,0,0,0.3,0.3])
# # plt.show()
# # print(df5)
#
# # print(iris.filter(['Id',"SepalLengthCm"]))
# # plt.figure(figsize=(10,10))
# # plt.scatter(iris.SepalLengthCm,iris.PetalLengthCm,c=iris2.Species,cmap='summer',)
# # for index,_ in enumerate(zip(iris.SepalLengthCm,iris.PetalLengthCm)):
# #     plt.text(_[0],_[1],iris.Species.iloc[index])
# # plt.show()
#
# #
# # batsmans = (df2.sample(25))
# # print(batsmans.runs.max())
# #
# # plt.figure(figsize=(10,10))
# # plt.scatter(batsmans.runs,batsmans.strike_rate)
# #
# # for index,xx in enumerate(zip(batsmans.runs,batsmans.strike_rate)):
# #     plt.text(xx[0],xx[1],batsmans.batter.iloc[index])
# #
# #
# # plt.axhline(150,color='red')
# # plt.axvline(4000,color='yellow')
# # plt.show()
#
#
#
#
# # figure,axis = plt.subplots(figsize=(10,10))
# #
# # print(p)
#
#
#
# fig = plt.figure()
#
# x = fig.add_subplot(221,)
#
# x.scatter(df5.batsman,df5['2015'])
#
#
# x = fig.add_subplot(222)
#
# x.scatter(df5.batsman,df5['2016'])
#
#
# x = fig.add_subplot(223)
# plt.xticks(rotation='vertical')
# x.scatter(df5.batsman,df5['2016'])
#
#
#
# x = fig.add_subplot(224)
# plt.xticks(rotation='vertical')
# x.scatter(df5.batsman,df5['2016'])
#
#
#
#
# plt.show()

import matplotlib.pyplot as plt
# fig = plt.figure()
#
# df2 = df2.sample(5)
#
# a = fig.add_subplot() # his create only (pie hist bar plot) #subplot not working
#
#
#
# subplott = plt.subplot()
# # print(df2)
# # subplott.scatter(df2.runs,df2.avg,df2.strike_rate)
#
# x = np.linspace(-10,10,100)
# y = np.linspace(-10,10,100)
#
# xx,yy = np.meshgrid(x,y)
# z = xx**2+yy**2
# #
# # x = subplott.plot_surface(xx,yy,z)
# # plt.colorbar(x)
#
# x = subplott.contourf(xx,yy,z)
# plt.colorbar(x)
#
#
#
# df = (df[(df.ballnumber<7) & (df.batsman_run==6)])



# (df[['ballnumber','batsman_run']])
#
# print(df.pivot_table(index='overs',columns='ballnumber')['batsman_run'])
#
#
# a = (df.pivot_table(index='overs',columns='ballnumber',aggfunc='count')['batsman_run'])
#
#
# plt.imshow(a)
# plt.colorbar()
# plt.show()


#
# series = pd.Series([1,2,3,4,5,6,7])
#
# print(series.plot(kind='pie'))
# plt.show()




# df5.plot(kind='scatter',x='batsman',y='2015',marker='+',c='2016')
# plt.show()






# df = pd.read_csv('s:/csvfiles/IPL_Ball_by_Ball_2008_2022.csv')


# df = pd.DataFrame({'date':('5/1/2017','5/2/2017','5/3/2017','5/1/2017','5/2/2017',
#                            '5/3/2017','5/3/2017','5/2/2017','5/5/2017'),
#                    'city':('newyork','newyork','newyork','mumbai','mumbai','mumbai',
#                     'bejing','bejing','bejing'),
#                    'humidity':(56,58,60,80,83,85,26,30,35),
#                    'tempreture':(65,66,68,75,78,82,80,77,79)})
#
#
#
# print(df.pivot('city','date')['humidity'])
# print()
# print()
# print(df.pivot('city','date')['tempreture'])
# print()
# print()
# print(df.pivot_table('city','date',aggfunc = 'count'))
#
#





















