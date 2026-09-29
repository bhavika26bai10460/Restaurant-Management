from restaurant_data import menu, orders
from menu_management import show_menu


def take_order():
    show_menu()

    order = []

    while True:
        try:
            item_number = int(input("\nEnter item number (0 to exit): "))

            if item_number == 0:
                break

            if item_number not in menu:
                print("Item does not exist.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity should be greater than zero.")
                continue

            item_name = menu[item_number][0]
            price = menu[item_number][1]

            order.append([item_name, quantity, price])

            print(item_name, "added to your order.")

        except ValueError:
            print("Please enter a valid number.")

    if len(order) == 0:
        print("Nothing to order.")
        return None

    orders.append(order)

    print("\nOrder successful.")
    show_order(order)

    return order


def show_order(order):
    print("\n----------- YOUR ORDER -----------")

    total = 0

    for item in order:
        name = item[0]
        quantity = item[1]
        price = item[2]

        amount = quantity * price
        total += amount

        print(name, "x", quantity, "=", "₹", amount)

    print("----------------------------------")
    print("Subtotal:", "₹", total)

    return total