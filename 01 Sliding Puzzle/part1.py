# Aaliya Hussain
# 2nd Period
# 9/9/19

# import sys
# from collections import deque
# import time
#
# def print_puzzle(size, rep):
#     for x in range(size):
#         print(" ".join(rep[size*x:size*(x+1)]))
#
# def find_goal(board):
#     return "".join(sorted(board)[1:])+"."
#
# def coor_to_index(r, c, size):
#     if r == 0:
#         return int(c)
#     return int(c+size*r)
#
# def index_to_coor(i, size):
#     if i < size:
#         return 0, int(i)
#     return int(i/size), int(i%size)
#
# def swap(state, a, b):
#     sl = list(state)
#     sl[a], sl[b] = sl[b], sl[a]
#     return ''.join(sl)
#
# def get_children(state):
#     size = int(len(state)**.5)
#     r = index_to_coor(state.index("."), size)[0]
#     c = index_to_coor(state.index("."), size)[1]
#     cp = state.index(".")
#     ret = []
#     # Up
#     if r > 0:
#         np = coor_to_index(r-1, c, size)
#         ret.append(swap(state, np, cp))
#     # Down
#     if r < size-1:
#         np = coor_to_index(r+1, c, size)
#         ret.append(swap(state, np, cp))
#     # Left
#     if c > 0:
#         np = coor_to_index(r, c-1, size)
#         ret.append(swap(state, np, cp))
#     # Right
#     if c < size-1:
#         np = coor_to_index(r, c+1, size)
#         ret.append(swap(state, np, cp))
#     return ret
#
# def goal_test(board):
#     return board == find_goal(board)
#
# # Modeling
# # with open(sys.argv[1]) as f:
# #     i = 0
# #     for line in f:
# #         print("Line %s start state:" % i)
# #         print_puzzle(int(line[0]), line[2:])
# #         print()
# #         print("Line %s goal state:" % i)
# #         print_puzzle(int(line[0]), find_goal(line[2:]))
# #         print()
# #         print("Line %s children:" % i)
# #         for x in get_children(line[2:]):
# #             print_puzzle(int(line[0]), x)
# #             print()
# #         i += 1
#
# # BFS Searching
# # def bfs_games_from_goal(state):
# #     fringe = deque()
# #     visited = set()
# #     for c in get_children(state):
# #         fringe.append(c)
# #         visited.add(c)
# #     while len(fringe) != 0:
# #         v = fringe.popleft()
# #         if v != state:
# #             for c in get_children(v):
# #                 if c not in visited:
# #                     fringe.append(c)
# #                     visited.add(c)
# #     return len(visited)
# #
#
# def bfs_shortest_path(state):
#     fringe = deque()
#     visited = dict()
#     fringe.append((state, []))
#     visited[state] = tuple([])
#     while len(fringe) != 0:
#         v = fringe.popleft()
#         if v[0] == find_goal(state):
#             print_game(v)
#             return len(v[1])
#         for c in get_children(v[0]):
#             if c not in visited:
#                 t = v[1]+list([v[0]])
#                 fringe.append((c, t))
#                 visited[c] = tuple(t)
#     return None
#
# def print_game(v):
#     size = int(len(v[0])**.5)
#     for s in v[1]:
#         print_puzzle(size, s)
#         print()
#     print_puzzle(size, v[0])
# def bfs(state):
#     fringe = deque()
#     visited = set()
#     fringe.append((state, 0))
#     visited.add(state)
#     while len(fringe) != 0:
#         v = fringe.popleft()
#         if v[0] == find_goal(state):
#             return v[1]
#         else:
#             for c in get_children(v[0]):
#                 if c not in visited:
#                     fringe.append((c, v[1]+1))
#                     visited.add(c)
#     return None
#
# # def longest_8games():
# #     fringe = deque()
# #     visited = set()
# #     lens = dict()
# #     for c in get_children("12345678."):
# #         fringe.append((c, 1))
# #         visited.add(c)
# #         if 1 not in lens:
# #             lens[1] = tuple([c])
# #         else:
# #             t = list(lens[1])+list([c])
# #             lens[1] = tuple(t)
# #     while len(fringe) != 0:
# #         v = fringe.popleft()
# #         if v[0] != "12345678.":
# #             for c in get_children(v[0]):
# #                 if c not in visited:
# #                     fringe.append((c, v[1]+1))
# #                     visited.add(c)
# #                     if v[1]+1 not in lens:
# #                         lens[v[1]+1] = tuple([c])
# #                     else:
# #                         t = list(lens[v[1]+1]) + list([c])
# #                         lens[v[1]+1] = tuple(t)
# #     print(max(lens, key=int))
# #     return lens[max(lens, key=int)]
#
# #DFS
# def dfs1(state):
#     fringe = deque()
#     visited = set()
#     fringe.append((state, 0))
#     visited.add(state)
#     while len(fringe) != 0:
#         v = fringe.pop()
#         if v[0] == find_goal(state):
#             return v[1]
#         else:
#             for c in get_children(v[0]):
#                 if c not in visited:
#                     fringe.append((c, v[1] + 1))
#                     visited.add(c)
#     return None
#
# def dfs2(state):
#     fringe = deque()
#     visited = set()
#     fringe.append((state, 0))
#     while len(fringe) != 0:
#         v = fringe.pop()
#         if v[0] == find_goal(state):
#             return v[1]
#         if v[0] not in visited:
#             visited.add(v[0])
#             for c in get_children(v[0]):
#                 fringe.append((c, v[1] + 1))
#     return None
