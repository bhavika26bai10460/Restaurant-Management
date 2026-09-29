from menu_management import display_menu, add_item, delete_item, change_price
from order_management import take_order
from table_management import show_tables, reserve_table, release_table
from customer_management import add_customer, show_customers
from billing import generate_bill
from sales_summary import sales_summary

current_order = None


def main():
    global current_order

    while True: 
        print("\n")
        print("========================================")
        print("       RESTAURANT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Show Menu")
        print("2. Add Food Item")
        print("3. Remove Food Item")
        print("4. Update Food Price")
        print("5. Take Order")
        print("6. Table Management")
        print("7. Customer Management")
        print("8. Generate Bill")
        print("9. Sales Summary")
        print("10. Exit")
        print("========================================")

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
            current_order = take_order()

        elif choice == "6":
            table_menu()

        elif choice == "7":
            customer_menu()

        elif choice == "8":
            if current_order is None:
                print("Please take an order first.")
            else:
                generate_bill(current_order)

        elif choice == "9":
            sales_summary()

        elif choice == "10":
            print("\nThank you for using Restaurant Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


def table_menu():
    while True:
        print("\n---------- TABLE MANAGEMENT ----------")
        print("1. Show Tables")
        print("2. Reserve Table")
        print("3. Release Table")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tables()

        elif choice == "2":
            reserve_table()

        elif choice == "3":
            release_table()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def customer_menu():
    while True:
        print("\n---------- CUSTOMER MANAGEMENT ----------")
        print("1. Add Customer")
        print("2. Show Customers")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            show_customers()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()