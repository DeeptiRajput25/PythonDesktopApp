# import tkinter as tk
# root = tk.Tk()
# root.title("App	Title")
# root.geometry("400x300")
# label = tk.Label(root, text="Hello	Tkinter!")
# label.pack()
# def clickMe():
#     print("click me")
# button1 = tk.Button(root, text="Click Me", command=clickMe,width=5, height=5)
# button1.pack(pady=10)
# def sum2():
#     print("sum")
# button2=tk.Button(root, text="sum", command=sum2, width=5, height=5)
# button2.pack(pady=10)
# def devide():
#     print("devide")
# button3=tk.Button(root,text="divide",command=devide,width=5,height=5)
# button3.pack(pady=10)
# root.mainloop()
#
#
# # 2nd program
# import tkinter as tk
# root	=	tk.Tk()
# root.title("3x3	Button	Grid	- grid()")
# root.geometry("300x300")
# for	i	in	range(3):
#     for	j	in	range(3):
#         number = i*3+j+1
#         button = tk.Button(root,text=str(number),width=10,height=3)
#         button.grid(row=i,column=j,padx=5,pady=5)
# root.mainloop()
#
#
# # 2rd program using pack
# import	tkinter	as	tk
# root	=	tk.Tk()
# root.title("3x3	Button	Grid	- pack()")
# root.geometry("300x300")
# for	i	in	range(3):
#     frame=tk.Frame(root)
#     frame.pack(pady=5)
#     for j in range (3):
#         number = i*3+j+1
#         button = tk.Button(frame, text=str(number), width=10, height=3)
#         button.pack(side="left",padx=5)
# root.mainloop()
#
#
#
# import	tkinter	as	tk
#
# root = tk.Tk()
# root.title("3x5	Button	Grid - pack()")
# root.geometry("500x500")
#
# entry = tk.Entry(root)
# entry.place(x=40, y=20, width=380, height=50)
#
# for	i	in	range(5):
#
#
#
#
#
#     frame	=	tk.Frame(root)
#     frame.pack(pady=5)
#     for	j	in	range(3):
#         if i == 3 and j == 0:
#             button = tk.Button(frame, text="+", width=10, height=3)
#             button.pack(side="left", padx=5)
#         elif i == 3 and j == 1:
#             button = tk.Button(frame, text="-", width=10, height=3)
#             button.pack(side="left", padx=5)
#         elif i ==3 and j == 2:
#             button = tk.Button(frame, text="*", width=10, height=3)
#             button.pack(side="left", padx=5)
#         elif i == 4 and j == 0:
#                 button = tk.Button(frame, text="/", width=10, height=3)
#                 button.pack(side="left", padx=5)
#         elif i == 4 and j == 1:
#                 button = tk.Button(frame, text="clear", width=10, height=3)
#                 button.pack(side="left", padx=5)
#         elif i == 4 and j == 2:
#                 button = tk.Button(frame, text="=", width=10, height=3)
#                 button.pack(side="left", padx=5)
#         else:
#             number	=	i	*	3	+	j	+	1
#             button	=	tk.Button(frame, text=str(number),	width=10,	height=3)
#             button.pack(side="left",padx=5)
#
# root.mainloop()
#




import tkinter as tk

root = tk.Tk()
root.title("3x6 Button Grid - pack()")
root.geometry("500x500")

# Frame to hold the Entry at the top
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

entry = tk.Entry(top_frame, font=("Old English Text MT", 20), justify="left", width=30)
entry.pack(padx=10, pady=10, ipady=20)  # ipady increases height

def insert1():
    entry.insert(tk.END,"1")
def insert2():
    entry.insert(tk.END,string="2")
def insert3():
    entry.insert(tk.END,string="3")
def insert4():
    entry.insert(tk.END,string="4")
def insert5():
    entry.insert(tk.END,string="5")
def insert6():
    entry.insert(tk.END,string="6")
def insert7():
    entry.insert(tk.END,string="7")
def insert8():
    entry.insert(tk.END,string="8")
def insert9():
    entry.insert(tk.END,string="9")
def insertplus():
    entry.insert(tk.END, string="+")
def insertsubtract():
    entry.insert(tk.END, string="-")
def insertmultiply():
    entry.insert(tk.END, string="*")
def insertdivide():
    entry.insert(tk.END, string="/")
def insertclear():
    entry.delete(0,'end')
def insertfloor():
    entry.insert(tk.END, string="//")
def insertpercentage():
    entry.insert(tk.END, string="%")
def insertpower():
    entry.insert(tk.END, string="**")
def calculate():
    data = entry.get()
    result = eval(data)
    entry.delete(0,'end')
    entry.insert(tk.END,string = str(result))

# Frame to hold all button frames
button_frame = tk.Frame(root)
button_frame.pack()

# Create button rows
for i in range(6):
    row_frame = tk.Frame(button_frame)
    row_frame.pack(pady=5)

    for j in range(3):
        # Operator and control buttons
        if i == 3 and j == 0:
            btn_text = "+"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertplus)
            button.pack(side="left", padx=5)
        elif i == 3 and j == 1:
            btn_text = "-"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertsubtract)
            button.pack(side="left", padx=5)
        elif i == 3 and j == 2:
            btn_text = "*"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertmultiply)
            button.pack(side="left", padx=5)
        elif i == 4 and j == 0:
            btn_text = "/"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertdivide)
            button.pack(side="left", padx=5)
        elif i == 4 and j == 1:
            btn_text = "Clear"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertclear)
            button.pack(side="left", padx=5)
        elif i == 4 and j == 2:
            btn_text = "="
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=calculate)
            button.pack(side="left", padx=5)
        elif i == 5 and j == 0:
            btn_text = "//"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertfloor)
            button.pack(side="left", padx=5)
        elif i == 5 and j == 1:
            btn_text = "%"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertpercentage)
            button.pack(side="left", padx=5)
        elif i == 5 and j == 2:
            btn_text = "**"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insertpower)
            button.pack(side="left", padx=5)
        elif i == 0  and j == 0:
            btn_text = "1"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert1)
            button.pack(side="left", padx=5)
        elif i == 0  and j == 1:
            btn_text = "2"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert2)
            button.pack(side="left", padx=5)
        elif i == 0 and j == 2:
            btn_text = "3"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert3)
            button.pack(side="left", padx=5)
        elif i == 1 and j == 0:
            btn_text = "4"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert4)
            button.pack(side="left", padx=5)
        elif i == 1 and j == 1:
            btn_text = "5"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert5)
            button.pack(side="left", padx=5)
        elif i==1 and j==2:
            btn_text = "6"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert6)
            button.pack(side="left", padx=5)
        elif i==2 and j==0:
            btn_text = "7"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert7)
            button.pack(side="left", padx=5)
        elif i==2 and j==1:
            btn_text = "8"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert8)
            button.pack(side="left", padx=5)
        elif i==2 and j==2:
            btn_text = "9"
            button = tk.Button(row_frame, text=btn_text, width=10, height=3, command=insert9)
            button.pack(side="left", padx=5)

root.mainloop()
