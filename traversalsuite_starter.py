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
    print("num_islands_dfs received:", grid)
    return 0


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
    print("num_islands_bfs received:", grid)
    return 0


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
    print("is_symmetric received root with value:",
          root.val if root is not None else None)
    return False


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