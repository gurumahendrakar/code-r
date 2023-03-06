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



iris = pd.read_csv('S:/csvfiles/iris.csv')
iris = (iris.sample(5).replace({'Iris-setosa':0,
                                'Iris-virginica':1,
                                'Iris-versicolor':2}))
# print(iris.shape)
#
#
# iriss = pd.DataFrame([*iris.Id],columns=['Id']).head(10)
#
# print(pd.concat([iris,iriss])['Id'].size)

# print(iris)
colors = ['r','g','b','y','p']
plt.scatter(iris.SepalLengthCm,iris.PetalLengthCm,c=['g'])
plt.show()





































