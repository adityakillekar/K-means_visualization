# K-means Clustering Visualization
This directory contains the visualization code for K-means clustering using synthectically generated data.
The data with K clusters can be formed using the driver code at the end of k_means_visualization.py file.
The function in this file also creates a video of how the K-means clustering progress. There is an option
to initialize the centroids in an intuitive manner instead of zero initializing the centroids. The algorithm used for intuitive
centroid intialization is called "The Farthest Neighbor Algorithm". The functions also generates the Elbow diagram to exactly know the
optimum number of clusters in the actual dataset. Finally, we can comapare the convergence rate (Number of interations) with intuitive centroid initialization
and zero initialized centroids.

An example is displayed below:
The figure below plots the synthetically generated data with 6 clusters (k=6).
<img width="1077" alt="Screen Shot 2019-03-19 at 12 06 55 PM" src="https://user-images.githubusercontent.com/32280293/54634740-0db77500-4a40-11e9-8e3a-cfcee2127bc2.png">

The Elbow diagram that correctly gives us the optimum number of clusters (k)
![Optimal_k](https://user-images.githubusercontent.com/32280293/54634765-17d97380-4a40-11e9-8cc3-cbcc949b92c1.png)

The final clustering with k=6.
<img width="1074" alt="Screen Shot 2019-03-19 at 12 12 46 PM" src="https://user-images.githubusercontent.com/32280293/54635046-96ceac00-4a40-11e9-9b6e-46f4da8fdb2b.png">

The figure below clearly shows that the centroid initialization plays an important role in immediate convergence (in terms of number of iterations).
![Convergence](https://user-images.githubusercontent.com/32280293/54634181-e44a1980-4a3e-11e9-9ecc-08ea29dfed50.png)

There are many other ways of finding the optimum K and centroid initialization. But that's not the goal of this experiment. The goal of this experiment is to see how the centroids move on every iteration and visually understand how K-means work. The video for the same can be found in the code directory.
