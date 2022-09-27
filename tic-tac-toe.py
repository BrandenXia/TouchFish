import curses
import random

# init windows
stdscr = curses.initscr()
# init variables
mousePos_Y = 3
mousePos_X = 6
turn_X = True
# [[Y1, X1, status1], [Y2, X2, status2]]
inPlace = []
turns = 0
AImode = False


# setup window
def setup_window():
    """
    -------------
    |1,2|1,6|1,10|
    -------------
    |3,2|3,6|3,10|
    -------------
    |5,2|5,6|5,10|
    -------------
    """
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    # draw board
    stdscr.addstr(0, 0,
                  "-------------\n"
                  "|   |   |   |\tMode: Human Mode\n"
                  "-------------\n"
                  f"|   |   |   |\tTurns: {turns}\n"
                  "-------------\n"
                  "|   |   |   |\tNext Player: X\n"
                  "-------------\n\n\n\n"
                  "Press 'w' or up key to move up\n"
                  "Press 's' or down key to move down\n"
                  "Press 'a' or left key to move left\n"
                  "Press 'd' or right key to move right\n"
                  "Press Enter to place a mark\n"
                  "Press 'm' to change the mode (human / AI)\n"
                  "Press 'r' to restart\n"
                  "Press 'q' to quit")
    # draw mouse
    stdscr.addstr(mousePos_Y, mousePos_X, "")
    # refresh window
    stdscr.refresh()


def input_and_react():
    global mousePos_Y, mousePos_X, turn_X, turns, inPlace, AImode
    while True:
        # get mouse input
        key = stdscr.getch()
        # move mouse
        if key == ord('w') or key == curses.KEY_UP:
            if mousePos_Y > 1:
                mousePos_Y -= 2
        elif key == ord('s') or key == curses.KEY_DOWN:
            if mousePos_Y < 5:
                mousePos_Y += 2
        elif key == ord('a') or key == curses.KEY_LEFT:
            if mousePos_X > 2:
                mousePos_X -= 4
        elif key == ord('d') or key == curses.KEY_RIGHT:
            if mousePos_X < 8:
                mousePos_X += 4
        # place mark
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if [mousePos_Y, mousePos_X] not in [[i[0], i[1]] for i in inPlace]:
                inPlace.append([mousePos_Y, mousePos_X, turn_X])
                turn_X = not turn_X
                turns += 1
            # draw marks
            draw_marks()
            # judgement
            if AImode:
                judgement_ai()
                judgement_result()
            else:
                judgement_result()
        # change mode
        elif key == ord('m'):
            AImode = not AImode
            restart_window()
        # restart
        elif key == ord('r'):
            restart_window()
        # quit
        elif key == ord('q'):
            break
        # draw mode
        if AImode:
            stdscr.addstr(1, 13, "\tMode: AI Mode   ")
        else:
            stdscr.addstr(1, 13, "\tMode: Human Mode")
        # draw turns
        stdscr.addstr(3, 13, f"\tTurns: {turns}")
        # draw next player
        if turn_X:
            stdscr.addstr(5, 13, "\tNext Player: X")
        else:
            stdscr.addstr(5, 13, "\tNext Player: O")
        # draw mouse
        stdscr.addstr(mousePos_Y, mousePos_X, "")
        # refresh window
        stdscr.refresh()


def draw_marks():
    # draw marks
    for i in inPlace:
        if i[2]:
            stdscr.addstr(i[0], i[1], "X", curses.A_BOLD)
        else:
            stdscr.addstr(i[0], i[1], "O", curses.A_BOLD)


