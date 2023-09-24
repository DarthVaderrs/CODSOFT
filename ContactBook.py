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
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def find_contact_index(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                return i
        return -1

    def update_contact(self, name, new_contact):
        index = self.find_contact_index(name)
        if index != -1:
            self.contacts[index] = new_contact
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        index = self.find_contact_index(name)
        if index != -1:
            del self.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == "2":
            contact_book.display_contacts()
        elif choice == "3":
            name = input("Enter the name of the contact to update: ")
            index = contact_book.find_contact_index(name)
            if index != -1:
                name = input("Enter New Name: ")
                phone_number = input("Enter New Phone Number: ")
                email = input("Enter New Email: ")
                address = input("Enter New Address: ")
                new_contact = Contact(name, phone_number, email, address)
                contact_book.update_contact(name, new_contact)
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
