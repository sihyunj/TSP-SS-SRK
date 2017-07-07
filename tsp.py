
'''

written by Sihyun Jeong (sihyunj@snu.ac.kr)

'''

import triadic
import networkx as nx
import numpy
import math
from collections import defaultdict


#1-1. triad count (ref: https://github.com/maksim2042/SNABook/blob/master/chapter4/triadic.py)
def triad_count(egonet,nodes):
    
    wf = open("triad_count.txt","w")
    total_census = defaultdict(list)
    
    
    for n in nodes:
        
        G = nx.DiGraph()
        
        G.add_edges_from(egonet[n])
        
        census, node_census = triadic.triadic_census(G)
    
        # output format : id(tab)201(tab)021C(tab)...
        
        wf.write(n)
        
        for k in census.keys():
            wf.write('\t')
            wf.write(str(census[k]))
            
            #if k in total_census.keys():
            total_census[k].append(census[k])
            #else:
             #   total_census[k] = census[k]
               
        wf.write('\n')
        
        G.clear()
    
    wf.close()
    return total_census
    
#1-2. Z score computation
def zscore(egonet,total_census,nodes):
   
    # average and stanard deviation of triad count (census) is originally for a null model (ex. random network or legitimate user network)
    # In this example, I used average and standard deviation as 1 and 0.5 
    
    wf = open("zscore.txt","w")
    
    average_census = dict()
    std_census = dict()
    
    for k in total_census.keys():
        average_census[k] = 1 # numpy.mean(total_census[k]) 
        std_census[k] = 0.5 # math.sqrt(numpy.var(total_census[k]))
        del total_census[k]
        
    
    
    for n in nodes:
        
        G = nx.DiGraph()
        
        G.add_edges_from(egonet[n])
        
        census, node_census = triadic.triadic_census(G)
    
        # output format (zscore): id(tab)201(tab)021C(tab)...
        
        wf.write(n)
        
        for k in census.keys():
            wf.write('\t')
            
            zscore = float(census[k] - average_census[k])/float(std_census[k])
            wf.write(str(zscore))
           
               
        wf.write('\n')
        
        G.clear()
    wf.close() 