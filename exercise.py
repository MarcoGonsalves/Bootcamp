# =========================
# Overview
# =========================

####################################################################################
# ========================
# Part 1: Vector and Complex Numbers
# ========================

# In this exercise you will use what you have learned to implement a Vector
# class and a complex number class.

# ========================
# The Vector class
# ========================

# Write definitions for a class called Vector.
# Your definition should include a constructor,  __str__, values for the x and y
# coordinates, and methods for addition and subtraction of vectors, scalar multiplication,
# length, and comparison.

class Vector(object): #Create vector(x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): #Produce a readable output from arithmetic methods
        return f"Vector ({self.x}, {self.y})"

    def __add__(self, addVec): #Addition of two vectors method
        return Vector(self.x + addVec.x, self.y + addVec.y)

    def __sub__(self, subVec): #Subtraction of two vectors method
        return Vector(self.x - subVec.x, self.y - subVec.y)

    def __mul__(self, multVec): #Multipliction of two vectors method
        return Vector(self.x * multVec.x, self.y * multVec.y)

    def length(self): #Length calculation method
        return (self.x**2 + self.y**2)**.5

    def compare(self, compVec): #Comparing the vectors values
        if self.x == compVec.x and self.y == compVec.y:
            return "Vectors are equal"
        else:
            return "Vectors are not equal"

#Code testing
v1 = Vector(3, 4)
v2 = Vector(3, 4)
v3 = Vector(-4, -3)

print (v1 + v2)
print (v1 - v2)
print (v1 * v2)
print(v1.length())
print(v1.compare(v2))
print(v1.compare(v3))


    #pass

# =========================
# The derived Complex class
# =========================

# Write definitions for a class called MyComplex that is derived from your
# Vector class.  Your definition should include methods for multiplying two
# complex numbers and computing the complex conjugate as well as an updated
# definition of __str__.
import cmath
class MyComplex(Vector):

    def __rmul__(self, multVec): #Multiply by complex numbers
        return self.__mul__(multVec)

    def conj(self):
        return (self.x.conjugate(), self.y.conjugate())
    pass

#Code test
vj1 = MyComplex(2, 3j)
print(vj1.conj())



####################################################################################
# ========================
# Part 2: Tic-tac-toe
# ========================

# In this task you will be writing a simple game of tic-tac-toe.
# You should expect to find this exercise more challenging than Part 1.
# Please write docstrings for each class and method.
# As you walk through each element, think about how the game's objects are organized.
# Does it seem like the most efficient way to do things to you?
# A common criticism of object-oriented programming is that it can lead to
# excessive abstractions and overcomplication.

# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:

'''while True: 
    class Piece(object): 
        board.drawBoard()
'''
        

# =======================
# The X and O classes
# =======================

# Write definitions of X and O piece classes.
# Your definitions should include:

''' class X(Piece): #Player X fills the board with an X, a new baord is drawn and the games tries to end
        turnX = int(input("\nPlayer X:\nChoose location (0 - 8): "))
        board.play(turnX, "X")
        board.drawBoard()
        board.endGame()

    class O(Piece): #Player O fills the board with an O, a new baord is drawn and the games tries to end
        turnO = int(input("\nPlayer O:\nChoose location (0 - 8): "))
        board.play(turnO, "O")
        board.endGame()
'''

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:

class TicTacToeBoard(object): #Defining board        
    def __init__ (self):
        self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    
    def drawBoard(self): #Draw the board, formating and key for players
        print(f"\n{self.board[0]} | {self.board[1]} | {self.board[2]} INDEX: 0 | 1 | 2 ") 
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}        3 | 4 | 5 ")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}        6 | 7 | 8")

    def play(self, index, player): #Players turn updating board
        if self.board[index] == "-":
            self.board[index] = player

    def winner(self, player): #Check to see if there are three of the same in a row/column/diagonal
        if self.board[0] == player and self.board[1] == player and self.board[2] == player:
            return True
        if self.board[3] == player and self.board[4] == player and self.board[5] == player:
            return True
        if self.board[6] == player and self.board[7] == player and self.board[8] == player:
            return True
        if self.board[0] == player and self.board[3] == player and self.board[6] == player:
            return True
        if self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        if self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        if self.board[0] == player and self.board[4] == player and self.board[8] == player:
            return True
        if self.board[2] == player and self.board[4] == player and self.board[6] == player:
            return True
        return False

    def tie(self): #If the whole board is not '-' that means the board is full and nobody has won
        turns = 0
        for spot in self.board:
            if spot != '-':
                turns += 1
        if turns == 9:
            return True
        else:
            return False

    def endGame(self): #Try to end the game, fails if winner is False
        if board.winner("O"):
            print("\nPlayer O wins")
            return board.newGame()
            
        if board.winner("X"):
            print("\nPlayer X wins")
            return board.newGame()

    def newGame(self): #Refresh the board
        self.board = []
        self.board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

board = TicTacToeBoard()

while True: 
    class Piece(object): #Draw initial new board
        board.drawBoard()

    class X(Piece): #Player X fills the board with an X, a new baord is drawn and the games tries to end
        turnX = int(input("\nPlayer X:\nChoose location (0 - 8): "))
        board.play(turnX, "X")
        board.drawBoard()
        board.endGame()

    class O(Piece): #Player O fills the board with an O, a new baord is drawn and the games tries to end
        turnO = int(input("\nPlayer O:\nChoose location (0 - 8): "))
        board.play(turnO, "O")
        board.endGame()

###### Hi, I tried to use different methods where I could think of new ways to implement the game
###### but obviously once I had seen the way you did it I couldn't get it out my head.
