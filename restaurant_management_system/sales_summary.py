from restaurant_data import orders


def sales_summary():
    if not orders:
        print("\nNo orders have been placed yet.")
        return

    number_of_orders = len(orders)
    number_of_sales = 0
    items = {}

    for order in orders:
        total_order = 0

        for item in order:
            name = item[0]
            quantity = item[1]
            cost = item[2]

            total_order += quantity * cost

            if name in items:
                items[name] += quantity
            else:
                items[name] = quantity

        number_of_sales += total_order

    print("\n---------- SALES SUMMARY ----------")
    print("Number of Orders:", number_of_orders)
    print("Total Sales     : ₹", number_of_sales)

    print("\nItems Sold:")

    for item, quantity in items.items():
        print(item, ":", quantity)

    item_sold_mostly = max(items, key=items.get)

    print("\nMost Sold Item:", item_sold_mostly)
    print("Quantity sold  :", items[item_sold_mostly])

sales_summary()