#!/usr/bin/python

import csv

# reads suduko file in CSV (comma seperated) format called sudoku1.csv to be placed in same directory
# usage: python suduko1.py


def main():   
   board = readFromFile()     
   
   run = 1
   while run == 1:
      run = algorithm(board)

   print "Suduko Solution ....."
   for row in board:
      print row
   	    
      
      
def algorithm(board):
   fullset = set(['1','2','3','4','5','6','7','8','9'])
   
   for r in range(9):
      for c in range(9):
       
	 if getNumber(r,c,board) != '':
	    continue  # skip
	    
	 # get row list 
         rowList = board[r]	 
      
         # get column list
	 columns = getColumns(board)
	 colList = columns[c]	 
	 
	 # get square list
	 squares = getSquares(board)
	 squareList = getSquare(r,c,squares)	  
	 
	 remainSet = fullset - set(rowList) - set(colList) - set(squareList)
	 if len(remainSet) == 1:
	    a = list(remainSet)
	    print "updating board with " + a[0] + " (" + str(r) + "," + str(c) + ")"
	    board = updateBoard(r,c,a[0],board)	    
	    return 1
   return 0
   	    

def updateBoard(r,c,x,board):
   board[r][c] = x
   return board

def getNumber(r,c,board):
   return board[r][c]
   
def getSquare(r,c,squares):   
   x = int(c/3) + (3 * int(r/3))   
   return squares[x]   


def getColumns(board):
   colBrd = []   
   for x in range(9):
      colBrd.append([])
      
   for i,row in enumerate(board):
      for a,x in enumerate(row):
         colBrd[a].append(x)
   return colBrd 
 

def getSquares(board):
   squares = []
   #0-2
   s = board[0][0:3] + board[1][0:3] + board[2][0:3]
   squares.append(s)
   s = board[0][3:6] + board[1][3:6] + board[2][3:6]
   squares.append(s)
   s = board[0][6:10] + board[1][6:10] + board[2][6:10]
   squares.append(s)
   #3-5
   s = board[3][0:3] + board[4][0:3] + board[5][0:3]
   squares.append(s)
   s = board[3][3:6] + board[4][3:6] + board[5][3:6]
   squares.append(s)
   s = board[3][6:10] + board[4][6:10] + board[5][6:10]
   squares.append(s)
   #6-8
   s = board[6][0:3] + board[7][0:3] + board[8][0:3]
   squares.append(s)
   s = board[6][3:6] + board[7][3:6] + board[8][3:6]
   squares.append(s)
   s = board[6][6:10] + board[7][6:10] + board[8][6:10]
   squares.append(s)   
   return squares
   
   

def readFromFile():
   board = []
   f = open('sudoku1.csv', 'rb') 
   Reader = csv.reader(f)
   for row in Reader:      
      board.append(row) 
   f.close() 
   return board        


if __name__ == '__main__':
    main()
