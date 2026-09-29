from restaurant_data import customers


def add_customer():
    print("\n---------- CUSTOMER DETAILS ----------")

    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")

    customer = {
        "name": name,
        "phone": phone
    }

    customers.append(customer)

    print("Customer details added successfully.")


def show_customers():
    if len(customers) == 0:
        print("\nNo customer details available.")
        return

    print("\n---------- CUSTOMER LIST ----------")

    for i, customer in enumerate(customers, start=1):
        print("\nCustomer", i)
        print("Name :", customer["name"])
        print("Phone:", customer["phone"])
print("\n===== CUSTOMER MANAGEMENT =====")
print("1. Add Customer")
print("2. Show Customers")
print("3. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    add_customer()

elif choice == "2":
    show_customers()

elif choice == "3":
    print("Exiting...")

else:
    print("Invalid choice.")