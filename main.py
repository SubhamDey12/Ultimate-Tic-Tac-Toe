import tkinter
from tkinter import *
import tkinter.messagebox

# Creating the GUI Window
root = Tk()

# Creating the Title of the Output Window

root.title("Tic Tac Toe")

# Defining the size of the output window ( " width x height " )

root.geometry("1400x1015")

# Defining the minimum size ( width , height )

root.minsize(1400,1015)

# Defining the maximum size ( width , height )

root.maxsize(1400,1020)

# Creating the Heading
first_heading = Label(text = " TIC TAC TOE ", bg = "grey70",height = 2,width = 50,font = "times 55 bold",borderwidth = 1, relief = RIDGE)
first_heading.pack(fill = X)

Check_turn = True
B_name = StringVar()
win_var = False

def pinky(B_name) :
    global Check_turn
    global win_var
    if B_name["text"] == " " and Check_turn == True and win_var == False:
        B_name["text"] = "X"
        Check_turn = False
        is_win()
    elif B_name["text"] == " " and Check_turn == False and win_var == False:
        B_name["text"] = "O"
        Check_turn = True
        is_win()

def vs_comp(B_name) :
    global player_1_score_int
    global player_2_score_int
    global player_1_score
    global player_2_score
    play_again(B_name)
    player_1_score_int = 0
    player_1_score = str(player_1_score_int)
    player_1_text.set("Player X score :                " + player_1_score)
    player_2_score_int = 0
    player_2_score = str(player_2_score_int)
    player_2_text.set("Player O score :                " + player_2_score)


def vs_player(B_name) :
    global player_1_score_int
    global player_2_score_int
    global player_1_score
    global player_2_score
    play_again(B_name)
    player_1_score_int = 0
    player_1_score = str(player_1_score_int)
    player_1_text.set("Player X score :                " + player_1_score)
    player_2_score_int = 0
    player_2_score = str(player_2_score_int)
    player_2_text.set("Player O score :                " + player_2_score)

# Play Again Function

def play_again(B_name) :

    # Resetting the grid text

    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "

    # Resetting the grid colour

    b1.configure(bg="grey71")
    b2.configure(bg="grey71")
    b3.configure(bg="grey71")
    b4.configure(bg="grey71")
    b5.configure(bg="grey71")
    b6.configure(bg="grey71")
    b7.configure(bg="grey71")
    b8.configure(bg="grey71")
    b9.configure(bg="grey71")

    # Resetting the Player Count
    global Check_turn
    Check_turn = True

    # Resetting Win variable
    global win_var
    win_var = False


# The Win or Not Function
def is_win() :
    global win_var
    global player_1_score_int
    global player_2_score_int
    global val
    global val_str
    global player_1_score
    global player_2_score
    if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
        b1.configure(bg="light pink")
        b2.configure(bg="light pink")
        b3.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!","X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)


    elif (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X"):
        b4.configure(bg="light pink")
        b5.configure(bg="light pink")
        b6.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)

    elif (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
        b7.configure(bg="light pink")
        b8.configure(bg="light pink")
        b9.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)

    elif (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X"):
        b1.configure(bg="light pink")
        b4.configure(bg="light pink")
        b7.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)

    elif (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
        b2.configure(bg="light pink")
        b5.configure(bg="light pink")
        b8.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)

    elif (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
        b3.configure(bg="light pink")
        b6.configure(bg="light pink")
        b9.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)

    elif (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
        b1.configure(bg="light pink")
        b5.configure(bg="light pink")
        b9.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)

    elif (b7["text"]=="X" and b5["text"]=="X" and b3["text"]=="X"):
        b7.configure(bg="light pink")
        b5.configure(bg="light pink")
        b3.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "X Won the Game")
        win_var = True
        player_1_score_int += 1
        player_1_score = str(player_1_score_int)
        player_1_text.set("Player X score :                " + player_1_score)

    elif (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O"):
        b1.configure(bg="light pink")
        b2.configure(bg="light pink")
        b3.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)

    elif (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O"):
        b4.configure(bg="light pink")
        b5.configure(bg="light pink")
        b6.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)

    elif (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O"):
        b7.configure(bg="light pink")
        b8.configure(bg="light pink")
        b9.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)

    elif (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O"):
        b1.configure(bg="light pink")
        b4.configure(bg="light pink")
        b7.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)

    elif (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O"):
        b2.configure(bg="light pink")
        b5.configure(bg="light pink")
        b8.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)

    elif (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
        b3.configure(bg="light pink")
        b6.configure(bg="light pink")
        b9.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)

    elif (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O"):
        b1.configure(bg="light pink")
        b5.configure(bg="light pink")
        b9.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)

    elif (b7["text"]=="O" and b5["text"]=="O" and b3["text"]=="O"):
        b7.configure(bg="light pink")
        b5.configure(bg="light pink")
        b3.configure(bg="light pink")
        tkinter.messagebox.showinfo("!!! Winner !!!", "O Won the Game")
        win_var = True
        player_2_score_int += 1
        player_2_score = str(player_2_score_int)
        player_2_text.set("Player O score :                " + player_2_score)







