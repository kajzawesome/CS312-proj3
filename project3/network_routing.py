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


class  unsortedArray:
    def __init__(self, location, node, cost):
        self.location = location
        self.node = node
        self.cost = cost                                                          

    def getCost(self):
        return self.cost

    def remove(self):
        del(self)

class binaryHeap:
    def __init__(self, node, child1, child2, cost1, cost2):
        self.node = node
        self.cost1 = cost1
        self.cost2 = cost2
        self.child1 = child1
        self.child2 = child2

    def isLast(self) -> bool:
        if self.child1() is None and self.child2() is None:
            return True
        else:    
            return False

    def isParentBigger(self):
        if self.isLast() is not True:
            if self.child1 < self.node:
                temp = self.child1
                self.child1 = self.node
                self.node = temp
            else: 
                if self.child2 < self.node:
                    temp = self.child2
                    self.child2 = self.node
                    self.node = temp 