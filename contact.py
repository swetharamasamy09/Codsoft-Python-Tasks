contacts = []
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print(f"\nContact {name} added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['Name']} | {contact['Phone']}")
    else:
        print("\nNo contacts available.")

def search_contact():
    search = input("Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if search.lower() in contact['Name'].lower() or search in contact['Phone']:
            print(f"\nFound Contact: {contact}")
            found = True
    if not found:
        print("No contact found with that name or phone number.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contact['Phone'] = input("Enter new phone number: ")
            contact['Email'] = input("Enter new email: ")
            contact['Address'] = input("Enter new address: ")
            print(f"\nContact {name} updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"\nContact {name} deleted successfully!")
            return
    print("Contact not found.")


while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Management System...")
        break
    else:
        print("Invalid choice! Try again.")
