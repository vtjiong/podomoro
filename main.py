from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
check="✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
check_mark_text=""
timer2 = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_mark_text
    window.after_cancel(timer2)
    label.config(text="Timer",fg=GREEN)
    check_mark_text=""
    check_mark.config(text=check_mark_text)
    canvas.itemconfig(timer,text="00:00")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    if reps%2!=0:
        label.config(text="Work",fg=GREEN)
        count_down(WORK_MIN*60)
    elif reps/8==1:
        label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN* 60)
    else:
        label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN* 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(number):
    global timer2
    count_min=math.floor(number/60)
    count_sec=number % 60
    if count_sec<10:
        count_sec="0"+str(count_sec)
    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    #timer is the name of the canvas
    if number>0:
       timer2= window.after(1000,count_down,number-1)
        #After 1000 second them it will call, count_down, and pass in the arguement, number-1
    else:
        start_timer()
        if reps%2 == 0:
            global check_mark_text
            check_mark_text+=check + " "
            check_mark.config(text=check_mark_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Podomoro")
window.config(padx=100,pady=50,bg=YELLOW)

label=Label(text="Timer",font=(FONT_NAME,35),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224,bg=YELLOW)# canvas is created within the window that is in this size
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(103, 112,image=tomato_img) #middle of the canvas
timer=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="start",bg=YELLOW,highlightbackground=YELLOW,command=start_timer)
#we cannot pass in a function with an argumemnt to command
start_button.grid(column=0,row=2)


reset_button=Button(text="reset",bg=YELLOW,highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark=Label(bg=YELLOW,fg=GREEN)
check_mark.grid(column=1,row=3)

window.mainloop() # every milisecond it is checking for clicks and stuff like that