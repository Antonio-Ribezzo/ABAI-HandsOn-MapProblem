# import the environment and other
from input.roads import roads_small
from src.Problem import Problem
from src.startegies import BreadthFirst
from src.Search import TreeSearch
# load environment
streets = roads_small

# formulate the problem
initial_state = 'Terlizzi'
goal_state = 'Bari'
map_problem = Problem(environment=streets,
                      initial_state=initial_state,
                      goal_state=goal_state)

# search strategy
strategy = BreadthFirst()

# search algorithm (Tree Search / Graph Search)
search = TreeSearch(problem=map_problem, strategy=strategy)

# run algorithm
result, path = search.run()

# display the solutions
print(result)
print(path)