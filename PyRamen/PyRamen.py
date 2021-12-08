# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
menu_file = open(menu_filepath)
menuReader = csv.reader(menu_file)
next(menuReader)
for row in menuReader:
    menu.append(row)
menu_file.close()


# @TODO: Read in the sales data into the sales list
sales_file = open(sales_filepath)
salesReader = csv.reader(sales_file)
next(salesReader)
for row in salesReader:
    sales.append(row)

sales_file.close()





# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

for sales_item in sales:


    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    Menu_Item = sales_item[4]
    Quantity = float(sales_item[3])

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    
    if not (Menu_Item in report):
        report[Menu_Item] = {
                            "01-count": 0,
                            "02-revenue": 0,
                            "03-cogs": 0,
                            "04-profit": 0,
                        }
        



    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for menu_item in menu:

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables

        Item = menu_item[0]
        Price = float(menu_item[3])
        Cost = float(menu_item[4])
        

        # @TODO: Calculate profit of each item in the menu data
        profit = Price - Cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if (Menu_Item == Item):
            

            # @TODO: Print out matching menu data

            # print(menu_item)




            # @TODO: Cumulatively add up the metrics for each item key

            report[Menu_Item]["01-count"] += Quantity
            report[Menu_Item]["02-revenue"] += Price * Quantity
            report[Menu_Item]["03-cogs"] += Cost * Quantity
            report[Menu_Item]["04-profit"] += profit * Quantity



        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        # else:
        #     print(f"{sales_item} does not equal {Item}! NO MATCH!")


    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data

print(report)


# @TODO: Write out report to a text file (won't appear on the command line output)
