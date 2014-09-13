import random
import curses

# window initialization
stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
stdscr.keypad(1)
curses.cbreak()

size = 3
gamewin = curses.newwin(9+2,9*4 + 2,2,6)
infowin = curses.newwin(5,9*4 + 2,13,6)
infowin.border(0,0,0,0)
infowin.attron(curses.color_pair(1))

#Direction Constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


# print some text
text = "Sliding Puzzle By MaomiHz"
stdscr.addstr(0,curses.COLS / 2 - len(text) / 2,"Sliding Puzzle By MaomiHz",curses.color_pair(1))
text = "Press q to exit..."
stdscr.addstr(20,curses.COLS - len(text),"Press q to exit",curses.A_STANDOUT)


#:::Functions:::

#make a move -- dir constants:
# 0 is up,   1 is right, 
# 2 is down, 3 is left,
def advance(ary,dir):
	zero = getZero(ary)
	if canMove(ary,dir):
		if dir == UP:
			ary[zero[0]][zero[1]] = ary[zero[0] + 1][zero[1]]
			ary[zero[0] + 1][zero[1]] = 0
		elif dir == DOWN:
			ary[zero[0]][zero[1]] = ary[zero[0] - 1][zero[1]]
			ary[zero[0] - 1][zero[1]] = 0
		elif dir == LEFT:
			ary[zero[0]][zero[1]] = ary[zero[0]][zero[1] + 1]
			ary[zero[0]][zero[1] + 1] = 0
		elif dir == RIGHT:
			ary[zero[0]][zero[1]] = ary[zero[0]][zero[1] - 1]
			ary[zero[0]][zero[1] - 1] = 0
	

def canMove(ary,dir):
	zero = getZero(ary)
	
	if dir == UP:
		if zero[0] + 1 >= len(ary): return False
	elif dir == DOWN:
		if zero[0] - 1 < 0: return False
	elif dir == LEFT:
		if zero[1] + 1 >= len(ary): return False
	elif dir == RIGHT:
		if zero[1] - 1 < 0: return False
	else:
		return False
		
	return True
	
def getZero(ary):
	for i in range(0,len(ary)):
		for j in range(0,len(ary[i])):
			if ary[i][j] == 0: 
				return [i,j]
	return [0,0]

#checkwin
def checkwin(list):
	length = len(list)
	for i in range(0,length):
		for j in range(0,length):
			if list[i][j] != i * length + j + 1 and list[i][j] != 0:
				return False
	return True

#initialize a new list with given size
def initlist(size):
	list = []
	for i in range(0,size):
		sublist = []
		for j in range(0,size):
			sublist.append(i*size+j+1)
		list.append(sublist)
	list[size-1][size-1] = 0
	return list
				
#shuffle the list
def shuffle(list):
	for i in range(1,5000):
		advance(list,random.randint(0,3))


# Start of the game...
while True:
	list = initlist(size)	
	shuffle(list)
	
	userin = ' '
	while userin != ord('n'):
	
		if userin == ord('w') or userin == curses.KEY_UP or userin == ord('k'):
			advance(list,UP)
		elif userin == ord('d') or userin == curses.KEY_RIGHT or userin == ord('l'):
			advance(list,RIGHT)
		elif userin == ord('s') or userin == curses.KEY_DOWN or userin == ord('j'):
			advance(list,DOWN)
		elif userin == ord('a') or userin == curses.KEY_LEFT or userin == ord('h'):
			advance(list,LEFT)
		elif userin == ord('q') or userin == 27:
			curses.endwin()
			exit()
		gamewin.border(0,0,0,0,0,0,0,0)
		for i in range(0,size):
			gamewin.move(i+1,1)
			for j in range(0,size):
				if list[i][j] != 0:
					gamewin.addstr("{0:4d}".format(list[i][j]))
				else:
					gamewin.addstr(" "*4)

		if checkwin(list):
			infowin.addstr(2,2,"You win!!! Press n to restart")
		else:
			infowin.addstr(2,2,"Press Arrow Key To Play...   ")
			infowin.border(0,0,0,0)

		stdscr.refresh()
		gamewin.refresh()
		infowin.refresh()
		userin = stdscr.getch()

#End of the program
curses.endwin()
	

