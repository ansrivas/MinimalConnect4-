# -*- coding: utf-8 -*-
"""
Created on Sun May 18 02:20:16 2014


"""

#Change the number of ROWS and COLUMNS here for your graph
COLUMN = 20
ROW = 20
#COLUMN = 35
#ROW = 22


#Give source and destination values
SOURCE = (0,10)
DEST = (15,1)

import math
import networkx as nx
import matplotlib.pyplot as plt
import propython as profiler

pos = None

def read_file_draw_graph():
    global pos
    with open('sample.txt') as file:
        array2d = [[int(digit) for digit in line.split()] for line in file]
    
    count = 1 
    G = nx.Graph()    
    for j in range(COLUMN):
        for i in range(ROW):
            if array2d[ROW-1-i][j] == 0:
                G.add_node(count,pos=(j,i))
            count +=1 
     
  
    pos=nx.get_node_attributes(G,'pos')
    
    
    for index in pos.keys():
        for index2 in pos.keys():
            if pos[index][0] == pos[index2][0] and pos[index][1] == pos[index2][1] -1 :
                G.add_edge(index,index2,weight=1)
            if pos[index][1] == pos[index2][1] and pos[index][0] == pos[index2][0] -1 :
                G.add_edge(index,index2,weight=1)
    
    return G
 

def heuristics(a,b):
     global pos
     x1,y1 = pos[a]
     x2,y2 = pos[b]   
     return ((y2-y1)**2 + (x2-x1)**2) **0.5
     
def minimum_distance_node(unvisited_nodes,destination):
    
    
    nodeIndex = None
    minDistance = float("inf")
    #pos=nx.get_node_attributes(G,'pos')
    for k in unvisited_nodes:
        
        #Finding the Heuristic value
        heuristic_value = heuristics(k,destination)
     
        actual_value = G.node[k]['distance']
        
        #Summing actual and heuristic value
        total_value = heuristic_value + actual_value
        
        if  total_value < minDistance:
            minDistance = total_value
            nodeIndex = k
    return nodeIndex,minDistance
 
  
def astar(G,source,destination):

    total_nodes = G.nodes()
    paths = {source:[source]}
    fringe=[]
    fringe.append(source)
    #heuristic_value=[]
    #total_value=[]
    
    #making distances of all nodes to INF
    for n in total_nodes:
         G.add_node(n,distance=float("inf"),visited=False)
    node_distance = nx.get_node_attributes(G,'distance') 
    
    #Exception for source for INF
    G.add_node(source,distance=0,visited=True)

    while len(fringe) !=0:
        minDistNodeIndex, distanceMin = minimum_distance_node(fringe,destination)
        
        if ( minDistNodeIndex == destination):
            break

        G.add_node(minDistNodeIndex,visited=True)
        
        #mark this node visited and remove from nodes for consideration
        neighbors = G.neighbors(minDistNodeIndex)
        fringe.remove(minDistNodeIndex)      
        
        
        unvisited_neighbors = [neighbor for neighbor in neighbors if G.node[neighbor]['visited'] == False ]
              
        for n in unvisited_neighbors:
            #find the weight of the minDistnodeIndex here
            edge_data_of_node = G.get_edge_data(minDistNodeIndex,n)
            new_actual = distanceMin + edge_data_of_node['weight']
       
            if  new_actual < node_distance[n] and n not in fringe:
                #print "updating distances"
                node_distance[n] = distanceMin + new_actual
                
                #heuristic values
                heuristic_value = heuristics(n,destination)
                
                #adding actual and heuristic
                total_value = heuristic_value + node_distance[n]
                G.add_node(n,distance=total_value)
                paths[n] = paths[minDistNodeIndex] + [n]
                if n not in fringe:
                    fringe.append(n)
              
    return G,paths  
    
    
    
if __name__ == "__main__":
   
    
        
    
    G = read_file_draw_graph()
    for n in G.nodes():
        if G.node[n]['pos'] == SOURCE:
            source = n 
        if G.node[n]['pos'] == DEST:
            destination = n
    
    print source, destination
    
    #Uncomment this to profile your code
    '''
    t1 = 0
    for i in range(0,1000):
        timer = profiler.timewith()
        G, paths = astar(G,SOURCE,DEST)
        t1 += timer.checkpoint()
    
    print t1/1000  #0.0156180000305
    '''
    
    G, paths = astar(G,source,destination)   
    print paths[destination]
    l=paths[destination]
    
    nx.draw(G,pos)
    nx.draw(G,pos,nodelist =l,node_color = 'g')
    plt.show()
    