def judgement_result():
    # get all positions of X and O
    x = [x[0:2] for x in inPlace if x[2]]
    o = [y[0:2] for y in inPlace if not y[2]]
    # check if X wins
    for i in x:
        # horizontal
        if [i[0], i[1] + 4] in x and [i[0], i[1] + 8] in x:
            stdscr.addstr(8, 0, "X wins!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
        # vertical
        elif [i[0] + 2, i[1]] in x and [i[0] + 4, i[1]] in x:
            stdscr.addstr(8, 0, "X wins!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
        # diagonal
        elif [i[0] + 2, i[1] + 4] in x and [i[0] + 4, i[1] + 8] in x:
            stdscr.addstr(8, 0, "X wins!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
        elif [i[0] + 2, i[1] - 4] in x and [i[0] + 4, i[1] - 8] in x:
            stdscr.addstr(8, 0, "X wins!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
    # check if O wins
    for i in o:
        # horizontal
        if [i[0], i[1] + 4] in o and [i[0], i[1] + 8] in o:
            stdscr.addstr(8, 0, "O wins!",  curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
        # vertical
        elif [i[0] + 2, i[1]] in o and [i[0] + 4, i[1]] in o:
            stdscr.addstr(8, 0, "O wins!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
        # diagonal
        elif [i[0] + 2, i[1] + 4] in o and [i[0] + 4, i[1] + 8] in o:
            stdscr.addstr(8, 0, "O wins!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
        elif [i[0] + 2, i[1] - 4] in o and [i[0] + 4, i[1] - 8] in o:
            stdscr.addstr(8, 0, "O wins!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            restart_window()
    # check if draw
    if turns == 9:
        stdscr.addstr(8, 0, "Draw!", curses.A_BOLD)
        stdscr.refresh()
        curses.napms(1000)
        restart_window()


def judgement_ai():
    global turn_X, turns, inPlace
    not_available_place = [i[0:2] for i in inPlace]
    x_place = [x[0:2] for x in inPlace if x[2]]
    all_place = [[1, 2], [1, 6], [1, 10], [3, 2], [3, 6], [3, 10], [5, 2], [5, 6], [5, 10]]
    available_place = [i for i in all_place if i not in not_available_place]
    del not_available_place, all_place
    if not turn_X and turns < 9:
        for i in x_place:
            if [i[0], i[1] + 4] in x_place and [i[0], i[1] + 8] in available_place:
                inPlace.append([i[0], i[1] + 8, turn_X])
                break
            elif [i[0], i[1] + 4] in available_place and [i[0], i[1] + 8] in x_place:
                inPlace.append([i[0], i[1] + 4, turn_X])
                break
            elif [i[0], i[1] - 4] in x_place and [i[0], i[1] - 8] in available_place:
                inPlace.append([i[0], i[1] - 8, turn_X])
                break
            elif [i[0], i[1] - 4] in available_place and [i[0], i[1] - 8] in x_place:
                inPlace.append([i[0], i[1] - 4, turn_X])
                break
            elif [i[0] + 2, i[1]] in x_place and [i[0] + 4, i[1]] in available_place:
                inPlace.append([i[0] + 4, i[1], turn_X])
                break
            elif [i[0] + 2, i[1]] in available_place and [i[0] + 4, i[1]] in x_place:
                inPlace.append([i[0] + 2, i[1], turn_X])
                break
            elif [i[0] - 2, i[1]] in x_place and [i[0] - 4, i[1]] in available_place:
                inPlace.append([i[0] - 4, i[1], turn_X])
                break
            elif [i[0] - 2, i[1]] in available_place and [i[0] - 4, i[1]] in x_place:
                inPlace.append([i[0] - 2, i[1], turn_X])
                break
            elif [i[0] + 2, i[1] + 4] in x_place and [i[0] + 4, i[1] + 8] in available_place:
                inPlace.append([i[0] + 4, i[1] + 8, turn_X])
                break
            elif [i[0] + 2, i[1] + 4] in available_place and [i[0] + 4, i[1] + 8] in x_place:
                inPlace.append([i[0] + 2, i[1] + 4, turn_X])
                break
            elif [i[0] + 2, i[1] - 4] in x_place and [i[0] + 4, i[1] - 8] in available_place:
                inPlace.append([i[0] + 4, i[1] - 8, turn_X])
                break
            elif [i[0] + 2, i[1] - 4] in available_place and [i[0] + 4, i[1] - 8] in x_place:
                inPlace.append([i[0] + 2, i[1] - 4, turn_X])
                break
            elif [i[0] - 2, i[1] + 4] in x_place and [i[0] - 4, i[1] + 8] in available_place:
                inPlace.append([i[0] - 4, i[1] + 8, turn_X])
                break
            elif [i[0] - 2, i[1] + 4] in available_place and [i[0] - 4, i[1] + 8] in x_place:
                inPlace.append([i[0] - 2, i[1] + 4, turn_X])
                break
            elif [i[0] - 2, i[1] - 4] in x_place and [i[0] - 4, i[1] - 8] in available_place:
                inPlace.append([i[0] - 4, i[1] - 8, turn_X])
                break
            elif [i[0] - 2, i[1] - 4] in available_place and [i[0] - 4, i[1] - 8] in x_place:
                inPlace.append([i[0] - 2, i[1] - 4, turn_X])
                break
            elif i == x_place[-1]:
                inPlace.append([random.choice(available_place)[0], random.choice(available_place)[1], turn_X])
        turns += 1
        turn_X = not turn_X
    else:
        pass
    # draw marks
    draw_marks()


def restart_window():
    global mousePos_Y, mousePos_X, turn_X, turns, inPlace
    # restart window
    setup_window()
    # reset variables
    mousePos_Y = 3
    mousePos_X = 6
    turn_X = True
    inPlace = []
    turns = 0


def end_window():
    # end window
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


def main():
    # start window
    setup_window()
    # main loop
    input_and_react()
    # end window
    end_window()


if __name__ == "__main__":
    main()
