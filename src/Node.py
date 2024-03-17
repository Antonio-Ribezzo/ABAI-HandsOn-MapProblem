#creiamo un nodo a cui associamo lo stato, il genitore, l'azione, il costo e la lunghezza
#esempio per creare il primo nodo del nostro albero: node = Node(state='Corato', parent=None, action=None, cost=1, depth=1)
class Node:
    def __init__(self, state, parent, action, cost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    # built-in function che ritorna una stringa e serve per vedere in console la rappresentazione dell'oggetto
    def __repr__(self):
        return f'({self.state})'


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

    def path(self):
        path = []
        node = self
        while node.parent:
            path.append(node.action)
            node = node.parent
        path = list(reversed(path))
        return path