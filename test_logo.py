# c_eyes.py - create a curses with a cowsay message
#
import curses , time, random

# create a curses object
stdscr = curses.initscr()
height, width = stdscr.getmaxyx() # get the window size

# define two color pairs
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

# Read the cowsay output file and write it to the screen

f = open("logo.txt", "r")
eyes = f.read()
stdscr.addstr(0, 0, eyes,curses.color_pair(3))

# Add a footer
stdscr.addstr(height-1, 0, " " * (width-1),curses.color_pair(1))
stdscr.addstr(height-1, 0, " Key Commands : q - to quit " ,curses.color_pair(1))

# Add intrusion code here....
stdscr.addstr(15, 5, "PIR1 input: no movement" ,curses.color_pair(2) )
stdscr.addstr(16, 5, "PIR2 input: no movement" ,curses.color_pair(2) )

curses.curs_set(0) # don't show the cursor
stdscr.refresh()

# Cycle to update text. Enter a 'q' to quit
k = 0
stdscr.nodelay(1)
while (k != ord('q')):
    k = stdscr.getch()

curses.endwin()