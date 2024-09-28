from collections import deque

# Goal state of the puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# Function to find the index of the empty tile (0)
def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Function to get all possible moves from a given state
def get_possible_moves(state):
    empty_tile_i, empty_tile_j = find_empty_tile(state)
    possible_states = []
    for move in moves:
        new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
            possible_states.append(new_state)
    return possible_states


# Function to check if a state is the goal state
def is_goal_state(state):
    return state == goal_state


# BFS to solve the puzzle
def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if is_goal_state(state):
            return path
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))

        for next_state in get_possible_moves(state):
            queue.append((next_state, path + [next_state]))

    return None


# Example initial state
initial_state = [[1, 2, 0],
                 [4, 5, 6],
                 [7, 3, 8]]

# Solve the puzzle
solution_path = bfs(initial_state)
if solution_path:
    print("Solution found!")
    for i, state in enumerate(solution_path):
        print(f"Step {i + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
