#https://leetcode.com/problems/word-search/
#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
#horizontally or vertically neighboring. The same letter cell may not be used more than once.
Concept check the word in each 2D matrix and if the word is coming from the
each different matrix then yes and if not then false. 
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
[(i,'True',j) if i in j and board.count(j)==1 else 'False' for i in set(list(word)) for j in board]