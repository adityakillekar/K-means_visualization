#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:29:40 2019

@author: adityakillekar
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as manimation
from scipy.spatial import distance
from sklearn.datasets.samples_generator import make_blobs


def incremental_farthest_search(pts, k):
    remaining_points = pts.tolist()[:]
    solution_set = []
    solution_set.append(remaining_points.pop(random.randint(0, len(remaining_points) - 1)))
    for _ in range(k-1):
        distances = [distance.cdist([p], [solution_set[0]]) for p in remaining_points]
        for i, p in enumerate(remaining_points):
            for j, s in enumerate(solution_set):
                distances[i] = min(distances[i], distance.cdist([p], [s]))
        solution_set.append(remaining_points.pop(distances.index(max(distances))))
    return np.asarray(solution_set)


def k_means(dataset,k, filename, tol=0.0000000000000005, smart_init=False):
    # Set up formatting for the movie files
    Writer = manimation.writers['ffmpeg']
    metadata = dict(title='K-means Visualization', artist='Aditya Killekar', comment='K-means')
    writer = Writer(fps=30, metadata=metadata)
    
    #Initialize the centroids
    if smart_init:
        centroids = incremental_farthest_search(dataset, k)
    else:
        centroids = np.zeros((k,dataset.shape[1]))  
        
    old_centroids = np.ones(centroids.shape)
    label_dict = dict.fromkeys([i for i in range(k)], 0)
    print("Iteration number: 0")
    print(label_dict)
    print()
        
    #Initialize the labels
    labels = np.full(dataset.shape[0], 10)
    #Number of iterations
    iter_num = 1
    
    fig = plt.figure(filename)
    if smart_init:
        plt.title('K-means Visualization with Smart centroid initialization')
    else:
        plt.title('K-means Visualization with Zero centroid initialization')
    plt.xlabel('x')
    plt.ylabel('y')
    
    with writer.saving(fig, filename, 500):
        #Actual iterator
        plt.scatter(dataset[:,0],dataset[:,1],c=labels)
        m = plt.scatter(centroids[:,0],centroids[:,1], c ='orange')
        writer.grab_frame()
        m.remove()
        writer.grab_frame()
        while np.linalg.norm(centroids-old_centroids) > tol:
            print("Iteration number: {}".format(iter_num))
            for i in range(dataset.shape[0]):
                min_dist = float('inf')
                for j in range(k):
                    ed = np.linalg.norm(centroids[j]-dataset[i])
                    if ed < min_dist:
                        min_dist = ed
                        labels[i] = j
                        
            old_centroids = np.copy(centroids)
            unique, counts = np.unique(labels, return_counts=True)
    
            for i,j in zip(unique,counts):
                label_dict[i] = j
            print("Labels:",label_dict)
    
            for i in range(k):
                sums_x = np.sum(dataset[np.where(labels == i),0])
                sums_y = np.sum(dataset[np.where(labels == i),1])
                if label_dict[i] != 0:
                    centroids[i] = [sums_x/label_dict[i], sums_y/label_dict[i]]
            iter_num += 1
            print()
            
            plt.scatter(dataset[:,0],dataset[:,1],c=labels)
            m = plt.scatter(centroids[:,0],centroids[:,1], c ='orange')
            writer.grab_frame()
            writer.grab_frame()
            m.remove()
            writer.grab_frame()
        m = plt.scatter(centroids[:,0],centroids[:,1], c ='red')
        writer.grab_frame()
        plt.close()
        final_ed = 0
        for i in range(k):
            final_ed += sum(distance.cdist(dataset[np.where(labels == i)],[centroids[i]], metric='euclidean'))
    return centroids, labels, final_ed, iter_num

#Generating the synthetic data
N = 600 #Number of data samples
K = 6 #Number of actual clusters
data, _ = make_blobs(n_samples=N, centers=K, cluster_std=1.5, random_state=0) #Generate synthetic data

#Range of unknown "k"
k = 14
eds = np.zeros(k)
num_iter = np.zeros(k)

#K_means with different number of clusters size(k)
for i in range(1,k):
    centroids, labels, eds[i], num_iter[i] = k_means(data, i, filename="Random.mp4", smart_init=True)
fig = plt.figure()
plt.title('Elbow method to find optimal number of clusters')
plt.plot(range(1,k),eds[1:])
plt.ylabel('Sum of L2-norms')
plt.xlabel('Number of clusters (k)')
plt.savefig('Optimal_k.png', dpi=500)

    
#centroids1, labels1, ed1, num1 = k_means(data, K, smart_init=False, filename="k_means_visualization_no_init.mp4")
#centroids2, labels2, ed2, num2 = k_means(data, K, smart_init=True, filename="k_means_visualization_with_init.mp4")
#
#fig = plt.figure()
#plt.title('Number of iteration to convergence')
#plt.ylabel('Number of iterations')
#plt.bar(['Zero centroid initialization','Smart centroid initialization'],[num1,num2])
#plt.savefig('Convergence.png', dpi=500)