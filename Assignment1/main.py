edges = [['A', 'B', 5], ['B', 'C', 4], ['C', 'D', 8], ['D', 'C', 8], ['D', 'E', 6], ['A', 'D', 5], ['C', 'E', 2],['E', 'B', 3], ['A', 'E', 7]]

edges_Dictionary = {
    'A': [['B', 5], ['D', 5], ['E', 7]],
    'B': [['C', 4]],
    'C': [['D', 8], ['E', 2]],
    'D': [['C', 8], ['E', 6]],
    'E': [['B', 3]]
}

route = ['C', 'D', 'C']
distance_covered = 0
route_Step = 0
fromNode = route[route_Step]
toNode = route[route_Step + 1]

train = True
while train:
    for edge in edges:
        if edge[0] is fromNode:
            if edge[1] is toNode:
                distance_covered += edge[2]
                route_Step += 1

                fromNode = route[route_Step]
                if route_Step + 1 < len(route):
                    toNode = route[route_Step + 1]

                if fromNode is route[len(route) - 1]:
                    train = False

print('The route is : ' + str(route))
print(f'For this route, Total distance is : ' + str(distance_covered), '& Total stops are : ' + str(route_Step))


routes = ['A', 'C']
routeStep = 0
initial_Node = routes[routeStep]
final_Node = routes[len(routes) - 1]
Possible_Route = edges_Dictionary[initial_Node]
list_train = []
whileFlag = True
distance_between = 0
path_covers = ""
while whileFlag:
    for node in Possible_Route:
        distance_between = 0
        path_covers = initial_Node + " - "
        List = []
        if final_Node is not node[0]:
            cur_Node = node[0]
            for edge in edges:
                if edge[0] is cur_Node:
                    if edge[1] is final_Node:
                        distance_between = distance_between + int(node[1])
                        distance_between = distance_between + edge[2]
                        path_covers = path_covers + node[0] + " - " + edge[1]
                        List.insert(0, path_covers)
                        List.insert(1, distance_between)
                        list_train.append(List)
                        break
                    else:
                        end_node = edge[1]
                        for InEdge in edges:
                            if InEdge[0] is end_node:
                                if InEdge[1] is final_Node:
                                    distance_between = distance_between + int(node[1])
                                    distance_between = distance_between + InEdge[2] + edge[2]
                                    path_covers = path_covers + node[0] + " - " + end_node + " - " + InEdge[1]
                                    List.insert(0, path_covers)
                                    List.insert(1, distance_between)
                                    list_train.append(List)
                                    break

            whileFlag = False
        else:
            whileFlag = False
print(f'The possible routes from {initial_Node} to {final_Node} are as :-')
shortest_Distance = 0
i = 0
j = 0
for paths in list_train:
    i + 1
    print(f'For the path : {paths[0]}  &  the distance is : {paths[1]}')
    if shortest_Distance > paths[1] or shortest_Distance == 0:
        shortest_Distance = paths[1]
        i = j

shortDist = list_train[j]
print(f'The shortest path is : {shortDist[0]} having distance : {shortest_Distance}')
