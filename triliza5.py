import random
class tic_tac_toe:
  
  
  def __init__(self):
    self.board=[' ']*10

  def eisagvgi_paiktvn(self):
    self.name2='Robot'
    self.name1, self.symbol1=input('Give name and symbol to play(Peter Χ) : ').split()
    if self.symbol1=='X':
      self.symbol2='O'
    else: self.symbol2='X'
    self.name=random.choice((self.name1, self.name2))
    self.symbol=' '
    
  def display_board(self):
    banner = '+-----------+'
    grammi1='|7  |8  |9  |'
    grammi2='| ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9]+' |'
    grammi3='|4  |5  |6  |'
    grammi4='| ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6]+' |'
    grammi5='|1  |2  |3  |'
    grammi6='| ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3]+' |'
    grammes=[banner,grammi1,grammi2,banner,grammi3,grammi4,banner,grammi5,grammi6, banner]
    pinakas='\n'.join(grammes)
    print(pinakas)

  def play_player(self): 
    while True :
      epilogi = input("{} play ? (1-9) :  ".format(self.name1))
      if epilogi not in list('123456789') or self.board[int(epilogi)] != ' ':
        print('pick a free numbered square \n')
      else:
        self.board[int(epilogi)]=self.symbol1
        break
      
  def play_robot(self):
    options=[i for i in range(1,10) if self.board[i]==' ']
    for i in options:#check for win
      self.board[int(i)]=self.symbol2
      if self.win_check(self.symbol2):
        return
      else:
        self.board[int(i)]=' ' 
    for i in options: #check for loses
      self.board[int(i)]=self.symbol1
      if self.win_check(self.symbol1):
        self.board[int(i)]=self.symbol2
        return
      else:
        self.board[int(i)]=' '
    #avoid fork
    if self.board[5]==self.symbol2 and self.board[1]==self.symbol1 and self.board[9]==self.symbol1 and self.board[2]==' ' and self.board[4]==' ' and self.board[6]==' ' and self.board[8]==' ':
      self.board[2]=self.symbol2
      return
    #avoid fork 
    if self.board[5]==self.symbol2 and self.board[3]==self.symbol1 and self.board[7]==self.symbol1 and self.board[2]==' ' and self.board[4]==' ' and self.board[6]==' ' and self.board[8]==' ':
      self.board[2]=self.symbol2
      return
    for i in options: #Robot tries to make a fork
      self.board[int(i)]=self.symbol2
      new_options=[i for i in range(1,10) if self.board[i]==' ']
      ways_to_win=0
      for j in new_options:
        self.board[int(j)]=self.symbol2
        if self.win_check(self.symbol2):
          ways_to_win+=1
        self.board[int(j)]=' '
      if ways_to_win==2:
        return
      else:
        self.board[int(i)]=' '
    for i in options: #Stop players fork not sure if it evers play
      self.board[int(i)]=self.symbol1
      new_options=[i for i in range(1,10) if self.board[i]==' ']
      ways_to_win=0
      for j in new_options:
        self.board[int(j)]=self.symbol1
        if self.win_check(self.symbol1):
          ways_to_win+=1
        self.board[int(j)]=' '
      if ways_to_win==2:
        self.board[int(i)]=self.symbol2
        return
      else:
        self.board[int(i)]=' '
    if self.board[5]==' ': #check for center
      self.board[5]=self.symbol2
      return
    for i in options: #check for corner
      if i in (1,3,5,7):
        self.board[i]=self.symbol2
        return
    self.board[random.choice(options)]=self.symbol2#get random

  def next_player(self):
    if self.name==self.name1:
      self.name=self.name2
    else:
      self.name=self.name1
  
  def win_check(self,marker): 
    win_options=('123','456','789','147','258','369','357','159')
    for option in win_options:
      if self.board[int(option[0])]==self.board[int(option[1])]==self.board[int(option[2])]==marker:
        return True
    return False

  def check_full(self):
    return all(map(lambda x: x!=' ', self.board[1:]))

  def main(self):
    self.eisagvgi_paiktvn()
    self.display_board()
    while True:
      if self.name==self.name1:
        self.symbol=self.symbol1
        self.play_player()
      else:
        self.symbol=self.symbol2
        print('{} plays'.format(self.name2))
        self.play_robot()
      self.display_board()
      if self.win_check(self.symbol):
        print('{} wins!!!'.format(self.name))
        break
      elif self.check_full():
        print('Draw!!!')
        break
      self.next_player()
 
if __name__=='__main__':
  a=tic_tac_toe()
  a.main()
  while True:
    play_again=input('Want to play again (y for yes) : ')
    if play_again=='y':
      del a
      a=tic_tac_toe()
      a.main()
    else: break
  
 

