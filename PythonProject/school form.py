import tkinter as tk

root = tk.Tk()

root.title("School Form")
root.geometry("500x500")
root.config(padx=20,pady=20)

nameLabel = tk.Label(root,text="Student Name")
nameLabel.grid(row=0,column=0,sticky="w")

nameEntry = tk.Entry(root,width=30)
nameEntry.grid(row=1,column=0,pady=(10,10))

nameLabel = tk.Label(root,text="Father's  Name")
nameLabel.grid(row=2,column=0,sticky="w")

nameEntry = tk.Entry(root,width=30)
nameEntry.grid(row=3,column=0,pady=(10,10))

emailLabel = tk.Label(root,text="Email")
emailLabel.grid(row=4,column=0,sticky="w")

emailEntry = tk.Entry(root,width=30)
emailEntry.grid(row=5,column=0,pady=(10,10))

phoneNoEntry = tk.Label(root,text="Phone no")
phoneNoEntry.grid(row=6,column=0,sticky="w")

phoneNoEntry = tk.Entry(root,width=30)
phoneNoEntry.grid(row=7,column=0,pady=(10,10))

dateOfBirthEntry = tk.Label(root,text="Date of Birth")
dateOfBirthEntry.grid(row=8,column=0,sticky="w")

dateOfBirthEntry = tk.Entry(root,width=30)
dateOfBirthEntry.grid(row=9,column=0,pady=(10,10))

genderVar = tk.StringVar()
genderVar.set("Male")

nameLabel = tk.Label(root,text="Gender")
nameLabel.grid(row=10,column=0,sticky="w")

maleRadio = tk.Radiobutton(root, text="Male", variable=genderVar, value="Male")
maleRadio.grid(row=11, column=0, padx=10, pady=5,sticky="w")

femaleRadio = tk.Radiobutton(root, text="Female", variable=genderVar, value="Female")
femaleRadio.grid(row=12, column=0, padx=10, pady=5,sticky="w")

termsVar = tk.BooleanVar()
termsCheck = tk.Checkbutton(root, text="I accept the Terms and Conditions", variable=termsVar)
termsCheck.grid(row=13, column=0, padx=10, pady=(10, 0), sticky="w")


root.mainloop()