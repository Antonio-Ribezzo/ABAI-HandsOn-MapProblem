from src.Node import Node
class TreeSearch:
    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []

    def run(self):
        # first node
        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)
        # loop
        while True:
            # check the goal test
            if self.problem.goal_test(node.state):
                return 'Ok', node.path()
            # add visited for the graph search
            self.strategy.add_visited(node.state)

            # expand the node
            # creo prima lo state
            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s,
                                     action=a)for s, a in new_states]

            # select the new node
            # the fringe is the result of our strategy
            self.fringe = self.strategy.select(self.fringe, new_nodes)

            # check if is empty
            if len(self.fringe) == 0:
                return 'Fail', []

            node = self.fringe.pop() # pop takes the last element of the list

