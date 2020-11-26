from tkinter import * 

def bcomm():
  score = 0
  if score == 0:
    l0 = Label(master, text="Pressed", bg="white", fg="black")
    l0.grid(column=0, row=1)
  score += 1
  print(score)

def shapez():
  o = w.create_oval(250,250, 150, 200, fill="gray")


master =Tk()
master.minsize(height=200, width=300)

w = Canvas(master, width=450, height=400)  
w.grid(column=2, row=2)
o = w.create_oval(250, 250, 150, 200, fill="green")


b = Button(master, text="START", command=bcomm)
b.grid(column=0, row=0)
b.configure(bg="black")
b.configure(fg="white")
b.configure(pady=30)
b.configure(relief="groove")

master.mainloop()