import numpy as np
import scipy.sparse as ssp
from graphLib import Graph
from itertools import combinations
import matplotlib.pyplot as plt

#=================== Task 1: Compute Graph Properties ===================

#------------- Task 1.1: compute degree distribution
def compute_deg_distr(graph):
    # compute the degree distribution of the input graph
    # return two array's
    # degs: all the possible node degrees, in ascending order
    # counts: the corresponding counts (number of nodes) for each degree value in degs
   
    # get the degree sequence of all the nodes
    deg_seq = graph.get_deg_seq()

    # get degree and its corresponding count
    # using np.unique(); check documentation
    #degs, counts = np.unique()
    degs = []
    counts = []
    
    return degs, counts

#------------ Task 1.2: compute clustering coefficient
def get_cc_local(graph,nid):
    
    # get the neighbors of node nid
    nbrs = []
    
    # number of neighbors of node nid 
    deg = 0

    # get adjacency matrix of graph in dense form
    adj_matrix = []

    # all possible pairs of neighbors of nid
    all_pairs = 0
    
    # number of connected pairs of neighbors
    closed_pairs = 0
        
    if deg < 2:
        return 0.0
    else:
        # enumerate all pairs of neighbors
        comb = combinations() 

        for node_pair in list(comb):              
            # check if this pair of nodes are connected and update closed_pairs
            closed_pairs = 0

        # return local clustering coefficient
        return 0

def get_cc_global(graph):
    adj_matrix = []
    
    # number of closed 2-pth
    closed_2_path = 0
    
    # number of 2-path 
    all_2_path = 1
    
    #loop over all nodes
    for i in range(graph.n):
        # get the neighbors of node i
        nbrs = []
        nbrs_num = 0
        if nbrs_num >= 2:
            # enumerate all pairs of neighbors
            comb = combinations()                      
            for node_pair in list(comb):
                # update all_2_path
                all_2_path = 0

                #update closed_2_path
                closed_2_path = 0

    # return global clustering coefficient
    return 0

# --------------------- Task 1.3: compute diameter
def distance_BFS(adj_list, s):
    # return the distance of s to every node
    # travel the graph from s using BFS; this is will create a tree rooted at s
    # the hight of the tree is the longest distance

    n = len(adj_list)

    # use a vector to record if a node is visited or not
    visited = [False] * n   
    visited[s] = True
    
    # store the distance from s to all other nodes
    distance = np.zeros(n, dtype = int)
    distance[s] = 0
    
    # current layer of nodes
    current_level = [s]
    # next layer of nodes
    next_level = []

    # the number of layers
    depth = 0
    
    # while current layer is not empty
    while len(current_level)>0:
        for node in current_level: # each node in current layer
            nbrs = []
            for nbr in nbrs: #for each neighbor of this node
                # add a neighbor into next layer, if the neighbor is not visited yet
                nbr = 0
                
                # remember to update visited


        # update depth
        depth = 0
        # update distance from s to all nodes in the next_level
        for child in next_level:
            distance[child] = 0

        # set current_level as next_level
        current_level = []
        # empty next_level
        next_level = []

    return distance

def get_diameter(graph):
    adj_list = graph.get_adj_list()

    diameter = -1

    # treat every node in graph as the source node
    # call distance_BFS() to get the distance
    # find the max distance
    for source in range(graph.n):
        source = 0


    return diameter
