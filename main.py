#basic usage of window.after() method
#   def say_something(thing):
#        print(thing)
#   window.after(10000,say_something,"swapna")


from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=None
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 
def end_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
#if we want to count down for 1 minute, then we need to keep count=1*60 as a parameter in the count_down function
#therefore, we need 25 min. hence, we need to keep count=25*60

def start_timer():
    global reps
    reps=reps+1
    work_sec = WORK_MIN * 60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break)
        timer_label.config(text="Break",fg=RED)

    elif reps%2==0:
        count_down(short_break)
        timer_label.config(text="Break",fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="work",fg=GREEN)


    # count_down(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#But we need to get the count down as 01:34
#    for example, 245/60 = 4 minutes (4.03888 )-->no.of minutes remaining
#                 245%60 =                     -->no.of seconds remaining

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("pomodora")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)



timer_label=Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

start_button=Button(text="Start",bg="white",fg="blue",command=start_timer)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset",bg="white",fg="blue",command=end_timer)
reset_button.grid(row=2,column=2)

check_label=Label(fg="GREEN",bg=YELLOW,font=("Times New Roman",20,"bold"))
check_label.grid(row=3,column=1)


#to remove the border of the canvas. we can use highlightthickness=0

canvas=Canvas(width=220,height=224,bg=YELLOW)

pomodora_image=PhotoImage(file="tomato.png")
canvas.create_image(110,112,image=pomodora_image)
canvas.grid(row=1,column=1)

timer_text=canvas.create_text(110,130,text="00:00",font=("Courier",35,"bold"),fill="white")

window.mainloop()





















