import tkinter as tk

root = tk.Tk()
root.title("Grade Analysis")

root.geometry("400x300")
g = tk.PhotoImage(file = "Your_img.png")

year = tk.Text(root, height=2, width=30)
year.pack()
year.insert(tk.END, "Please Enter Year")
year_enter = tk.Entry(root)
year_enter.pack()
y = year_enter.get()

depart = tk.Text(root, height=2, width=30)
depart.pack()
depart.insert(tk.END, "Please Enter Department")
depart_enter = tk.Entry(root)
depart_enter.pack()
d = depart_enter.get()

crn = tk.Text(root, height=2, width=30)
crn.pack()
crn.insert(tk.END, "Please Enter CRN")
crn_enter = tk.Entry(root)
crn_enter.pack()
crn_enter.get()

variable = tk.StringVar(root)
variable.set("None")

w = tk.OptionMenu(root, variable, "A distribution", "Pass distribution")
w.pack()

enterButton = tk.Button(root, text="Enter")
enterButton.pack()
tk.mainloop()