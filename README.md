# K-means Clustering Visualization
This directory contains the visualization code for K-means clustering using synthectically generated data.
The data with K clusters can be formed using the driver code at the end of k_means_visualization.py file.
The function in this file also creates a video of how the K-means clustering progress. There is an option
to initialize the centroids in an intuitive manner instead of zero initializing the centroids. The algorithm used for intuitive
centroid intialization is called "The Farthest Neighbor Algorithm". The functions also generates the Elbow diagram to exactly know the
optimum number of clusters in the actual dataset. Finally, we can comapare the convergence rate (Number of interations) with intuitive centroid initialization
and zero initialized centroids.

An example below displays the synthetically generated data with 6 clusters (k=6), the Elbow diagram that correctly gives us the optimum number of clusters (k) and the convergence rate in terms of number of iterations.

<img width="1077" alt="Screen Shot 2019-03-19 at 12 06 55 PM" src="https://user-images.githubusercontent.com/32280293/54634740-0db77500-4a40-11e9-8e3a-cfcee2127bc2.png">

![Optimal_k](https://user-images.githubusercontent.com/32280293/54634765-17d97380-4a40-11e9-8cc3-cbcc949b92c1.png)



![Convergence](https://user-images.githubusercontent.com/32280293/54634181-e44a1980-4a3e-11e9-9ecc-08ea29dfed50.png)
