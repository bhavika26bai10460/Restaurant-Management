from restaurant_data import menu

def display_menu():
    print("\n---------- RESTAURANT MENU ----------")
    print("No.     Item                 Price")

    for no, item in menu.items():
        print(no, "   ", item[0], " " * (20 - len(item[0])), "₹", item[1])

def add_item():
    name = input("Enter food item name: ")
    price = float(input("Enter price: ₹"))
    if menu:
        no = max(menu.keys()) + 1
    else:
        no = 1
    menu[no] = [name, price]
    
    print("Food item added successfully.")

def delete_item():
    display_menu()

    try:
        no = int(input("Enter item number to remove: "))
        
        if no in menu:
            deleted_item = menu.pop(no)
            print(deleted_item[0], "deleted from menu.")
        else:
            print("Item not found.")

    except ValueError: 
        print("Please enter a valid number.")

def change_price():
    display_menu()

    try:
        no = int(input("Enter item number: "))
        
        if no in menu:
            price = float(input("Enter new price: ₹"))
            menu[no][1] = price
            print("Price changed successfully.")
        else:
            print("Item not found.")

    except ValueError:
        print("Please enter a valid number.")
while True:
    print("\n===== MENU MANAGEMENT =====")
    print("1. Display Menu")
    print("2. Add Item")
    print("3. Delete Item")
    print("4. Change Price")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu()
    elif choice == "2":
        add_item()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        change_price()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")