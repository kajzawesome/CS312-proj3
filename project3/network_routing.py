class  unsorted:
    unsortedArray = dict[int,float]

    def __init__(self):
        self.unsortedArray = {
            None: None
        }

    def __init__(self,node, cost):
        self.unsortedArray = {
            node: cost
        }

    def push(self, node, cost):
        self.unsortedArray[node] = cost

    def pop(self):
        u = next(reversed(self.unsortedArray.items()))
        del(self.unsortedArray[u[0]])
        return u

    def pop(self):
        lowest = float("inf")
        for node in self.unsortedArray:
            if lowest > self.unsortedArray[node]:
                lowest = node
        del(self.unsortedArray[lowest])
        return lowest




class BinaryMinHeap:
    nodes: list[int]

    def __init__(self, nodes: list[int] =  []):
        self.nodes = []
        for node in nodes:
            self.add(node)

    def __init__(self, node: int):
        self.nodes = []
        self.add(node)

#helper functions
    def get_left_child_index(self, parent_index: int):
        return 2 * parent_index + 1
    def get_right_child_index(self, parent_index: int):
        return 2 * parent_index + 2
    def get_parent_index(self, child_index: int):
        return (child_index -1) // 2

    def has_left_child(self, parent_index: int) -> bool:
        return self.get_left_child_index(parent_index) < len(self.nodes)
    def has_right_child(self, parent_index: int) -> bool:
        return self.get_right_child_index(parent_index) < len(self.nodes)
    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) >= 0

    def parent(self, index: int):
        return self.nodes[self.get_parent_index(index)]
    def left_child(self, index: int):
        return self.nodes[self.get_left_child_index(index)]
    def right_child(self, index: int):
        return self.nodes[self.get_right_child_index(index)]

#functions to construct and edit tree to keep min on top/first element
    def add(self, item:int):
        self.nodes.append(item)
        position: int = len(self.nodes) - 1
        self.heapify_up(position)

    def swap(self, first_idx: int, second_idx: int):
        temp = self.nodes[first_idx]
        self.nodes[first_idx] = self.nodes[second_idx]
        self.nodes[second_idx] = temp

    def heapify_up(self, position):
        if (self.has_parent(position) and self.parent(position) > self.nodes[position]):
            self.swap(self.get_parent_index(position),position)
            self.heapify_up(self.get_parent_index(position))

    def remove(self):
        node = self.nodes[0]
        self.nodes[0] = self.nodes[(len(self.nodes) - 1)]
        self.heapify_down(0)
        return node

    def heapify_down(self, index: int):
        smallest = index
        if (self.has_right_child(index) and self.nodes[smallest]) > self.right_child(index):
            smallest = self.get_right_child_index(index)
        if (self.has_left_child(index) and self.nodes[smallest]) > self.left_child(index):
            smallest = self.get_left_child_index(index)
        if smallest is not index:
            self.swap(index, smallest)
            self.heapify_down(smallest)




def find_shortest_path_with_array(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    dist = {}
    path = {}
    for item in graph:
        dist[item] =  float('inf')
        path[item] = None
    dist[source] = 0
    path[source] = source
    Q = unsorted(source,0)
    nodesVisited = []

    while Q is not None:
        u = Q.pop()
        if graph[u] is not None:
            for v in graph[u]:
                if dist[v] == float('inf'):
                    dist[v] = dist[u] + graph[u][v]
                    path[v] = u
                    Q.push(v,dist[v])
                elif dist[v] < dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    path[v] = u
            
            if u == target:
                break
    item = path[target]
    while item is not source:
        nodesVisited.append(item)
        item = path[item]
    bestPath = []
    for item in nodesVisited[:-1]:
        bestPath.append(item)
    return bestPath, dist[target]



def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    dist = {}
    prev = {}
    for u in graph:
        dist[u] =  float('inf')
        prev[u] = None
    dist[source] = 0
    H = BinaryMinHeap(source)
    nodesVisited = []
    nodesVisited.append(source)
    while H is not None:
        u = H.remove()
        if graph[u] is not None:
            for v in graph[u]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    H.heapify_down(0)
                    prev[v] = u
            if u == target:
                break
            else:
                nodesVisited.append(u)

    return nodesVisited, dist[target]