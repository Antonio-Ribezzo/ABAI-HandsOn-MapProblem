#creiamo un nodo a cui associamo lo stato, il genitore, l'azione,
#il costo e la lunghezza
class Node:
    def __init__(self, state, parent, action, cost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    #given the state and the action return another node of the tree
    #this function create an object of the node class
    #da questo nodo creiamo un altro nodo
    #ruvo is the state, the action is "to Corato" ritorna "Corato"
    def expand(self, state, action, cost=1):
        return Node(state=state,
                    parent=self,
                    action=action,
                    cost=self.cost + cost,
                    depth=self.depth + 1)