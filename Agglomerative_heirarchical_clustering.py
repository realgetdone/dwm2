import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x, y))
print(data)
linkage_data = linkage(data, method='single', metric='euclidean')
dendrogram(linkage_data)
plt.show()
# Perform Agglomerative Clustering to get labels
agg_clustering = AgglomerativeClustering(n_clusters=2)  # You can change n_clusters as needed
labels = agg_clustering.fit_predict(data)
plt.scatter(x, y, c=labels)
plt.show()