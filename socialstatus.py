'''

written by Sihyun Jeong (sihyunj@snu.ac.kr)

'''
   
def status_comp(lines):
    
   
     wf = open("social_status.txt","w")
     
     indegree = dict()
     outdegree = dict()
     
     for l in lines:
         
         tmp = l.strip('\n').strip('\r').split('\t')
         
         if tmp[1] in indegree.keys():
             indegree[tmp[1]] +=1
         else:
             indegree[tmp[1]] = 1

         
         if tmp[0] in outdegree.keys():
             outdegree[tmp[0]] +=1
         else:
             outdegree[tmp[0]] = 1
             
    
     nodes = set(indegree.keys()) | set(outdegree.keys())
    
     statusdict = dict()
    
     for n in nodes:
        
         if n in indegree.keys():
             incnt = indegree[n]
         else:
             incnt = 0
            
         if n in outdegree.keys():
             outcnt = outdegree[n]
         else:
             outcnt = 0
            
            
         #status = float(incnt) / float(outcnt) 
         status = float(incnt) / float(incnt+outcnt) #normalized version
        
         del indegree[n]
         del outdegree[n]
        
         statusdict[n] = status
        
  
         
         wf.write(n)
         wf.write('\t')
         wf.write(str(status))
         wf.write('\n')
         
     wf.close()
     return statusdict
         
def plp(egonet,statusdict):
    
    
    wf = open("plp.txt","w")
    
    for k in egonet.keys():
        
       
        outdegree=0
        positivelink =0
        
        for (i,j) in egonet[k]:
            if i == k:
                outdegree+=1
                
                if statusdict[i] < statusdict[j]:
                    positivelink +=1
            
        if outdegree > 0:
            plp = float(positivelink) / float(outdegree)
            
            wf.write(k)
            wf.write('\t')
            wf.write(str(plp))
            wf.write('\n')
        
        
    
    