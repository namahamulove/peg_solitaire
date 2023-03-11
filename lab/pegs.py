import tkinter
import copy
import peg
import time

mouse_x = 0
mouse_y = 0
mouse_c = 0

check_x = 0
check_y = 0
size = 80

index = 0
qnum = 0
sum = 0

turn = 0
solutions = [peg.getsolution("54"), peg.getsolution("231"), peg.getsolution("278a")]

board = []

sboard = [
[[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 0, 0, 2, 2, 2, 0, 0, 1],
[1, 0, 2, 2, 2, 2, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1]],

[[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 2, 0, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 0, 2, 0, 2, 2, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 1],
[1, 1, 1, 0, 2, 0, 1, 1, 1],
[1, 1, 1, 0, 2, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1]],

[[1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 2, 2, 2, 1, 1, 1],
[1, 1, 1, 2, 2, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 0, 2, 2, 2, 1],
[1, 2, 2, 0, 0, 2, 0, 0, 1],
[1, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1]]
]


def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def draw_ball():
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                cvs.create_image(x*size+60, y*size+50, image=noball, tag="BALL")
            elif board[y][x] == 2:
                cvs.create_image(x*size+60, y*size+50, image=ball, tag="BALL")
            elif board[y][x] == 7:
                cvs.create_image(x*size+60, y*size+50, image=cheball, tag="BALL")

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def mouse_click(e):
    global mouse_c
    global check_x
    global check_y
    global board
    global qnum
    global index
    if mouse_c == 0:
        check_x = int((mouse_x - 60 + (size / 2)) / size)
        check_y = int((mouse_y - 50 + (size / 2)) / size)
        if index == 1:
            mouse_c = 1
        elif index == 2 and 668 < mouse_x and mouse_x < 856 and 384 < mouse_y and mouse_y < 456:
            index = 0
        elif index == 2 and 668 < mouse_x and mouse_x < 856 and 528 < mouse_y and mouse_y < 600:
            board = copy.deepcopy(sboard[qnum-1])
        elif index == 2 and board[check_y][check_x] == 2:
            board[check_y][check_x] = 7
            mouse_c = 1
        elif index == 6:
            mouse_c = 1
    elif mouse_c == 1 and index == 2:
        #上への遷移
        if int((mouse_x - 60 + (size / 2)) / size) == check_x and int((mouse_y - 50 + (size / 2)) / size) == check_y-2 and check_y >= 3 and board[check_y-1][check_x] == 2 and board[check_y-2][check_x] == 0:
            board[check_y][check_x] = 0
            board[check_y-1][check_x] = 0
            board[check_y-2][check_x] = 2
            check_x = 0
            check_y = 0
            mouse_c = 0
        #下への遷移
        elif int((mouse_x - 60 + (size / 2)) / size) == check_x and int((mouse_y - 50 + (size / 2)) / size) == check_y+2 and check_y <= 5 and board[check_y+1][check_x] == 2 and board[check_y+2][check_x] == 0:
            board[check_y][check_x] = 0
            board[check_y+1][check_x] = 0
            board[check_y+2][check_x] = 2
            check_x = 0
            check_y = 0
            mouse_c = 0
        #左への遷移
        elif int((mouse_x - 60 + (size / 2)) / size) == check_x-2 and int((mouse_y - 50 + (size / 2)) / size) == check_y and check_x >= 3  and board[check_y][check_x-1] == 2 and board[check_y][check_x-2] == 0:
            board[check_y][check_x] = 0
            board[check_y][check_x-1] = 0
            board[check_y][check_x-2] = 2
            check_x = 0
            check_y = 0
            mouse_c = 0
        #右への遷移
        elif int((mouse_x - 60 + (size / 2)) / size) == check_x+2 and int((mouse_y - 50 + (size / 2)) / size) == check_y and check_x <= 5  and board[check_y][check_x+1] == 2 and board[check_y][check_x+2] == 0:
            board[check_y][check_x] = 0
            board[check_y][check_x+1] = 0
            board[check_y][check_x+2] = 2
            check_x = 0
            check_y = 0
            mouse_c = 0
        elif int((mouse_x - 60 + (size / 2)) / size) == check_x and int((mouse_y - 50 + (size / 2)) / size) == check_y:
            board[check_y][check_x] = 2
            check_x = 0
            check_y = 0
            mouse_c = 0
        else:
            pass

