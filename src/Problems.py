class StreetProblem:
    #constructor
    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    #definisco la funzione actions che
    #prende come parametro lo stato attuale
    #la possibile azione dello state Ad esempio 'Corato'
    #sarà ciò che è presente nel dictionary "environment"
    #corrispondente alla chiave Corato
    def actions(self, state):
        return self.environment[state]

    #ritorna lo state e l'action
    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    #implemento il transition model
    #se ho come state in input Ruvo e come action ho Corato
    #come returno voglio "vado a Corato"
    #in questo caso hanno lo stesso nome
    def result(self, state=None, action=None):
        return action

    #se abbiamo raggiunto il goal lo ritorniamo
    def goal_test(self, state):
        return state == self.goal_state

    #cost function (per il momento non ci interessa e ritorniamo 1)
    def cost(self, state, action):
        return 1