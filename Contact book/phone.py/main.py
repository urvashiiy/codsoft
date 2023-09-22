class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        """Add a contact to the contact book."""
        contact = Contact(name, phone, email, address)
        self.contacts[name] = contact
        print(f"Contact {name} added successfully!")

    def delete_contact(self, name):
        """Delete a contact from the contact book."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found!")

    def view_contact(self, name):
        """View contact information for a given name."""
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
        else:
            print(f"Contact {name} not found!")

    def search_contact(self, name):
        """Search for a contact by name."""
        self.view_contact(name)

    def update_contact(self, name, phone, email):
        """Update contact information."""
        if name in self.contacts:
            contact = self.contacts[name]
            contact.phone = phone
            contact.email = email
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found!")

    def list_contacts(self):
        """List all contacts in the contact book."""
        for name in self.contacts:
            print(name)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add a Contact")
        print("2. Delete a Contact")
        print("3. View a Contact")
        print("4. Search for a Contact")
        print("5. Update a Contact")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email : ")
            address = input("Enter the contact's address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '3':
            name = input("Enter the name of the contact to view: ")
            contact_book.view_contact(name)
        elif choice == '4':
            name = input("Enter the name to search for: ")
            contact_book.search_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            contact_book.update_contact(name, phone, email)
        elif choice == '6':
            contact_book.list_contacts()
        elif choice == '7':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
