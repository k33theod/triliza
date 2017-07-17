from tkinter import *
from tkinter.messagebox import *
import random
import sys

class tic:
  def __init__(self):
    self.a=Tk()
    self.a.title('TIC TAC TOE')
    self.initialize()
    self.eisagvgi_paiktvn()
    
  
  def initialize(self):
    self.board=[' ']*10
    self.buttons=[]
    self.buttons.append(1)
    self.draw()
    
  
  def draw(self): 
    self.main_frame=Frame(self.a)
    self.main_frame.pack(fill=BOTH, expand=YES) 
  
    self.button1=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button1)))
    self.button1.config(height=10, width=20, text=' ')
    self.button1.grid(row = 2, column=0)
    self.buttons.append(self.button1)
    
    self.button2=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button2)))
    self.button2.config(height=10, width=20, text=' ')
    self.button2.grid(row = 2, column=1)
    self.buttons.append(self.button2)
    
    self.button3=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button3)))
    self.button3.config(height=10, width=20, text=' ')
    self.button3.grid(row = 2, column=2)
    self.buttons.append(self.button3)
    
    self.button4=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button4)))
    self.button4.config(height=10, width=20, text=' ')
    self.button4.grid(row = 1, column=0)
    self.buttons.append(self.button4)
    
    self.button5=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button5)))
    self.button5.config(height=10, width=20, text=' ')
    self.button5.grid(row = 1, column=1)
    self.buttons.append(self.button5)
    
    self.button6=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button6)))
    self.button6.config(height=10, width=20, text=' ')
    self.button6.grid(row = 1, column=2)
    self.buttons.append(self.button6)
    
    self.button7=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button7)))
    self.button7.config(height=10, width=20, text=' ')
    self.button7.grid(row = 0, column=0)
    self.buttons.append(self.button7)
    
    self.button8=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button8)))
    self.button8.config(height=10, width=20, text=' ')
    self.button8.grid(row = 0, column=1)
    self.buttons.append(self.button8)
    
    self.button9=Button(self.main_frame, bd=5, relief=RAISED, command=(lambda:self.play_player(self.button9)))
    self.button9.config(height=10, width=20, text=' ')
    self.button9.grid(row = 0, column=2)
    self.buttons.append(self.button9)

    self.quit_button=Button(self.main_frame, text='Quit', command=self.a.quit)
    self.quit_button.grid(row=3, column=2)
  
  def eisagvgi_paiktvn(self):
    self.players_win=Toplevel(self.a)
    label1=Label(self.players_win, text='Name')
    self.entry_name=Entry(self.players_win, width=30)
    self.entry_name.focus_set()
    label2=Label(self.players_win, text='Symbol')
    self.entry_symbol=Entry(self.players_win, width=30)  
    label1.grid(column=0, row=0)
    label2.grid(column=0, row=1)
    self.entry_name.grid(column=1, row=0)
    self.entry_symbol.grid(column=1, row=1)
    button_ok=Button(self.players_win, text='OK', command=self.get_name)
    button_ok.grid(column=1, row=2)
    self.a.mainloop()
    self.players_win.focus_set() 
    self.players_win.grab_set() # disable other windows while I'm open,
    self.players_win.wait_window()    
    
  def get_name(self):
    self.paiktes = {}
    self.name2 = 'Robot'
    self.name1=self.entry_name.get()
    self.symbol1=self.entry_symbol.get()
    if self.symbol1 == 'X':
      self.symbol2 = 'O'
    else:
      self.symbol2 = 'X'
    self.paiktes[self.name1]=self.symbol1
    self.paiktes[self.name2]=self.symbol2
    self.name = random.choice((self.name1, self.name2))
    self.symbol = self.paiktes[self.name]
    self.players_win.destroy()
    self.main()
    self.a.focus_set()
    
  def play_player(self,button):
    self.board[self.buttons.index(button)]=self.symbol1
    button.config(text=self.symbol1, relief=SUNKEN, state=DISABLED)
    if self.win_check(self.symbol1):
      if askyesno('{} Wins'.format(self.name1), 'Do you want to play again ?'):
        self.main_frame.destroy()
        self.initialize()
      else:
        self.a.quit()
    elif self.check_full():
      if askyesno('Draw!!!', 'Do you want to play again ?'):
        self.main_frame.destroy()
        self.initialize()
      else:
        self.a.quit()
    self.next_player()
    self.main()
    
  def main(self):
    if self.name==self.name2:
      self.play_robot()
    else:
      return
    if self.win_check(self.symbol2):
      if askyesno('{} Wins'.format(self.name2), 'Do you want to play again ?'):
        self.main_frame.destroy()
        self.initialize()
      else:
        self.a.quit()
    elif self.check_full():
      if askyesno('Draw!!!', 'Do you want to play again ?'):
        self.main_frame.destroy()
        self.initialize()
      else:
        self.a.quit()
    self.next_player()
      
  def next_player(self):
    if self.name==self.name1:
      self.name=self.name2
      self.symbol=self.symbol2
    else:
      self.name=self.name1
      self.symbol=self.symbol1
    
  def win_check(self,marker): 
    win_options=('123','456','789','147','258','369','357','159')
    for option in win_options:
      if self.board[int(option[0])]==self.board[int(option[1])]==self.board[int(option[2])]==marker:
        return True
    return False  
    
  def check_full(self):
    return all(map(lambda x: x!=' ', self.board[1:]))

  def robot_click(self,box):
    box.config(text=self.symbol2, relief=SUNKEN, state=DISABLED)
  
  def play_robot(self):
    options=[i for i in range(1,10) if self.board[i]==' ']
    for i in options:#check for win
      self.board[int(i)]=self.symbol2
      if self.win_check(self.symbol2):
        self.robot_click(self.buttons[i])
        return
      else:
        self.board[int(i)]=' ' 
    
    for i in options: #check for loses
      self.board[int(i)]=self.symbol1
      if self.win_check(self.symbol1):
        self.board[int(i)]=self.symbol2
        self.robot_click(self.buttons[i])
        return
      else:
        self.board[int(i)]=' '

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
        self.robot_click(self.buttons[i])
        return
      else:
        self.board[int(i)]=' ' 

    
    #avoid fork
    if self.board[5]==self.symbol2 and self.board[1]==self.symbol1 and self.board[9]==self.symbol1 and self.board[2]==' ' and self.board[4]==' ' and self.board[6]==' ' and self.board[8]==' ':
      self.board[2]=self.symbol2
      self.robot_click(self.buttons[2])
      return
    
    #avoid fork 
    if self.board[5]==self.symbol2 and self.board[3]==self.symbol1 and self.board[7]==self.symbol1 and self.board[2]==' ' and self.board[4]==' ' and self.board[6]==' ' and self.board[8]==' ':
      self.board[2]=self.symbol2
      self.robot_click(self.buttons[2])
      return
    
    
    
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
        self.robot_click(self.buttons[i])
        return
      else:
        self.board[int(i)]=' '
    
    if self.board[5]==' ': #check for center
      self.board[5]=self.symbol2
      self.robot_click(self.buttons[5])
      return
    
    for i in options: #check for corner
      if i in (1,3,5,7):
        self.board[i]=self.symbol2
        self.robot_click(self.buttons[i])
        return
    
    a=random.choice(options)
    self.board[a]=self.symbol2#get random
    self.robot_click(self.buttons[a])
      
if __name__=='__main__':
  a=tic()
  
#,width=300, height=300,