# Creating the buttons

frame = Frame(root,)
frame.pack(side=LEFT,anchor = "nw")
b1 = Button(frame, borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold",fg = "green",bg="grey71",command= lambda:pinky(b1))
b1.pack()
b1.bind('<Button-1>', pinky)
b2 = Button(frame, borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold",fg = "green",bg="grey71",command= lambda:pinky(b2))
b2.pack()
b3 = Button(frame, borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold",fg = "green",bg="grey71",command= lambda:pinky(b3))
b3.pack()
frame2 = Frame(root)
frame2.pack(side=LEFT,anchor = "nw")
b4 = Button(frame2,borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold",fg = "green",bg="grey71",command= lambda:pinky(b4))
b4.pack()
b5 = Button(frame2,borderwidth= 1, text = " " ,height = 6,width = 10, font = "times  28 bold" ,fg = "green",bg="grey71",command= lambda:pinky(b5))
b5.pack()
b6 = Button(frame2, borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold" ,fg = "green",bg="grey71",command= lambda:pinky(b6))
b6.pack()
frame3 = Frame(root)
frame3.pack(side=LEFT,anchor = "nw")
b7 = Button(frame3, borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold",fg = "green",bg="grey71",command= lambda:pinky(b7))
b7.pack()
b8 = Button(frame3, borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold" ,fg = "green",bg="grey71",command= lambda:pinky(b8))
b8.pack()
b9 = Button(frame3, borderwidth= 1, text = " " ,height = 6,width = 10, font = "times 28 bold",fg = "green",bg="grey71",command= lambda:pinky(b9))
b9.pack()

# Creating the right Window

Right_frame = Frame(root,width = 500,height = 40,bg="red")
Right_frame.pack(side=LEFT,anchor = "nw")

player_1_score_int = IntVar()
player_2_score_int = IntVar()

player_1_score_int = 0
player_2_score_int = 0

player_1_score = StringVar()
player_2_score = StringVar()

player_1_score = str(player_1_score_int)
player_2_score = str(player_2_score_int)

player_1_text = StringVar()
player_2_text = StringVar()

player_1_text.set("Player X score :                " + player_1_score)
player_2_text.set("Player O score :                " + player_2_score)

Player_1_label = Label(Right_frame, textvariable = player_1_text ,width = 23, font=('arial',40,'bold'),bg = "grey71")
Player_1_label.grid(row=0,column=0,sticky = W)
Player_2_label = Label(Right_frame,  textvariable = player_2_text ,width = 23, font=('arial',40,'bold'),bg = "grey71")
Player_2_label.grid(row=1,column=0,sticky = W)




# Creating the right buttons
frame4 = Frame(Right_frame)
frame4.grid(sticky = W)
b_vs_comp = Button(frame4, borderwidth= 0.5, text = "V/S COMPUTER" ,height = 6,width = 34, font = "times 26 bold",fg = "black",bg="grey71",command= lambda:vs_comp(b_vs_comp), relief = RIDGE)
b_vs_comp.grid(sticky = W)
b_vs_player = Button(frame4, borderwidth= 0.5, text = "V/S HUMAN" ,height = 6,width = 34, font = "times 26 bold",fg = "black",bg="grey71",command= lambda:vs_player(b_vs_player), relief = RIDGE)
b_vs_player.grid(sticky = W)
b_play_again = Button(frame4, borderwidth= 0, text = "Play Again" ,height = 4,width = 34, font = "times 26 bold",fg = "black",bg="grey71",command= lambda:play_again(b_play_again), relief = RIDGE)
b_play_again.grid(sticky = W)




root.mainloop()
