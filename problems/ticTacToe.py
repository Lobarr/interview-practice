from random import randint
from abc import ABC, abstractmethod

class Board(ABC):
  def __init__(self, rowSize: int, colSize: int):
    self.board = [[''] * colSize for _ in range(rowSize)]
    self.rowSize = rowSize
    self.colSize = colSize

  def validateCoordinate(self, x: int, y: int) -> bool:
    if (
      0 <= x < self.rowSize
      and 0 <= y < self.colSize
    ):
      return True
    return False

  def setCoordinate(self, x: int, y: int, value: str) -> bool:
    if not self.validateCoordinate(x, y) or self.board[x][y] != '':
      return False

    self.board[x][y] = value

    return True

  def getCoordinate(self, x: int, y: int) -> str:
    if not self.validateCoordinate(x,y):
      raise Exception('Coordinates provided are out of bounds')

    return self.board[x][y]

  def isFull(self) -> bool:
    for row in self.board:
      if len(list(filter(lambda x: x == '', row))) > 0:
        return False

    return True

  @abstractmethod
  def checkWin(self, player: str) -> bool:
    """
    raise error when there is a tie
    """
    raise Exception('not implemented')

  @abstractmethod
  def printBoard(self):
    raise Exception('not implemented')


class TicTacToeBoard(Board):
  def __init__(self, rowSize=3, colSize=3):
    super().__init__(rowSize, colSize)

  def checkHorizontal(self, player: str) -> bool:
    for row in self.board:
      if len(list(filter(lambda x: x == player, row))) == 3:
        return True
    return False

  def checkVertical(self, player: str) -> bool:
    curColIndex = self.colSize - 1
    while curColIndex >= 0:
      matchCount = 0 # holds count for number of matching coordinates 

      for row in self.board:
        if row[curColIndex] == player:
          matchCount += 1
      
      if matchCount == 3:
        return True

      curColIndex -= 1
    
    return False

  def checkDecreasingDiagonal(self, player: str) -> bool:
    colIndex = 0
    rowIndex = 0
    matchCount = 0

    while colIndex < self.colSize and rowIndex < self.rowSize:

      if self.getCoordinate(rowIndex, colIndex) == player:
        matchCount += 1

      colIndex += 1
      rowIndex += 1

    if matchCount == 3:
      return True
    
    return False

  def checkIncreasingDiagonal(self, player: str) -> bool:
    colIndex = 0
    rowIndex = self.rowSize - 1
    matchCount = 0

    while rowIndex >= 0 and colIndex < self.colSize:
      if self.getCoordinate(rowIndex, colIndex) == player:
        matchCount += 1

      colIndex += 1
      rowIndex -= 1

    if matchCount == 3:
      return True

    return False

  def checkWin(self, player: str) -> bool:
    if (
      self.checkHorizontal() 
      or self.checkVertical() 
      or self.checkDecreasingDiagonal() 
      or self.checkIncreasingDiagonal()
    ):
      return True

    if self.isFull():
      raise Exception('Game is a tie')
    
    return False

  def printBoard(self):
    for index, row in enumerate(self.board):
      print(' | '.join(row))
      if index < len(self.board):
        print('_' * 9)



"""
- should run execution loop
- should track player turn
- 
"""
class TicTacToe:
  def __init__(self):
    self.curPlayer = 'X' if randint(0, 1) == 0 else 'O'
    self.board = TicTacToeBoard()

  def togglePlayer(self):
    self.curPlayer = 'X' if self.curPlayer == 'O' else 'O'

  def play(self):
    """
    get user input

    """
    try:
      #TODO: write execution loop
      pass
    except Exception as error:
      #TODO: handle error
      pass


if __name__ == '__main__':
  ticTacToe = TicTacToe()
  # ticTacToe.play()
