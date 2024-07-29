import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    age = entry_age.get()
    gender = gender_var.get()

    if first_name and last_name and email and password and age and gender:
        messagebox.showinfo("Registration Success", f"Registration Successful!\nName: {first_name} {last_name}\nEmail: {email}\nAge: {age}\nGender: {gender}")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Create the main application window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")

# Create labels and entry fields for the form
label_first_name = tk.Label(root, text="First Name:")
label_first_name.pack(pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.pack(pady=5)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.pack(pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

label_age = tk.Label(root, text="Age:")
label_age.pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

label_gender = tk.Label(root, text="Gender:")
label_gender.pack(pady=5)

gender_var = tk.StringVar(value="Select Gender")

radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_male.pack(pady=5)

radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_female.pack(pady=5)

radio_other = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")
radio_other.pack(pady=5)

# Create a submit button
button_submit = tk.Button(root, text="Submit", command=submit_form)
button_submit.pack(pady=20)

# Run the application
root.mainloop()