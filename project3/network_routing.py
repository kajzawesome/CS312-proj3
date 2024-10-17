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
        del(next(reversed(self.unsortedArray.items())))
        return u

    def pop(self,node):
        del(self.unsortedArray[node])




class BinaryMinHeap:
    nodes: list[int]

    def __init__(self, nodes: list[int] =  []):
        self.nodes = []
        for node in nodes:
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
        self.update_key()

    def swap(self, first_idx: int, second_idx: int):
        temp = self.nodes[first_idx]
        self.nodes[first_idx] = self.nodes[second_idx]
        self.nodes[second_idx] = temp

    def update_key(self):
        position: int = len(self.nodes) - 1
        while (self.has_parent(position) and self.parent(position) > self.nodes[position]):
            self.swap(self.get_parent_index(position),position)
            position = self.get_parent_index(position)




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
    dist = dict(int, int)
    for u in graph:
        dist[u] =  float('inf')
    dist[source] = 0
    Q = unsorted(source,0)
    nodesVisited: list
    nodesVisited.add(source)
    while Q is not None:
        u = Q.pop()
        for v in graph[Q]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + graph[u][v]
                Q.push(v,dist[v])
        if u == target:
            break
        else:
            nodesVisited.add(u)
    return nodesVisited, dist[u]



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
    dist = map(int, int)
    for u in graph:
        dist[u] =  float('inf')
    dist[source] = 0
    Q: binaryHeap = __init__(source,0)
    while Q is not None:
        u = Q.pop()
        for v in graph[Q]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + graph[u][v]
                push(Q,v)