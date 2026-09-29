from restaurant_data import tables


def display_table_status():
    print("\n---------- TABLE STATUS ----------")

    for table, status in tables.items():
        print("Table", table, ":", status)


def reserve_table():
    display_table_status()

    try:
        table_number = int(input("\nEnter table number: "))

        if table_number not in tables:
            print("Invalid table number.")
        elif tables[table_number] == "Occupied":
            print("This table is already occupied.")
        else:
            tables[table_number] = "Occupied"
            print("Table", table_number, "has been reserved.")

    except ValueError:
        print("Please enter a valid table number.")


def release_table():
    display_table_status()

    try:
        table_number = int(input("\nEnter table number to release: "))

        if table_number not in tables:
            print("Invalid table number.")
        elif tables[table_number] == "Available":
            print("This table is already available.")
        else:
            tables[table_number] = "Available"
            print("Table", table_number, "is now available.")

    except ValueError:
        print("Please enter a valid table number.")
while True:
    print("\n===== TABLE MANAGEMENT =====")
    print("1. Display Table Status")
    print("2. Reserve Table")
    print("3. Release Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_table_status()

    elif choice == "2":
        reserve_table()

    elif choice == "3":
        release_table()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")        