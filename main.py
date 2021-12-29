the_board = {
  7: " ", 8: " ", 9: " ",
  4: " ", 5: " ", 6: " ",
  1: " ", 2: " ", 3: " "
}
board_keys = []
for key in the_board:
  board_keys.append(key)#appends keys from the_board dictionary into board_keys list

'''The Function will print the board everytime we call this function using the the_board dictionary as a parameter'''
def print_board(board):
  print(board[7]+ "|" + board[8] + "|"+ board[9])
  print("-+-+-")
  print(board[4]+ "|" + board[5] + "|"+ board[6])
  print("-+-+-")
  print(board[1]+ "|" + board[2] + "|"+ board[3])

#Now we write the main function which will give the game functionality
def game():
  turn = 'X'
  count = 0

  for i in range(10):
    print()
    print_board(the_board)
    print("It is your turn: "+ turn)
    print("Where would you like to go?")
    move = int(input())
    #use number pad for moves
    if the_board[move] == " ":
      the_board[move] = turn
      count +=1
    else:
      print("The spot is already taken.\nPlease move somewhere else")
      continue
  #We will check if player has won after 5 moves because that is the min number of moves for a player to win
    if count >= 5:
      if the_board[7] == the_board[8] == the_board[9] != ' ': #Over the Top
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
      elif the_board[4] == the_board[5] == the_board[6] != ' ': #Over the Middle
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
      elif the_board[1] == the_board[2] == the_board[3] != ' ': #Over the Bottom
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
      elif the_board[1] == the_board[4] == the_board[7]!= ' ': #Left Column
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
      elif the_board[2] == the_board[5] == the_board[8] != ' ':#Middle Column
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
      elif the_board[3] == the_board[6] == the_board[9] != ' ': #Right Column
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
      elif the_board[7] == the_board[5] == the_board[3] != ' ':#top left to bottom right
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
      elif the_board[9] == the_board[5] == the_board[1] != ' ':#Top right to bottom left
        print_board(the_board)
        print("\nGame over.\n")
        print("*** "+ turn + " won.***")
        break
    #if no one wins, this will run to say it is a tie
    if count==9:
      print("Game over.")
      print("It's a tie!")
    #This if statement will alternated moves between "X" and "O"
    if turn == "X":
      turn = 'O'
    else:
      turn = "X"
  
  restart = input("Do you want to play again(y/n)")
  if restart == "y" or restart == 'Y':
    for key in the_board:
      the_board[key] = " "
    game()

#When running source file as main program name is assigned as such
if __name__ == "__main__":
  game()

