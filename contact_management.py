import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact Added Successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print("No Contacts Found.\n")
        return

    print("\n----- Contact List -----")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name : {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print()


def edit_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        index = int(input("Enter Contact Number to Edit: ")) - 1

        if 0 <= index < len(contacts):
            contacts[index]["name"] = input("New Name: ")
            contacts[index]["phone"] = input("New Phone: ")
            contacts[index]["email"] = input("New Email: ")

            save_contacts(contacts)
            print("Contact Updated Successfully!\n")
        else:
            print("Invalid Contact Number.\n")

    except ValueError:
        print("Please Enter a Valid Number.\n")


def delete_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    try:
        index = int(input("Enter Contact Number to Delete: ")) - 1

        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print("Contact Deleted Successfully!\n")
        else:
            print("Invalid Contact Number.\n")

    except ValueError:
        print("Please Enter a Valid Number.\n")


def main():
    contacts = load_contacts()

    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            edit_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice. Try Again.\n")


if __name__ == "__main__":
    main()