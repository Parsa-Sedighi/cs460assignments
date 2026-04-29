"""
Traversal Suite

Instructions:
- Implement all required functions in this file.
- Do not change any function names or parameters.
- Do not use external graph libraries.
- Do not write your own input() code.
- Do not rely on print() for correctness.
- Your functions must return values exactly as specified.

You may add helper functions if needed.
"""
from collections import deque

class TreeNode:
    """
    Basic binary tree node for the symmetric tree problem.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_islands_dfs(grid):
    """
    Problem 1A: Number of Islands using DFS

    Parameters:
        grid: List[List[str]]
            A 2D grid containing '1' for land and '0' for water.

    Returns:
        int
            The number of islands in the grid.

    Notes:
    - Adjacent land is connected horizontally or vertically only.
    - You must solve this version using DFS.
    - Be careful with edge cases such as:
        * empty grid
        * grid with no land
        * grid with all land
        * single row or single column
    """
    # TODO: Write your solution here.
    #Check if the grid is empty
    if grid == False:
        return 0
    # Number of islands (groups of connected 1's)
    islands = 0
    # Number of rows and columns
    rows, columns = len(grid), len(grid[0])
  

    def DFS (row, column):
        
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] == '0':
            return 
        grid[row][column] = '0'

        DFS(row + 1, column)
        DFS(row - 1, column)
        DFS(row, column + 1)
        DFS(row, column - 1)
    
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == '1':
                islands +=1
                DFS(row, column)
    return islands
    


#print("num_islands_dfs received:", grid)
#return 0


def num_islands_bfs(grid):
    """
    Problem 1B: Number of Islands using BFS

    Parameters:
        grid: List[List[str]]
            A 2D grid containing '1' for land and '0' for water.

    Returns:
        int
            The number of islands in the grid.

    Notes:
    - Adjacent land is connected horizontally or vertically only.
    - You must solve this version using BFS.
    """
    # TODO: Write your solution here.
    #Check if the grid is empty
    if not grid or not grid[0]: 
        return 0
    # Number of islands (groups of connected 1's)
    islands = 0
    # Number of rows and columns
    rows, columns = len(grid), len(grid[0])
    # The visited placeholder
    visited = set()

    for row in range(rows):
        for column in range(columns):
            # If at row x column, the value 1 island is found, and it is not in visited, increase islands by 1
            if grid[row][column] == '1' and (row,column) not in visited:
                islands+= 1
                queue = deque([(row,column)])
                visited.add((row,column))
                while queue:
                    # Assign the first item in queue to row and column
                    curr_row, curr_column = queue.popleft()
                    # Now, check for the 4 neighbors of down, up, right and left
                    for d_row, d_column in [(1,0), (-1,0), (0, 1), (0, -1)]:
                        n_row, n_column = curr_row + d_row, curr_column + d_column
                        # Check for boundaries, that grid at n_row and n_column is 1, and that it has not been visited.
                        if( 0 <= n_row < rows and 0 <= n_column < columns and grid[n_row][n_column] == '1' and (n_row, n_column) not in visited):
                            # If it has not already been visited, add that to the queue
                            queue.append((n_row, n_column))
                            # Add it to the visted
                            visited.add((n_row, n_column))
    print("num_islands_bfs received:", grid)
    # Return isolated neighboring group of 1's
    return islands

    #print("num_islands_bfs received:", grid)
    #return 0


def is_symmetric(root):
    """
    Problem 2: Symmetric Tree

    Parameters:
        root: TreeNode
            The root of a binary tree.

    Returns:
        bool
            True if the tree is symmetric, False otherwise.

    Notes:
    - A tree is symmetric if the left subtree is a mirror reflection
      of the right subtree.
    - Handle edge cases such as:
        * empty tree
        * single-node tree
        * missing children
    """
    # TODO: Write your solution here.
    if not root:
        return True

    def dfs(l_tree, r_tree):
        # If left and right subtree are non existent, then the tree is symmetric
        if( not l_tree and not r_tree):
            return True
        # If only one of the subrees is non existent, then the tree is no longer symmetric
        if(not l_tree or not r_tree):
            return False
        # If the left subtree value is not equal to right subtree value, then it is not symmetric
        if(l_tree.val != r_tree.val):
            return False
        # Compare left tree's left with right tree's right
        return  dfs(l_tree.left, r_tree.right) and dfs(l_tree.right, r_tree.left)
    
    return dfs(root.left, root.right)


    
    #print("is_symmetric received root with value:",
    #      root.val if root is not None else None)
    #return False


def can_finish_dfs(num_courses, prerequisites):
    """
    Problem 3A: Course Schedule using DFS Cycle Detection

    Parameters:
        num_courses: int
            Number of courses labeled from 0 to num_courses - 1

        prerequisites: List[List[int]]
            Each pair [a, b] means course b must be taken before course a.

    Returns:
        bool
            True if all courses can be finished, False otherwise.

    Notes:
    - You must solve this version using DFS.
    - This is a cycle-detection problem on a directed graph.
    - If a cycle exists, return False.
    - Otherwise, return True.
    """
    # TODO: Write your solution here.
    adj_list = [[] for _ in range(num_courses)]
    # the first dimension being the class, the second dimesnion being the pre-requisite
    for course, pre in prerequisites:
        adj_list[pre].append(course)
    # Create a list of status for each course. 0 as unvisited, 1 as currently being visited, 2 as visited
    state = [0] * num_courses
    def has_cycle(node):
        # If the node/class is being visited, return true
        if state[node] == 1:
            return True
        # If the node/class has already been visited, return false
        if state[node] == 2:
            return False
        # Mark the current node/class as being visited
        state[node] = 1 
        # For each neighboor in the adjancency list, if it has a cycle, if the neighbor has a cycle, return true
        for neighbor in adj_list[node]:
            if has_cycle(neighbor):
                return True
        # otherwise, mark it as visited and return false
        state[node] = 2
        return False
    # For each course that has not been visited, do the following...
    for i in range(num_courses):
        if state[i] == 0:
            # If a cycle is detected, return dalse since not all courses can be finished
            if has_cycle(i):
                return False
    # Return true if no cycle has been detected.
      
    return True
    print("can_finish_dfs received:", num_courses, prerequisites)
    return False


def course_order_bfs(num_courses, prerequisites):
    """
    Problem 3B: Course Schedule using BFS Topological Sort

    Parameters:
        num_courses: int
            Number of courses labeled from 0 to num_courses - 1

        prerequisites: List[List[int]]
            Each pair [a, b] means course b must be taken before course a.

    Returns:
        List[int]
            A valid order in which the courses can be taken.
            If no valid ordering exists, return an empty list.

    Notes:
    - You must solve this version using BFS.
    - This version should use indegree and queue-based topological sort.
    - If multiple valid answers exist, any valid order is acceptable.
    """
    # TODO: Write your solution here.
    # An adjacency list for the courses and their dependents
    adj_list = [[] for _ in range(num_courses)]
    # in degree list to track number of requiremnets for courses
    in_degree = [0] * num_courses

    for course, pre in prerequisites:
        # Assign all courses that depend on the prerequisite
        adj_list[pre].append(course)
        # increment the indegree since the course has a requirement
        in_degree[course] += 1
    # Initialize a queue for courses with no in_degrees/prerequisites
    queue = deque()
    for i in range(num_courses):
        if(in_degree[i] == 0):
            queue.append(i)
    # Create the set to order the courses
    order = []
    
    while queue:
        # Assign the no prerequisite course in the queue
        current = queue.popleft()
        order.append(current)
        # For each course that the current course is a prerequisite to
        for neighbor in adj_list[current]:
            # Subtract the indegree since the prerequisite has now been met
            in_degree[neighbor] -= 1
            # If now the neighbor has no outsanding prerequisites
            if in_degree[neighbor] == 0:
                # Add that to the queue as the new no prerequiste course
                queue.append(neighbor)
    # If the number of courses ordered in the set are equal to all courses...
    if len(order) == num_courses:
        # Then there is no cycle and an order is returned
        return order
    # Otherwise, there is a cycle and cannot be ordered is such way that classes can be finished.
    return []

    print("course_order_bfs received:", num_courses, prerequisites)
    return []


def solve_n_queens(n):
    """
    Problem 4: N-Queens

    Parameters:
        n: int
            Size of the chessboard (n x n)

    Returns:
        List[List[str]]
            A list of all valid board configurations.
            Each board is represented as a list of strings.

    Example board format for n = 4:
        [
            ".Q..",
            "...Q",
            "Q...",
            "..Q."
        ]

    Notes:
    - You must use backtracking.
    - No two queens may share the same row, column, or diagonal.
    - Edge cases include:
        * n = 1
        * n = 2
        * n = 3
    """
    # TODO: Write your solution here.
    column = set()
    # Diagnoal from bottom left, to top right
    posDiag = set() # (r + c)
    # Diagonal from top left, to bottom right
    negDiag = set() # (r - c)
    # Resulting 
    res = []
    # Make a board of n places where the queen can be placed
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in column or (row + c) in posDiag or (row - c) in negDiag:
                continue

            # Update sets and board
            column.add(c)
            posDiag.add(row + c)
            negDiag.add(row - c)
            board[row][c] = "Q"

            # Move to next row
            backtrack(row + 1)

            # Undo (Backtrack)
            column.remove(c)
            posDiag.remove(row + c)
            negDiag.remove(row - c)
            board[row][c] = "."

    backtrack(0)
    return res

    print("solve_n_queens received:", n)
    return []


def graph_coloring(graph, m):
    """
    Problem 5: M-Coloring / Graph Coloring

    Parameters:
        graph: dict[int, list[int]]
            Graph given as an adjacency list.
            Example:
                {
                    0: [1, 2],
                    1: [0, 2],
                    2: [0, 1]
                }

        m: int
            Maximum number of colors allowed

    Returns:
        bool
            True if the graph can be colored using at most m colors
            such that no adjacent vertices share the same color,
            otherwise False.

    Notes:
    - You must solve this using backtracking.
    - Assume the graph is undirected.
    - Edge cases include:
        * empty graph
        * disconnected graph
        * m = 1
    """
    # TODO: Write your solution here.
    #If the graph is empty, we must return True
    if not graph:
        return True
    # Create a color map and initialize all of them to color 0 = not colored
    colors = {node: 0 for node in graph}
    nodes = list(graph.keys())
    # Number of nodes
    nodes_count = len(nodes)
    # A backtrack helper function to
    def backtrack(index):
        if index == nodes_count:
            return True
        current_node = nodes[index]

        # For every color from 1 to m
        for color_choice in range(1, m+1):
            if is_safe(current_node, color_choice):
                #Assign the color
                colors[current_node] = color_choice

                if backtrack(index+1):
                    return True
                colors[current_node] = 0
        return False
    def is_safe(node, color_to_try):
        for neighbor in graph[node]:
            if colors.get(neighbor, 0) == color_to_try:
                return False
        return True
    
    return backtrack(0)



    print("graph_coloring received:", graph, m)
    return False


def main():
    """
    Local demo only.
    Your instructor's grading script will test your functions directly.
    """

    print("===== CS460 Traversal Suite Demo =====\n")

    # -----------------------------------
    # Problem 1: Number of Islands
    # -----------------------------------
    grid = [
        ['1', '1', '0'],
        ['0', '1', '0'],
        ['1', '0', '1']
    ]

    print("Testing Number of Islands")
    print("DFS result:", num_islands_dfs([row[:] for row in grid]))
    print("BFS result:", num_islands_bfs([row[:] for row in grid]))
    print()

    # -----------------------------------
    # Problem 2: Symmetric Tree
    # -----------------------------------
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    print("Testing Symmetric Tree")
    print("Symmetric result:", is_symmetric(root))
    print()

    # -----------------------------------
    # Problem 3: Course Schedule
    # -----------------------------------
    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print("Testing Course Schedule")
    print("Can finish (DFS cycle detection):",
          can_finish_dfs(num_courses, prerequisites))
    print("Course order (BFS topological sort):",
          course_order_bfs(num_courses, prerequisites))
    print()

    # -----------------------------------
    # Problem 4: N-Queens
    # -----------------------------------
    n = 4
    solutions = solve_n_queens(n) 
    print("Testing N-Queens")
    print("Solutions returned:", solutions)
    print()

    # -----------------------------------
    # Problem 5: Graph Coloring
    # -----------------------------------
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    m = 3

    print("Testing Graph Coloring")
    print("Coloring possible:", graph_coloring(graph, m))
    print()


if __name__ == "__main__":
    main()