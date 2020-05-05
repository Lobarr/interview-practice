from abc import ABC, abstractmethod
from random import randint
from typing import Tuple

class InvalidCoordinate(Exception):
  pass

class TiedGame(Exception):
  pass

class DoublePlay(Exception):
  pass

class Board(ABC):
  COORDINATE_PLACEHOLDER = '*'

  def __init__(self, rowSize: int, colSize: int):
    self.board = [[Board.COORDINATE_PLACEHOLDER] * colSize for _ in range(rowSize)]
    self.rowSize = rowSize
    self.colSize = colSize

  def getColSize(self) -> int:
    return self.colSize

  def getRowSize(self) -> int:
    return self.rowSize

  def validateCoordinate(self, x: int, y: int) -> bool:
    if (
      0 <= x < self.rowSize
      and 0 <= y < self.colSize
    ):
      return True
    return False

  def setCoordinate(self, x: int, y: int, value: str) -> bool:
    if not self.validateCoordinate(x, y):
      return False

    if self.board[x][y] != Board.COORDINATE_PLACEHOLDER:
      raise DoublePlay('Provided coordinate is already occupied')

    self.board[x][y] = value

    return True

  def getCoordinate(self, x: int, y: int) -> str:
    if not self.validateCoordinate(x,y):
      raise Exception('Coordinates provided are out of bounds')

    return self.board[x][y]

  def isFull(self) -> bool:
    for row in self.board:
      if len(list(filter(lambda x: x == Board.COORDINATE_PLACEHOLDER, row))) > 0:
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
      if len(list(filter(lambda x: x == player, row))) == self.rowSize:
        return True
    return False

  def checkVertical(self, player: str) -> bool:
    curColIndex = self.colSize - 1
    while curColIndex >= 0:
      matchCount = 0 # holds count for number of matching coordinates 

      for row in self.board:
        if row[curColIndex] == player:
          matchCount += 1
      
      if matchCount == self.colSize:
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

    if matchCount == self.rowSize:
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

    if matchCount == self.rowSize:
      return True

    return False

  def checkWin(self, player: str) -> bool:
    if (
      self.checkHorizontal(player) 
      or self.checkVertical(player) 
      or self.checkDecreasingDiagonal(player) 
      or self.checkIncreasingDiagonal(player)
    ):
      return True

    if self.isFull():
      raise TiedGame('Game is a tie')
    
    return False

  def printBoard(self):
    for index, row in enumerate(self.board):
      print(' | '.join(row))
      if index < len(self.board) - 1:
        print('_' * 9)
    print()


class TicTacToe:
  def __init__(self):
    self.curPlayer = 'X' if randint(0, 10) <= 5 else 'O'
    self.board = TicTacToeBoard()

  def togglePlayerTurn(self):
    self.curPlayer = 'X' if self.curPlayer == 'O' else 'O'

  def printHeader(self):
    print('--- TIC TAC TOE --- \n \n')

  def printPlayerTurn(self, player: str):
    print(f'Current Player - {self.curPlayer}')

  def printSeperatorSpaces(self):
    for _ in range(3):
      print()

  def getPlayerInput(self) -> Tuple[int, int]:
    while True:
      try:
        print('Enter board coordinate...')
        x = int(input(f'x [0 - {self.board.getRowSize() - 1}]: '))
        y = int(input(f'y [0 - {self.board.getColSize() - 1}]: '))

        if not self.board.validateCoordinate(x, y):
          raise InvalidCoordinate('Enter valid coordinates')

        return (x,y)
      except ValueError:
        print('Invalid input was provided')
        # self.printSeperatorSpaces()
        continue
      except InvalidCoordinate as err:
        print(str(err))
        # self.printSeperatorSpaces()
        continue
      else:
        break
      finally: 
        self.printSeperatorSpaces()

  def play(self):
    self.printHeader()
    while True:
      try:
        self.board.printBoard()
        self.printPlayerTurn(self.curPlayer)

        x, y = self.getPlayerInput()

        if not self.board.setCoordinate(x, y, self.curPlayer):
          continue

        if self.board.checkWin(self.curPlayer):
          self.board.printBoard()
          print(f'Game winner is Player {self.curPlayer}!')
          break

        self.togglePlayerTurn()
        
      except TiedGame:
        self.board.printBoard()
        print('Game is a tie!')
        break

      except DoublePlay as err:
        print(str(err))
        print()
        continue
    

if __name__ == '__main__':
  ticTacToe = TicTacToe()
  ticTacToe.play()
