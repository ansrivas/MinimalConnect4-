# -*- coding: cp1252 -*-
import numpy as np

nodeDict = {}
nodeSuccDict = {}
nodeUtilDict = {}
nodeMinMaxDict = {}

values = []
index = 0


def buildTree(node, level, branches=3):
    global index
    succ = []
    # if node is leaf, assign utility value
    if level == 0:
        nodeUtilDict[node] = values[index]
        index +=1
    # else, generate successors
    else:
        for i in range(branches):
            newnode = max(nodeDict.keys())+1
            nodeDict[newnode] = True
            succ.append(newnode)
       
    nodeSuccDict[node] = succ
  
    for s in succ:
    #Hardcoded the number of branches
        if s==1:
            branches = 4
        elif s == 2:
            branches = 2
        elif s == 3:
            branches = 2
        elif s == 4:
            branches = 3
        elif s == 5:
            branches = 3
        buildTree(s, level-1, branches)
        
        
        
def maxNodeUtil(node):
    if node in nodeUtilDict:
        nodeMinMaxDict[node] = nodeUtilDict[node]
        return nodeMinMaxDict[node]
    mmv = -np.inf
    for s in nodeSuccDict[node]:
        mmv = max(mmv, minNodeUtil(s))
    nodeMinMaxDict[node] = mmv
    return mmv

def minNodeUtil(node):
    if node in nodeUtilDict:
        nodeMinMaxDict[node] = nodeUtilDict[node]
        return nodeMinMaxDict[node]
    mmv = np.inf
    for s in nodeSuccDict[node]:
        mmv = min(mmv, maxNodeUtil(s))

    nodeMinMaxDict[node] = mmv
    return mmv


if __name__ == '__main__':
    l = 2
    n = 5
    values = [15,20,1,3,3,4,15,10,16,4,12,15,12,8]
    # build tree
    node = 0
    nodeDict[node] = True
    buildTree(node, l, n)
    # compute minmax value of node

    mmv = maxNodeUtil(node)
    print "Ouput value is ",mmv
    