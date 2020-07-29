# Get the value infinity
import math

# Used to get the Manhattan distance between 2 points on the grid
def manhattan_distance(a, b):
    x_diff = abs(b[0] - a[0])
    y_diff = abs(b[1] - a[1])
    distance = x_diff + y_diff
    return distance

# Used to initialize the values for functions f(x) and g(x)
def init_cost(size, grid):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            grid[(i, j)] = float("inf")

# Used to find the next point with the lowest cost from a set of candidates
def find_lowest_cost(open_set, grid):
    temp = tuple()
    temp = open_set[0]
    for i in open_set:
        if grid[i] < grid[temp]: 
            temp = i
    return temp

# Used to determine the neighbors of a particular point
def find_neighbors(loc, size):
    temp_list = list()
    #left neighbor
    if((loc[0] - 1) >= 1):
        temp_list.append((loc[0] - 1, loc[1]))
    #right neighbor
    if((loc[0] + 1) <= size):
        temp_list.append((loc[0] + 1, loc[1]))
    #top neighbor
    if((loc[1] + 1) <= size):
        temp_list.append((loc[0], loc[1] + 1))
    #bottom neighbor
    if((loc[1] - 1) >= 1):
        temp_list.append((loc[0], loc[1] - 1))
    return temp_list

# Heuristic used is 2 times the Manhattan distance, which is the minimum cost required
def heuristic_estimate(start, end):
    return(2 * manhattan_distance(start, end))

# Used to put a least cost path from start to goal in a list
def draw_path(parents, child):
    path = [child]
    while child in parents:
        child = parents[child]
        path.insert(0, child)
    return path

# Main function
def path_find(n, start_loc, goal_loc, values):
    # initialize variables
    visited = list()
    unvisited = list()
    neighbors = list()
    least_cost_path = dict()
    g_scores = dict()
    temp_g_score = int
    f_scores = dict()
    current = tuple()

    # add start location to open set
    unvisited.append(start_loc)

    init_cost(n, g_scores)
    init_cost(n, f_scores)
    
    g_scores[start_loc] = 0
    f_scores[start_loc] = heuristic_estimate(start_loc, goal_loc)

    # A* search algorithm
    while not len(unvisited) == 0:
        current = find_lowest_cost(unvisited, f_scores)
        if current == goal_loc:
            least_cost_path = draw_path(least_cost_path, current)
            unvisited = []
            continue
        unvisited.remove(current)
        visited.append(current)
        neighbors = find_neighbors(current, n)
        for i in neighbors:
            if(i in visited):
                continue
            if (i not in unvisited):
                unvisited.append(i)
            temp_g_score = g_scores[current] + values[(i)[0] - 1][(i)[1] - 1] + 1
            if(temp_g_score >= g_scores[i]):
                continue
            least_cost_path[i] = current
            g_scores[i] = temp_g_score
            f_scores[i] = g_scores[i] + heuristic_estimate(i, goal_loc)
    return least_cost_path

# default test values

n = 5
start_loc = (1, 1)
goal_loc = (5, 4)
values = [[4,3,3,4,2],[2,4,4,2,2],[3,4,5,3,2],[2,3,4,5,2],[4,3,3,2,4]]

# test case where start = goal

"""
n = 5
start_loc = (1, 1)
goal_loc = (1, 1)
values = [[4,3,3,4,2],[2,4,4,2,2],[3,4,5,3,2],[2,3,4,5,2],[4,3,3,2,4]]
"""

# test case for an intuitive least cost path

"""
n = 5
start_loc = (1, 1)
goal_loc = (1, 5)
values = [[1,1,1,50,1],[50,50,1,50,1],[1,1,1,50,1],[1,50,50,50,1],[1,1,1,1,1]]
"""

# test case for grid bigger than 5x5

"""
n = 7
start_loc = (1, 1)
goal_loc = (7, 1)
values = [[1,1,1,1,1,1,1],[100,100,100,100,100,100,1],[1,1,1,1,1,1,1],[1,100,100,100,100,100,100],[1,1,1,1,1,1,1],[100,100,100,100,100,100,1],[1,1,1,1,1,1,1]]
"""

least_cost_path = path_find(n, start_loc, goal_loc, values)
print(least_cost_path)
