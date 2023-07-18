import heapq

def dijkstra(graph,start):
    distances={node: float('inf') for node in graph}
    distances[start]=0
    heap=[(0,start)]



    while heap:
        currentdist,currentnode,=heapq.heappop(heap)
        if currentdist>distances[currentnode]:
            continue
        for neighbor,weight in graph[currentnode].items():
            distance=currentdist+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance,neighbor))

    return distances

def findoptimalroute(graph,start,destination):
    distances=dijkstra(graph,start)
    if distances[destination]==float('inf'):
        return None
    route=[]
    node=destination

    while node!=start:
        route.append(node)
        neighbors=graph[node]
        mindistance=float('inf')
        nextnode=None
        for neighbor,weight in neighbors.items():
            if distances[neighbor]+weight==distances[node] and distances[neighbor]<mindistance:
                mindistance=distances[neighbor]
                nextnode=neighbor

        if nextnode is None or nextnode in route:
            return None
        node=nextnode


     route.append(start)
     route.reverse()
     return route        


graph={
    'A':{'B':3,'C':99,'D':7,'E':99},
    'B':{'A':3,'C':99,'D':7,'E':99},
    'C':{'A':99,'C':99,'D':7,'E':99},
    'D':{'A':7,'C':99,'D':7,'E':99},
    'E':{'A':3,'C':99,'D':7,'E':99},
}

startlocation='A'
destinationlocation='E'

optimalroute=findoptimalroute(graph,startlocation,destinationlocation)

if optimalroute is None:
    print("No valid route exists from start to destination.")
else:
    print("Optimal route:",'->'.join(optimalroute))    
    