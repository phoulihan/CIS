

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.decomposition import PCA



the_path = 'C:/Users/dell/Desktop/instacart-market-basket-analysis/'

orders = pd.read_csv(the_path + 'orders.csv', sep=",")
order_train=orders[orders['eval_set'].isin(['train'])]
order_test=orders[orders['eval_set'].isin(['test'])]
#只提取order中test和train数据，便于分析

aisles = pd.read_csv(the_path + 'aisles.csv', sep=",")
order_products__train = pd.read_csv(the_path + 'order_products__train.csv', sep=",")
products = pd.read_csv(the_path + 'products.csv', sep=",")
#打开文件
order_products__train = order_products__train[0:300000]
#减少数据量

order_prior_train = pd.merge(order_train,order_products__train,on=['order_id','order_id'])


_summary_train = pd.merge(order_products__train,products, on = ['product_id','product_id'])
_summary_train = pd.merge(_summary_train,orders,on=['order_id','order_id'])
summary_train = pd.merge(_summary_train,aisles,on=['aisle_id','aisle_id'])

#summary_train['aisle'].value_counts()[0:10] 购买最多的十类商品

cust_prod = pd.crosstab(summary_train['user_id'], summary_train['aisle'])
#用户&购买种类

pca = PCA(n_components=6)
pca.fit(cust_prod)
pca_samples = pca.transform(cust_prod)
ps = pd.DataFrame(pca_samples)
 #数据预处理
 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
tocluster = pd.DataFrame(ps[[4,1]])
#选取其中 4，1两列
print (tocluster.shape)
print (tocluster.head())

fig = plt.figure(figsize=(8,8))
plt.plot(tocluster[4], tocluster[1], 'o', markersize=2, color='blue', alpha=0.5, label='class1')
#作图

plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

clusterer = KMeans(n_clusters=4,random_state=42).fit(tocluster)
#KMeans 聚类算法 原理见：https://blog.csdn.net/weixin_38656890/article/details/80447548

centers = clusterer.cluster_centers_
c_preds = clusterer.predict(tocluster)
#预测四类聚集
print(centers)


fig = plt.figure(figsize=(8,8))
colors = ['orange','blue','purple','green']
colored = [colors[k] for k in c_preds]
#每一类设置不同颜色
print (colored[0:10])
plt.scatter(tocluster[4],tocluster[1],  color = colored)
for ci,c in enumerate(centers):
    plt.plot(c[0], c[1], 'o', markersize=8, color='red', alpha=0.9, label=''+str(ci))

plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()
#聚类图

clust_prod = cust_prod.copy()
clust_prod['cluster'] = c_preds

clust_prod.head(10)

print (clust_prod.shape)
f,arr = plt.subplots(2,2,sharex=True,figsize=(15,15))
#plt.subplots 作图
c1_count = len(clust_prod[clust_prod['cluster']==0])

c0 = clust_prod[clust_prod['cluster']==0].drop('cluster',axis=1).mean()
arr[0,0].bar(range(len(clust_prod.drop('cluster',axis=1).columns)),c0)
c1 = clust_prod[clust_prod['cluster']==1].drop('cluster',axis=1).mean()
arr[0,1].bar(range(len(clust_prod.drop('cluster',axis=1).columns)),c1)
c2 = clust_prod[clust_prod['cluster']==2].drop('cluster',axis=1).mean()
arr[1,0].bar(range(len(clust_prod.drop('cluster',axis=1).columns)),c2)
c3 = clust_prod[clust_prod['cluster']==3].drop('cluster',axis=1).mean()
arr[1,1].bar(range(len(clust_prod.drop('cluster',axis=1).columns)),c3)
plt.show()
#四类人购买种类偏向图，x轴代表商品种类 ，y轴可以理解为购买意向

#c0.sort_values(ascending=False)[0:10]分别代表四类人的购买倾向
#c1.sort_values(ascending=False)[0:10]
#c2.sort_values(ascending=False)[0:10]
#c3.sort_values(ascending=False)[0:10]

cluster_means = [[c0['fresh fruits'],c0['fresh vegetables'],c0['packaged vegetables fruits'], c0['yogurt'], c0['packaged cheese'], c0['milk'],c0['water seltzer sparkling water'],c0['chips pretzels']],
                 [c1['fresh fruits'],c1['fresh vegetables'],c1['packaged vegetables fruits'], c1['yogurt'], c1['packaged cheese'], c1['milk'],c1['water seltzer sparkling water'],c1['chips pretzels']],
                 [c2['fresh fruits'],c2['fresh vegetables'],c2['packaged vegetables fruits'], c2['yogurt'], c2['packaged cheese'], c2['milk'],c2['water seltzer sparkling water'],c2['chips pretzels']],
                 [c3['fresh fruits'],c3['fresh vegetables'],c3['packaged vegetables fruits'], c3['yogurt'], c3['packaged cheese'], c3['milk'],c3['water seltzer sparkling water'],c3['chips pretzels']]]
cluster_means = pd.DataFrame(cluster_means, columns = ['fresh fruits','fresh vegetables','packaged vegetables fruits','yogurt','packaged cheese','milk','water seltzer sparkling water','chips pretzels'])

#输出四类人对于购买最多的几类商品的购买倾向表

cluster_perc = cluster_means.iloc[:, :].apply(lambda x: (x / x.sum())*100,axis=1)
#每类人购买某个种类商品的概率
