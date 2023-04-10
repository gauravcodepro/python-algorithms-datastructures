#https://leetcode.com/problems/word-search/
#Word Search
#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
#or vertically neighboring. The same letter cell may not be used more than once.
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#Output: true
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#Output: true
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#Output: false

list(map(lambda n: set([(j,i.__contains__(j)) for i in n for j in list(word)]),board))
[{('A', False),
  ('A', True),
  ('B', False),
  ('B', True),
  ('C', False),
  ('C', True),
  ('D', False),
  ('E', False),
  ('E', True)},
 {('A', False),
  ('B', False),
  ('C', False),
  ('C', True),
  ('D', False),
  ('E', False)},
 {('A', False),
  ('A', True),
  ('B', False),
  ('C', False),
  ('D', False),
  ('D', True),
  ('E', False),
  ('E', True)}]