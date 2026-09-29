def generate_bill(order):
    if not order or len(order) == 0:
        print("No order available.")
        return 0

    sub_total = 0

    print("\n===================================")
    print("            FINAL BILL")
    print("===================================")

    for i in order:
        name = i[0]
        quantity = i[1]
        price = i[2]

        amount = quantity * price
        sub_total += amount

        print(name, "x", quantity, "=", "₹", amount)

    gst = 0.05 * sub_total

    if sub_total >= 1000:
        discount = 0.10 * sub_total
    else:
        discount = 0

    total = sub_total + gst - discount

    print("-----------------------------------")
    print("Sub Total      : ₹", round(sub_total, 2))
    print("GST (5%)       : ₹", round(gst, 2))
    print("Discount       : ₹", round(discount, 2))
    print("-----------------------------------")
    print("Total Amount   : ₹", round(total, 2))
    print("-----------------------------------")

    payment = input("Choose payment mode (Cash / UPI / Card): ")

    print("Payment Mode   :", payment)
    print("Payment success.")
    print("Thanks for visiting.")

    return total
