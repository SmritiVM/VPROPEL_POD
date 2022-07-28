cons = {1: [2, 5, 7, 9], 2: [1, 4], 5: [1, 3, 6], 4: [2, 6], 3: [5], 6: [5, 4], 7: [1, 8, 10], 8: [7], 9: [1, 10], 10: [9, 7, 11], 11: [10, 12], 12: [11]}

def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        return 0
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    return len(new_path)-1
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    return None
k = int(input())
l = int(input())
length = BFS_SP(cons,k,l)
print(length)
