FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact Added Successfully!\n")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

            if not contacts:
                print("No contacts found.\n")
                return

            print("\nContact List:")
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"Name: {name} | Phone: {phone} | Email: {email}")

            print()

    except FileNotFoundError:
        print("No contacts file found.\n")


def search_contact():
    search_name = input("Enter name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for contact in file:
                name, phone, email = contact.strip().split(",")

                if search_name.lower() in name.lower():
                    print(f"\nFound: {name} | {phone} | {email}\n")
                    found = True

            if not found:
                print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts file found.\n")


def main():
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!\n")


if __name__ == "__main__":
    main()