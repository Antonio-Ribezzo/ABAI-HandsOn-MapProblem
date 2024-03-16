class Problem:
    #constructor
    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    # ritorna lo state e l'action
    def successors(self, state):
        possible_actions = self.actions(state)
        # return the state with the action
        return [(self.result(state, a), a) for a in possible_actions]

    # definisco la funzione actions che prende come parametro lo stato attuale
    # per esempio se mi trovo ad Andria mi deve restiruire Corato e Trani che sono le azioni
    def actions(self, state):
        # restituisce una lista
        return self.environment[state]

    #implemento il transition model, se ho come state in input Andria e come action ho Corato
    #come return voglio "vado a Corato" in questo caso hanno lo stesso nome ma in realtà voglio il new_state
    def result(self, state=None, action=None):
        return action

    # se abbiamo raggiunto il goal restituisce true altrimenti false
    # esempio: map_problem.goal_test('Corato') -> true se il goal_state = 'Corato
    def goal_test(self, state):
        return state == self.goal_state

    #cost function (per il momento non ci interessa e ritorniamo 1)
    def cost(self, state, action):
        return 1