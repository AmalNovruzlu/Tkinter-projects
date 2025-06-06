import tkinter as tk 

a=0

window=tk. Tk()
window.title("score")
window.configure(background="lightgrey")

def button_work (number):
    global a
    if number=='up':
        a+=1
    else:
        if a>0:
            a-=1 
    label1.config(text=a)

button_down=tk.Button(window,text= 'down',bg="grey",command= lambda: button_work("down"),padx=10, pady=20)
button_up=tk.Button(window,text= 'up',command= lambda: button_work("up"),padx=10, pady=20)


label1= tk.Label(window, text="Scores", font=( "Arial", 14))
label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


button_down.grid(row=3, column=0) 
button_up.grid(row=3, column=2) 

window.mainloop()