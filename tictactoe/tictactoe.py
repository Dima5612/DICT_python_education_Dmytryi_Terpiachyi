theBoard = {'1,1': ' ', '1,2': ' ', '1,3': ' ',
            '2,1': ' ', '2,2': ' ', '2,3': ' ',
            '3,1': ' ', '3,2': ' ', '3,3': ' '}

def printBoard(board):
    print('------')
    print(board['1,1'] + '|' + board['1,2'] + '|' + board['1,3'])
    print('-+-+-')
    print(board['2,1'] + '|' + board['2,2'] + '|' + board['2,3'])
    print('-+-+-')
    print(board['3,1'] + '|' + board['3,2'] + '|' + board['3,3'])
    print('------')
