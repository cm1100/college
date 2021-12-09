#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Taking Input
#insert number of vertices
def inputGraph():
    v=int(input("Enter the number of nodes"))
    e=int(input("Enter number of edges"))
    node={}
    graph={}
    
    for i in range(0,v):
        u=input("Enter Node "+str(i+1)+" Name ")
        graph[u]=[]
        node[u]=-1
            
    for i in range(0,e):
        u=input("Edge "+str(i)+" (from)- ")
        v=input("Edge "+str(i)+" (to)- ")
        graph[u].append(v)
        graph[v].append(u)
        
    for i in node.keys():
        if i not in graph:
            graph[i]=[]
        
    print(node)
    print(graph)
    return node,graph


# In[2]:


def checkValidColor(src,graph,nodes,i):
    
    for nbr in graph[src]:
            if nodes[nbr]==i:
                return False
    return True


# In[3]:


def colorGraph(color,src,nodes,graph):
        
        for i in color.keys():
            if checkValidColor(src,graph,nodes,i):
                nodes[src]=i
            
        
        for nbr in graph[src]:
            if nodes[nbr]==-1:
                colorGraph(color,nbr,nodes,graph)


# In[ ]:





# In[6]:


nodes,graph=inputGraph()
color={
    1: "Red",
    2: "Blue",
    3: "Yellow",
    4: "Green",
    5: "White",
    6: "Black",
}
src=input("Enter starting Node- ")
colorGraph(color,src,nodes,graph)

colorUsed=set()

for i in nodes.keys():
    print(i+" -  "+color[nodes[i]])
    colorUsed.add(nodes[i],)

print(colorUsed)

print("Chromatic Number- " +str(len(colorUsed)) )


# In[ ]:




