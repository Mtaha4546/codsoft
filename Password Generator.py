import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        result_label.config(text="Length must be a positive integer.")
        return

    # Define character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password using random.choices
    password = ''.join(random.choices(all_characters, k=length))
    result_label.config(text="Generated Password: " + password)

# Create a Tkinter window
window = tk.Tk()
window.title("Password Generator")

# Create and position widgets
length_label = tk.Label(window, text="Enter the desired length of the password:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
window.mainloop()
