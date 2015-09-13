import curses
from curses.textpad import Textbox, rectangle

def main() :
    choice = raw_input("Enter filename : ")
    screen = curses.initscr()
    curses.noecho()

    with open(choice, 'w+') as rf:
        filedata = rf.read()
        
    editwin = curses.newwin(20,70, 2,1)
    editwin.addstr(1,1,filedata)
    rectangle(screen, 1,0, 1+20+1, 1+70+1)
    screen.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()
        
    curses.endwin()

    with open(choice,'w+') as wf:
        wf.write(message)
    
if  __name__ =='__main__':
    main()
