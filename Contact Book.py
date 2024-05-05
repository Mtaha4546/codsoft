import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(self.root, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="e")
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, columnspan=2)

        self.contact_listbox = tk.Listbox(self.root, width=50)
        self.contact_listbox.grid(row=5, columnspan=2)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, columnspan=2)

        self.search_label = tk.Label(self.root, text="Search by Name:")
        self.search_label.grid(row=7, column=0, sticky="e")
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=7, column=1)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        self.update_contact_listbox()
        messagebox.showinfo("Success", "Contact added successfully.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name}: {contact.phone_number}")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.update_contact_listbox()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def search_contact(self):
        query = self.search_entry.get().lower()
        results = [contact for contact in self.contacts if query in contact.name.lower()]
        self.contact_listbox.delete(0, tk.END)
        for contact in results:
            self.contact_listbox.insert(tk.END, f"{contact.name}: {contact.phone_number}")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
