theBoard = {'1,1': ' ', '1,2': ' ', '1,3': ' ',
            '2,1': ' ', '2,2': ' ', '2,3': ' ',
            '3,1': ' ', '3,2': ' ', '3,3': ' '}
board_keys = []
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print('------')
    print(board['1,1'] + '|' + board['1,2'] + '|' + board['1,3'])
    print('-+-+-')
    print(board['2,1'] + '|' + board['2,2'] + '|' + board['2,3'])
    print('-+-+-')
    print(board['3,1'] + '|' + board['3,2'] + '|' + board['3,3'])
    print('------')
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("This cell is occupied! Choose another one!")
            continue
        if count >= 5:
            if theBoard['1,1'] == theBoard['1,2'] == theBoard['1,3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2,1'] == theBoard['2,2'] == theBoard['2,3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3,1'] == theBoard['3,2'] == theBoard['3,3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3,1'] == theBoard['2,1'] == theBoard['3,1'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3,2'] == theBoard['2,2'] == theBoard['1,2'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3,3'] == theBoard['2,3'] == theBoard['1,3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1,1'] == theBoard['2,2'] == theBoard['3,3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3,1'] == theBoard['2,2'] == theBoard['1,3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
        game()
if __name__ == "__main__":
    game()