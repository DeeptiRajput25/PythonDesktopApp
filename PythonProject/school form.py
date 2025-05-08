import tkinter as tk
import requests
from tkinter import messagebox
import json

def submit_form():
    # Get form data
    name = nameEntry.get()
    fatherName = fatherEntry.get()
    email = emailEntry.get()
    phoneNo = phoneNoEntry.get()
    dateOfBirth = dateOfBirthEntry.get()
    className= classEntry.get()
    gender = genderVar.get()

    # Prepare data for API
    form_data = {
        "name": name,
        "fatherName": fatherName,
        "email": email,
        "phoneNo": phoneNo,
        "dateOfBirth": dateOfBirth,
        "class": className,
        "gender": gender
    }
    print("Sending data:", form_data)


    url = "https://script.google.com/macros/s/AKfycbzE3K9EPCkc994RWB34grSMHWnISlfwRzmMY4ZKJGBfboJU_OaRvzbW3eJVuA3TAZl5Pw/exec"

    try:
        print("Sending data:", form_data)  # Debug print
        response = requests.post(url, json=form_data)
        print("Response status code:", response.status_code)  # Debug print
        print("Response content:", response.text)  # Debug print

        if response.status_code == 200:
            messagebox.showinfo("Success", "Form submitted successfully!")
            # Clear form
            nameEntry.delete(0, tk.END)
            emailEntry.delete(0, tk.END)
            gender_var.set("Male")
        else:
            messagebox.showerror("Error",f"Failed to submit form. Status code: {response.status_code}\nResponse: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print("Full error details:", e)  # Debug print


root = tk.Tk()

root.title("School Form")
root.geometry("500x800")
root.config(padx=20,pady=20)

nameLabel = tk.Label(root,text="Student Name")
nameLabel.grid(row=0,column=0,sticky="w")

nameEntry = tk.Entry(root,width=30)
nameEntry.grid(row=1,column=0,pady=(10,10))

fatherLabel = tk.Label(root,text="Father's  Name")
fatherLabel.grid(row=2,column=0,sticky="w")

fatherEntry = tk.Entry(root,width=30)
fatherEntry.grid(row=3,column=0,pady=(10,10))

emailLabel = tk.Label(root,text="Email")
emailLabel.grid(row=4,column=0,sticky="w")

emailEntry = tk.Entry(root,width=30)
emailEntry.grid(row=5,column=0,pady=(10,10))

phoneNumberLabel = tk.Label(root,text="Phone number")
phoneNumberLabel.grid(row=6,column=0,sticky="w")

phoneNoEntry = tk.Entry(root,width=30)
phoneNoEntry.grid(row=7,column=0,pady=(10,10))

dateOfBirthLabel = tk.Label(root,text="Date of Birth")
dateOfBirthLabel.grid(row=8,column=0,sticky="w")

dateOfBirthEntry = tk.Entry(root,width=30)
dateOfBirthEntry.grid(row=9,column=0,pady=(10,10))

classLabel = tk.Label(root,text="Class")
classLabel.grid(row=10,column=0,sticky="w")

classEntry = tk.Entry(root,width=30)
classEntry.grid(row=11,column=0,pady=(10,10))

addressLabel = tk.Label(root,text="Address")
addressLabel.grid(row=12,column=0,sticky="w")

addressEntry = tk.Entry(root,width=30)
addressEntry.grid(row=13,column=0,pady=(10,10))

streamLabel = tk.Label(root,text="Stream")
streamLabel.grid(row=14,column=0,sticky="w")

termsVar1 = tk.BooleanVar()
termsCheck = tk.Checkbutton(root, text="Math", variable=termsVar1)
termsCheck.grid(row=15, column=0, padx=10, pady=(10, 0), sticky="w")

termsVar2 = tk.BooleanVar()
termsCheck = tk.Checkbutton(root, text="Science", variable=termsVar2)
termsCheck.grid(row=16, column=0, padx=10, pady=(10, 0), sticky="w")

termsVar3 = tk.BooleanVar()
termsCheck = tk.Checkbutton(root, text="Art", variable=termsVar3)
termsCheck.grid(row=17, column=0, padx=10, pady=(10, 0), sticky="w")


genderVar = tk.StringVar() # this is requied for two way binding
genderVar.set("Male")

genderLabel = tk.Label(root,text="Gender")
genderLabel.grid(row=18,column=0,sticky="w")

maleRadio = tk.Radiobutton(root, text="Male", variable=genderVar, value="Male")
maleRadio.grid(row=19, column=0, padx=10, pady=5,sticky="w")

femaleRadio = tk.Radiobutton(root, text="Female", variable=genderVar, value="Female")
femaleRadio.grid(row=20, column=0, padx=10, pady=5,sticky="w")

termsVar = tk.BooleanVar()
termsCheck = tk.Checkbutton(root, text="I accept the Terms and Conditions", variable=termsVar)
termsCheck.grid(row=21, column=0, padx=10, pady=(10, 0), sticky="w")

summitButton= tk.Button(root,text="submit",command=submit_form)
summitButton.grid(row=22,column=0,padx=10,pady=(10,0))

root.mainloop()