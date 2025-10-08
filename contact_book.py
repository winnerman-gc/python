import csv


def addContact(name, phone):
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
    print(f"Contact {name} added.")  

def deleteContact(name):
    contacts = []
    found = False
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                contacts.append(row)
            else:
                found = True
    if found:
        with open('contacts.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def viewContacts():
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        print("Contacts:")
        for row in reader:
            print(f"Name: {row[0]}, Phone: {row[1]}")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        addContact(name, phone)
    elif choice == '2':
        name = input("Enter contact name to delete: ")
        deleteContact(name)
    elif choice == '3':
        viewContacts()
    elif choice == '4':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")