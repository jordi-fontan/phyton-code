def displayState(val):
 k = val # K represents the number of sticks not 
 # printed
 while k > 0: # So long as some are not printed …
 if k >=6: # If there is a whole row, print it.
 print ("O O O O O O ", end="")
 k = k – 6 # Six fewer sticks are unprinted
 else:
 for j in range(0,k): # Print the remainder
 print ("O ", end="")
 k = 0 # None remain
 print ("")


def getMove ():
 n = int(input ("Your move: Take away how many? "))
 while n<=0 or n>3:
 print ("Sorry, you must take 1, 2, or 3 sticks.")
 n = int(input ("Your move: Take away how many? "))
 return n
 
 
def gameOver (state):
 if state == 0:
 return True
 return False


def getComputerMove (val):
 n = val % 4
 if n<=0:
 return 1
 else:
 return n

displayState(val) # Show the game board
userMove = getMove() # Ask user for their move
val = val – userMove # Make the move
print ("You took ", userMove, " sticks leaving ", val)
if gameOver(val):
 print("You win!")
else:
 move = makeComputerMove (val) # Calculate the 
 # computerꞌs move
 print ("Computer took ", move, " sticks leaving ", val)
 if gameOver(val):
 print("Computer wins!")
 