def game_main():
    global index, mouse_c, qnum, turn, board, solutions
    if index == 0: #タイトルロゴ
        cvs.delete("BALL")
        draw_txt("ペグソリティア", 412, 240, 80, "violet", "TITLE")
        cvs.create_rectangle(268, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("簡単", 362, 420, 40, "white", "TITLE")
        cvs.create_rectangle(268, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("普通", 362, 564, 40, "white", "TITLE")
        cvs.create_rectangle(268, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("難しい", 362, 708, 40, "white", "TITLE")

        cvs.create_rectangle(568, 384, 756, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("解答", 662, 420, 40, "white", "TITLE")
        cvs.create_rectangle(568, 528, 756, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("解答", 662, 564, 40, "white", "TITLE")
        cvs.create_rectangle(568, 672, 756, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("解答", 662, 708, 40, "white", "TITLE")

        index = 1
        mouse_c = 0
    elif index == 1: #タイトル画面　スタート待ち
        qnum = 0

        if mouse_c == 1:
            if 268 < mouse_x and mouse_x < 456 and 384 < mouse_y and mouse_y < 456:
                qnum = 1
                mouse_c = 0
            elif 268 < mouse_x and mouse_x < 456 and 528 < mouse_y and mouse_y < 600:
                qnum = 2
                mouse_c = 0
            elif 268 < mouse_x and mouse_x < 456 and 672 < mouse_y and mouse_y < 744:
                qnum = 3
                mouse_c = 0
            elif 568 < mouse_x and mouse_x < 756 and 384 < mouse_y and mouse_y < 456:
                qnum = 4
                mouse_c = 0
            elif 568 < mouse_x and mouse_x < 756 and 528 < mouse_y and mouse_y < 600:
                qnum = 5
                mouse_c = 0
            elif 568 < mouse_x and mouse_x < 756 and 672 < mouse_y and mouse_y < 744:
                qnum = 6
                mouse_c = 0

        mouse_c = 0
        
        if qnum > 0 and qnum < 4:
            mouse_c = 0
            cvs.delete("TITLE")
            #盤面の読み込み
            board = copy.deepcopy(sboard[qnum-1])
            index = 2
        elif qnum >= 4:
            mouse_c = 0
            turn = 0
            cvs.delete("TITLE")
            index = 5
    elif index == 2:
        cvs.delete("BALL")
        draw_ball()
        cvs.create_rectangle(668, 384, 886, 456, fill="skyblue", width=0, tag="BALL")
        draw_txt("タイトル", 772, 420, 40, "white", "BALL")
        cvs.create_rectangle(668, 528, 856, 600, fill="lightgreen", width=0, tag="BALL")
        draw_txt("reset", 762, 564, 40, "white", "BALL")
    elif index == 5:
        board = []
        for i in solutions[qnum-4][turn]:
            board.append(i)
        cvs.delete("BALL")
        draw_ball()
        cvs.create_rectangle(678, 384, 896, 456, fill="skyblue", width=0, tag="BALL")
        draw_txt("タイトル", 782, 420, 40, "white", "BALL")
        cvs.create_rectangle(508, 584, 696, 656, fill="lightgreen", width=0, tag="BALL")
        draw_txt("前へ", 612, 620, 40, "white", "BALL")
        cvs.create_rectangle(708, 584, 896, 656, fill="orange", width=0, tag="BALL")
        draw_txt("次へ", 812, 620, 40, "white", "BALL")
        index = 6
    elif index == 6:
        if mouse_c == 1:
            if 708 < mouse_x and mouse_x < 896 and 384 < mouse_y and mouse_y < 456:
                index = 0
                mouse_c = 0
            if 508 < mouse_x and mouse_x < 696 and 584 < mouse_y and mouse_y < 656:
                turn = turn-1 if turn > 0 else turn
                index = 5
                mouse_c = 0
            if 708 < mouse_x and mouse_x < 896 and 584 < mouse_y and mouse_y < 656:
                turn = turn+1
                index = 5
                mouse_c = 0
    root.after(100, game_main)

root = tkinter.Tk()
root.title("ペグソリティア")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_click)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="board.png")
noball = tkinter.PhotoImage(file="NoBall.png")
ball = tkinter.PhotoImage(file="Ball.png")
cheball = tkinter.PhotoImage(file="CheBall.png")
cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()