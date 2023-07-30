class tictacboard:
  def __init__(self,n):
    self.n = n
    self.board = [['_']*n  for i in range(n)]

  def printboard(self):
    for l2 in self.board:
      for x in l2 : print(x, end='    ')
      print('\n') 

class OccupiedLocationError(Exception):
    pass
class InvalidBoard(Exception):
    pass


class match(tictacboard):
  def __init__(self,size):
    self.lastplayer = None
    self.player1 = None
    self.player2 = None
    super().__init__(size)
    
  def start(self):
    self.printboard()
    print('''Player 1 \nChoose a value X or O. Don't enter any other value.''')
    self.player1 = self.lastplayer = input().upper()
    self.player2 = 'O' if self.player1 not in ('O','0') else 'X'
    print('Choose a location i,j to put in board where 1 <=i,j<= 3')
    lis = list( map(int, input().strip().split() ) )
    if len(lis) == 1: 
      a=lis[0]//10
      b=lis[0]%10
    else:
      a,b = lis

    self.board[a-1][b-1] = self.lastplayer
    

  def play(self):
    self.printboard()
    currentplayer = self.player2 if self.lastplayer == self.player1 else self.player1
    print('PLAYER 2 CHANCE.' if self.lastplayer == self.player1 else 'PLAYER 1 CHANCE.')
    print('Currentplayer:', currentplayer,)
    print('Choose a location i,j to put in board')
    lis = list( map(int, input().strip().split() ) )
    if len(lis) == 1: 
      a=lis[0]//10
      b=lis[0]%10
    else:
      a,b = lis
      
    try:
      if self.board[a-1][b-1] != '_': 
        raise OccupiedLocationError("***Already Occupied,Enter Unoccupied location.")
      self.board[a-1][b-1] = currentplayer
    except Exception as e:
      print('\n', e, '\nTry again')
      self.play()
    
    self.lastplayer = currentplayer
    

  def check_if_won(self):
    l= self.board
    
    for x in self.board:   # Checking Horizontally
      if len(set(x)) ==1 and '_' not in set(x):
        Player = 'Player 1' if self.player1 ==x[0] else 'Player 2'
        print(f'\n{Player} ({x[0]}) WON')
        return True
        
    for i in range(len(l)):    # Checking Vertically
      s2 = {l[j][i] for j in range(len(l)) } 
      if len(s2) == 1 and '_' not in s2:
        Player = 'Player 1' if self.player1 ==l[0][i] else 'Player 2'
        print(f'\n{Player} ({l[0][i]}) WON')
        return True
        
    s3 = { l[i][i] for i in range(len(l)) }  # Checking Diagonal L to R
    if len(s3) ==1 and '_' not in s3:
      Player = 'Player 1' if self.player1 ==l[0][0] else 'Player 2'
      print(f'\n{Player} ({l[0][0]}) WON')
      return True

    s4 = { l[0+i][len(l)-1-i] for i in range(len(l))}    # Checking Diagonal R to L
    if len(s4) == 1 and '_' not in s4:
      Player = 'Player 1' if self.player1 ==l[0][len(l)-1] else 'Player 2'
      print(f'\n{Player} ( {l[0][len(l)-1]} ) WON')
      return True
    
    return False
    
    
    

if __name__ == '__main__':
    print('\nEnter the Size of board n x n.\nwhere n>=2 ')
    n= int(input())
    if n<2: raise InvalidBoard('***Cannot be created with this value')

    m = match(n)
    m.start()

    while not m.check_if_won():
      m.play()
      
    m.printboard()
    print('Game Over')