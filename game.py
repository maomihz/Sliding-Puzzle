import random
import curses

# window initialization
stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
stdscr.keypad(1)
curses.cbreak()

# print some text
stdscr.addstr(0,1,"Sliding Puzzle By MaomiHz",curses.color_pair(1))
stdscr.addstr(1,1,"Press q to exit",curses.A_STANDOUT)

def swap(ary,index1,index2) :
    temp = ary[index1]
    ary[index1] = ary[index2]
    ary[index2] = temp

def advance(ary,dir):
    for i in range(0,16):
        if ary[i] == 0:
            zeropos = i
    zerox = revparse(zeropos)[0]
    zeroy = revparse(zeropos)[1]
    if dir == 0:
        if zerox + 1 < 4:
            swap(ary,parse(zerox,zeroy),parse(zerox+1,zeroy))
    elif dir == 1:
        if zeroy + 1 < 4:
            swap(ary,parse(zerox,zeroy),parse(zerox,zeroy+1))
    elif dir == 2:
        if zerox - 1 >= 0:
            swap(ary,parse(zerox,zeroy),parse(zerox - 1,zeroy))
    elif dir == 3:
        if zeroy - 1 >= 0:
            swap(ary,parse(zerox,zeroy),parse(zerox,zeroy - 1))

def parse(x,y):
    return x*4 + y

def revparse(loc):
    return [loc/4,loc%4]

def checkwin(list):
    for i in range(0,15):
        if list[i] != i + 1:
            return False
    return True

while True:
    list = range(1,17)
    list[15] = 0

    for i in range(1,1000):
        advance(list,random.randint(0,3))


    userin = ' '
    while userin != ord('n'):
    
        if userin == ord('w') or userin == 259:
            advance(list,0)
        elif userin == ord('d') or userin == 261:
            advance(list,3)
        elif userin == ord('s') or userin == 258:
            advance(list,2)
        elif userin == ord('a') or userin == 260:
            advance(list,1)
        elif userin == ord('q') or userin == 27:
            curses.endwin()
            exit()

        stdscr.move(3,1)
        for i in range(0,4):
            for j in range(0,4):
                if list[i*4+j] != 0:
                    stdscr.addstr("{0:4d}".format(list[i*4+j]))
                else:
                    stdscr.addstr("    ")
            stdscr.move(i+4,1)

        if checkwin(list):
            stdscr.addstr(8,1,"You win!!! Press n to restart")
        else:
            stdscr.addstr(8,1," "*30)


        stdscr.refresh()
        userin = stdscr.getch()
#        stdscr.move(11,1)
#        stdscr.addstr("{0:4d}".format(userin))
curses.endwin()
    

