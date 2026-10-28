from tkinter import *

root = Tk()
root.title("Loghin App")
root.geometry("500x400")

frame = Frame(master=root, height=200, width=360,bg="lightgrey", relief=RAISED, borderwidth=1)
lbl1 = Label(master=frame, text="full name", bg="darkgrey", fg="black", font=("Arial", 20))
lbl2 = Label(master=frame, text="email", bg="darkgrey", fg="black", font=("Arial", 20))
lbl3 = Label(master=frame, text="password", bg="darkgrey", fg="black", font=("Arial", 20))


name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

def display_info():
    name = name_entry.get()
    greet = f"Hello, {name}!"
    msg = "congratulations! You have successfully created a account."
    textbox.insert(END, greet + "\n" + msg)
    
textbox = Text(bg="white", fg="black")
btn = Button( text="create account", command=display_info, bg="red", fg="white")


frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=70)
email_entry.place(x=150, y=70)
lbl3.place(x=20, y=120)
password_entry.place(x=150, y=120)
btn.place(x=130, y=210)
textbox.place(y=250)
 
root.mainloop()
