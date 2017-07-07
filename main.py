'''

written by Sihyun Jeong (sihyunj@snu.ac.kr)

'''
from collections import defaultdict
import tsp
import socialstatus as ss


if __name__ == '__main__':
    
    
    f = open("edgelist.txt","r")
    
    
    # reading node list and edge list of whole network
    nodes = set()
    egonet = defaultdict(set)
    lines = f.readlines()
    f.close()
    for l in lines:
        tmp = l.strip('\n').strip('\r').split('\t')
        nodes.add(tmp[0])
        nodes.add(tmp[1])
        
        #making ego-network edge set of every ego node
        egonet[tmp[0]].add((tmp[0],tmp[1]))
        egonet[tmp[1]].add((tmp[0],tmp[1]))
       
            
    #1-1. triad count 
    total_census = tsp.triad_count(egonet,nodes)
    
    
    #1-2. Z score computation
    tsp.zscore(egonet,total_census,nodes)
  
        
    #2-1. status computation 
    statusdict = ss.status_comp(lines)
    
    #2-2. positive link probability
    ss.plp(egonet,statusdict)
    
    
    