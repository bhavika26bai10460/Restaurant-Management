# Restaurant Management System

## Introduction

This is a small Python project for managing a restaurant. I made it as a console application so that the main programming concepts from the CSE1021 subject can be used directly.

The program manages the restaurant menu, customer details, food orders, tables, billing and sales summary.

## What the program can do

- Display the restaurant menu
- Add food items
- Remove food items
- Update food prices
- Take customer orders
- Display the customer's order and subtotal
- Manage restaurant tables
- Reserve and release tables
- Add and view customer details
- Generate the final bill
- Calculate GST and discount
- Select payment mode
- Display sales summary
- Show number of orders and total sales
- Find the most sold item

## Concepts used

The project uses input/output, if-else, loops, functions, lists, dictionaries, sets and simple calculations.

## How to run

Install Python 3 and open this project folder in Visual Studio Code.

Make sure all the Python files are saved in the same folder.

Open the VS Code Terminal:

```text
Terminal → New Terminal
```

Check that the terminal is opened inside your project folder.

Run:

```text
python main.py
```

The main program will display:

```text
========================================
       RESTAURANT MANAGEMENT SYSTEM
========================================
1. Show Menu
2. Add Food Item
3. Remove Food Item
4. Update Food Price
5. Take Order
6. Table Management
7. Customer Management
8. Generate Bill
9. Sales Summary
10. Exit
========================================
Enter your choice:
```

## Steps to run the project

### Step 1 - Open the project folder

Open the folder containing all the Python files in VS Code.

### Step 2 - Open Terminal

In VS Code select:

```text
Terminal → New Terminal
```

### Step 3 - Run the main program

Type:

```text
python main.py
```

and press Enter.

### Step 4 - Show Menu

Enter:

```text
1
```

This displays the available food items and their prices.

### Step 5 - Take Order

Enter:

```text
5
```

Select the item number and enter the quantity.

Enter `0` when you finish ordering.

The program displays the order and subtotal.

### Step 6 - Manage Tables

Enter:

```text
6
```

You can:

```text
1. Display Table Status
2. Reserve Table
3. Release Table
4. Back
```

### Step 7 - Manage Customers

Enter:

```text
7
```

You can:

```text
1. Add Customer
2. Show Customers
3. Back
```

### Step 8 - Generate Bill

First take an order using option `5`.

Then select:

```text
8
```

The program calculates:

- Sub Total
- GST (5%)
- Discount
- Total Amount

Then it asks for the payment mode:

```text
Cash / UPI / Card
```

### Step 9 - Sales Summary

Select:

```text
9
```

The program displays the number of orders, total sales, items sold and the most sold item.

### Step 10 - Exit

Select:

```text
10
```

The program displays:

```text
Thank you for using Restaurant Management System.
```

## Files

main.py - main program and main menu

restaurant_data.py - menu, table, order and customer data

menu_management.py - display, add, delete and price update functions

order_management.py - taking orders and displaying orders

table_management.py - table status, reservation and release functions

customer_management.py - add and display customer details

billing.py - bill calculation, GST, discount and payment mode

sales_summary.py - sales summary and most sold item
