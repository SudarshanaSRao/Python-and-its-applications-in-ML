pip install plotly

path = '' # Paste the file location of the datasets. 
import numpy as np
import pandas as pd

# Clustering of genes



x_unsup = np.load(path + 'X_unsup.npy')
x_unsup = np.array(x_unsup)
df_unsup = pd.DataFrame(x_unsup)
df_unsup.shape

import matplotlib.pyplot as plt
plt.figure(figsize = (8, 8))
df_unsup[19995].plot(kind = 'hist')
plt.grid()
plt.show() 
df_unsup.skew() # Evident that data is non-linear.

# ***Log transformation is applied to handle skewed data***

df_log = np.log2(df_unsup + 1)
plt.figure(figsize = (8, 8))
df_log[19995].plot(kind = 'hist')
plt.grid()
plt.show()
df_log.skew()

from sklearn.decomposition import PCA
pca = PCA(n_components = 3).fit_transform(df_log)
pca.shape

plt.figure(figsize = (10, 10))
ax = plt.axes(projection = '3d')
ax.scatter(pca[:, 0], pca[:, 1], pca[:, 2], s = 50)
plt.show()

from sklearn.cluster import KMeans
cost = []
K = range(1, 10)
for k in K :
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(pca)
    cost.append(kmeans.inertia_)

plt.figure(figsize = (8, 8))
plt.plot(K, cost)
plt.xlabel('Number of clusters')
plt.ylabel('Cost Function')
plt.title('Elbow Method')
plt.grid()
plt.show()

# ***The above graph shows that the optimal number of clusters for KMeans is 3***

clusters = KMeans(n_clusters = 3).fit_predict(pca)
df_pca = pd.DataFrame(pca)
set(clusters)

clust = clusters.tolist()
df_pca['Cluster'] = clust
clust0 = df_pca[df_pca['Cluster'] == 0]
clust1 = df_pca[df_pca['Cluster'] == 1]
clust2 = df_pca[df_pca['Cluster'] == 2]
df_pca.columns = ['X', 'Y', 'Z', 'Cluster']
df_pca

import plotly.express as px
fig = px.scatter_3d(df_pca, x = 'X', y = 'Y', z = 'Z', color = 'Cluster')
fig.show()

# Multi-class Classification.



from sklearn.preprocessing import StandardScaler
df_scaled = StandardScaler().fit_transform(df_unsup)
x_train = np.load(path + 'X_train.npy')
x_sup = StandardScaler().fit_transform(x_train)
df_scaled.shape

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
cluster_label = pd.DataFrame(clusters)
x_train,  x_test, y_train, y_test = train_test_split(df_scaled, cluster_label.values.ravel(), test_size = 0.2)
model = LogisticRegression(multi_class = 'ovr', solver = 'liblinear')
model.fit(x_train, y_train)

from sklearn.metrics import plot_confusion_matrix
y_class = model.predict(x_test)
plot_confusion_matrix(model, x_test, y_test)
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test, y_class))

# Basic Logistic Regression.

y_train = np.load(path + 'y_train.npy')
y_test = np.load(path + 'y_test.npy')
x_train = np.load(path + 'X_train.npy')
x_test = np.load(path + 'X_test.npy')
x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)
df_x = pd.DataFrame(x_train)
df_y = pd.DataFrame(y_train)

df_x.describe()

df_y.describe()

from sklearn.preprocessing import StandardScaler
df_x = StandardScaler().fit_transform(df_x)
x_test = StandardScaler().fit_transform(x_test)
df_x

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter = 250)
model.fit(df_x, df_y)

from sklearn.metrics import accuracy_score, mean_squared_error
y_prdct = model.predict(x_test)
print('Mean square error:', mean_squared_error(y_test, y_prdct))
print('Accuracy: %.2f'%(accuracy_score(y_test, y_prdct) * 100), '%')

from matplotlib import pyplot as plt 
plt.figure(figsize = (8, 8))
plt.scatter(y_test, y_prdct)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.grid()
plt.show()

