class BreadthFirst:

    def add_visited(self,state):
        pass
    def select(self, fringe, new_nodes):
        return new_nodes + fringe

class DepthFirst:
    def add_visited(self,state):
        pass
    def select(self,fringe, new_nodes):
        return fringe + new_nodes

class GraphBreadthFirst:
    def __init__(self):
        self.visited = set()
    def add_visited(self,state):
        self.visited.add(state)
    def select(self, fringe, new_nodes):
        fringe = new_nodes + fringe
        fringe = [n for n in fringe if n.state not in self.visited]
        return fringe

class GraphDepthFirst:
    def __init__(self):
        self.visited = set()
    def add_visited(self,state):
        self.visited.add(state)
    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        return fringe

# creare la depth limited search