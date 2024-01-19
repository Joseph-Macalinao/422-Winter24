import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Grade Analysis")

root.geometry("400x300")
variable = tk.StringVar(root)
def show_graph():
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

    ax = plt.plot(dev_x, dev_y)
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.title('Median Salary (USD) by Age')
    plt.show()

depart = tk.Text(root, height=2, width=30)
depart.pack()
depart.insert(tk.END, "Please Enter Department")
depart_enter = tk.OptionMenu(root, variable, "Physics", "Biology", "Chemistry", "Earth Science", "Human Physiology")
depart_enter.pack()
#d = depart_enter.get()

crn = tk.Text(root, height=2, width=30)
crn.pack()
crn.insert(tk.END, "Please Enter CRN")
crn_enter = tk.Entry(root)
crn_enter.pack()
#crn_enter.get()


variable.set("None")
choice = tk.Text(root, height=2, width=30)
choice.pack()
choice.insert(tk.END, "A or Passing Distribution")
w = tk.OptionMenu(root, variable, "A distribution", "Pass distribution")
w.pack()

enterButton = tk.Button(root, text="Enter", command=show_graph)
enterButton.pack()
tk.mainloop()