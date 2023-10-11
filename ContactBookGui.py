import tkinter as tk
import json

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        return self.contacts

    def find_contact_index(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                return i
        return -1

    def update_contact(self, name, new_contact):
        index = self.find_contact_index(name)
        if index != -1:
            self.contacts[index] = new_contact
            return "Contact updated successfully."
        else:
            return "Contact not found."

    def delete_contact(self, name):
        index = self.find_contact_index(name)
        if index != -1:
            del self.contacts[index]
            return "Contact deleted successfully."
        else:
            return "Contact not found."

##To save and load contacts even after app termination
    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def load_contacts(self, filename):
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(**data) for data in contacts_data]
        except FileNotFoundError:
            self.contacts = []



class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contact_book = ContactBook()

        #input file to load

        self.contact_file = "contacts.json"
        self.contact_book.load_contacts(self.contact_file)
       
        #input file loaded

        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone Number")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email")
        self.email_label.pack()

        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address")
        self.address_label.pack()

        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.display_button = tk.Button(root, text="Display Contacts", command=self.display_contacts)
        self.display_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = Contact(name, phone_number, email, address)
        self.contact_book.add_contact(contact)
        self.result_label.config(text="Contact added successfully.")
        self.clear_entries()

    def display_contacts(self):
        contacts = self.contact_book.display_contacts()
        if not contacts:
            self.result_label.config(text="No contacts found.")
        else:
            contact_info = "\n".join([f"Name: {contact.name}, Phone: {contact.phone_number}" for contact in contacts])
            self.result_label.config(text=contact_info)

    def update_contact(self):
        name = self.name_entry.get()
        index = self.contact_book.find_contact_index(name)
        if index != -1:
            new_name = self.name_entry.get()
            new_phone = self.phone_entry.get()
            new_email = self.email_entry.get()
            new_address = self.address_entry.get()
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            result = self.contact_book.update_contact(name, new_contact)
            self.result_label.config(text=result)
            self.clear_entries()
        else:
            self.result_label.config(text="Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        result = self.contact_book.delete_contact(name)
        self.result_label.config(text=result)
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def on_closing(self):
        # Save contacts when the application is closed
        self.contact_book.save_contacts(self.contact_file)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)

    #Callback to save contact when window closes
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
