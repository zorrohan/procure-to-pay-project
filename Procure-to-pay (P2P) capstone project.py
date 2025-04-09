from tabulate import tabulate
import random
import string
import sys

orders = {
    "PO60384":{
        "Supplier": "Unilever", 
        "Items": ["Rinso, Royco, Dove"], 
        "Vendor Invoice": "UNV14578",
        "Good Receive Number": "GO14578",
        "All Goods Received?": "yes", 
        "Payment Status": "This PO can be paid"
        }, 
        "PO76081": {
            "Supplier": "Wings", 
            "Items": ["So Klin, Mie Sedap, Jasjus"], 
            "Vendor Invoice": "WGS14578",
            "Good Receive Number": "GO14579",
            "All Goods Received?": "yes", 
            "Payment Status": "This PO can be paid"
        },
        "PO78228": {
            "Supplier": "Mayora",
            "Items": ["Kopiko, Energen, Kis"],
            "Vendor Invoice": "MAY14578",
            "Good Receive Number": "GO14580",
            "All Goods Received?": "no",
            "Payment Status": "This PO cannot be paid"
        }
}

def generate_po_number():
    """Generates a random 6-digit purchase order number starting with 'PO'"""
    digits = ''.join(random.choices(string.digits, k=5))
    return f"PO{digits}"

def add_new_purchase_order():
    """Adds a new purchase order with auto-generated ID."""
    supplier = input("\nEnter supplier name: ")
    items = input("Enter items (comma-separated): ").split(',')

    while True:
        po_number = generate_po_number()
        if po_number not in orders:  # Ensure PO number is unique
            break
    
    orders[po_number] = {"Supplier": supplier, "Items": items}
    print(f"\n✅ Purchase order number {po_number} has been added successfully!\n")
    return orders

def view_all_purchase_order():
    """Displays all purchase orders in orders(the data storage)."""
    if not orders:
        print("\nNo purchase orders available.\n")
        return
    else:
        table_data = [[po, details["Supplier"], ', '.join(details["Items"])] for po, details in orders.items()]
        headers = ["PO Number", "Supplier", "Items"]
        print("\n" + tabulate(tabular_data=table_data, headers=headers, tablefmt="grid") + "\n")

def view_specific_purchase_order():
    """Displays details of a specific purchase order by PO number."""
    po_number = input("Enter the PO number: ")
    if po_number in orders:
        details = orders[po_number]
        print(f"\nPO Number: {po_number}\nSupplier: {details['Supplier']}\nItems: {', '.join(details['Items'])}\n")
    else:
        print(f"\n❌ Purchase order number {po_number} is not found.\n")

def update_purchase_order():
    """Adds or removes items from an existing purchase order."""
    po_number = input("\nEnter the PO number to update: ")
    if po_number in orders:
        action = input("Do you want to add or remove an item? (add/remove): ").strip().lower()
        if action == "add":
            new_item = input("Enter the item to add: ")
            orders[po_number]["items"].append(new_item)
            print(f"\n✅ {new_item} as a new item has been added to purchase number {po_number} successfully!\n")
        elif action == "remove":
            remove_item = input("Enter the item to remove: ")
            if remove_item in orders[po_number]["Items"]:
                orders[po_number]["Items"].remove(remove_item)
                print(f"\n✅ {remove_item} has been removed from purchase number {po_number} successfully!\n")
            else:
                print(f"\n❌ {remove_item} item is not found in the order.\n")
        else:
            print(f"\n❌ {action} is Invalid action. only type add or remove\n")
    else:
        print(f"\n❌ Purchase order number {po_number} is not found.\n")

def delete_purchase_order():
    """Deletes the purchase order by PO number."""
    po_number = input("\nEnter the PO number to delete: ")
    if po_number in orders:
        del orders[po_number]
        print(f"\n✅ Purchase order number {po_number} has been deleted successfully!\n")
    else:
        print(f"\n❌ Purchase order number {po_number} is not found.\n")

def add_vendor_invoice():
    """Adds vendor invoice number to spesific purchase order number"""
    po_number = input("\nInsert Purchase Order Number: ")
    if po_number not in orders:
        print("\n❌ Purchase order not found.\n")
        return
    else:
        vi_number = input("Insert Vendor Invoice Number: ")
        orders[po_number].update({"Vendor Invoice": vi_number})
        print(f"\n✅ Vendor invoice number {vi_number} for purchase order number {po_number} has been added successfully!\n")

def view_vendor_invoice():
    """Displays all purchase orders with vendor invoice."""
    if not orders:
        print("\nNo purchase orders available.\n")
        return
    
    table_data = []
    for po, details in orders.items():
        supplier = details.get('Supplier', "N/A")
        items = ','.join(details.get("Items", []))
        vendor_invoice = details.get("Vendor Invoice", "Not Assigned")
        
        table_data.append([po, supplier, items, vendor_invoice])

    headers = ["PO Number", "Supplier", "Items", "Vendor Invoice"]
    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid") +"\n") 

def view_specific_vendor_invoice():
    """Displays details of a specific vendor invoice by invoice number."""
    vi_number = input("Enter the Vendor Invoice number: ")

    # Search for the vendor invoice in the orders dictionary
    for po_number, details in orders.items():
        if details.get("Vendor Invoice") == vi_number:
            print(f"\nVendor Invoice: {vi_number}\nPO Number: {po_number}\nSupplier: {details['Supplier']}\nItems: {', '.join(details['Items'])}\n")
            return
    
    print(f"\n❌ Vendor Invoice number {vi_number} is not found.\n")

def update_vendor_invoice():
    """Updates vendor invoice number to spesific purchase order"""
    po_number = input("\nEnter the PO number to modify vendor invoice: ")
    if po_number not in orders:
         print("\n❌ Purchase order not found.\n")
         return
    else:
        print(f"\nCurrent Vendor Invoice for {po_number}: {orders[po_number]['Vendor Invoice']}")

    new_invoice = input("Enter the new Vendor Invoice Number: ")
    orders[po_number]["Vendor Invoice"] = new_invoice
    print(f"\n✅ Vendor invoice with new number {new_invoice} for purchase order number {po_number} updated successfully!\n")

def delete_vendor_invoice():
    '''Deletes the vendor invoice number by PO number'''
    po_number = input("\nEnter the PO number to delete existing vendor invoice number: ")
    if po_number in orders:
         del orders[po_number]["Vendor Invoice"]
         print(f"\n✅ Vendor Invoice number for purchase order number {po_number} has been deleted")
    else:
        print(f"\n❌ Purchase order number {po_number} is not found.\n")
    
def generate_gr_number():
    """Generates a random 6-digit good receive number starting with 'GR'"""
    digits = ''.join(random.choices(string.digits, k=5))
    return f"GO{digits}"

def add_good_receive():
    '''Adds good receive data (good receive number, completeness of goods, and payment status)'''
    po_number = input("Insert PO Number: ")
    if po_number not in orders:
        print("\n❌ Purchase order not found.\n")
        return

    while True:
        gr_number = generate_gr_number()
        if gr_number not in orders:  # Ensure GR number is unique
            break

    while True:
        completeness_of_goods = input(f"\nFor Purchase number {po_number}, Have all goods been received? (yes/no): ").strip().lower()
        if completeness_of_goods in ["yes", "no"]:
            break
        else:
            print("\nYour input is not correct ❌, only choose yes or no\n")

    payment_status = "This PO can be paid" if completeness_of_goods == "yes" else "This PO cannot be paid"
            
    # Store the data in the orders dictionary
    orders[po_number].update ({
        "Good Receive Number": gr_number,
        "All Goods Received?": completeness_of_goods,
        "Payment Status": payment_status
    })

    print(f"\n✅ Good Receive number {gr_number} for Purchase Order number {po_number} has been added successfully!")
    return orders

def view_good_receive():
    '''Displays all purchase orders with good receive number.'''
    if not orders:
        print("\nNo purchase orders available.\n")
        return
    
    table_data = []
    for po, details in orders.items():
        supplier = details.get('Supplier', "N/A")
        items = ','.join(details.get("Items", []))
        vendor_invoice = details.get("Vendor Invoice", "Not Assigned")
        gr_number = details.get("Good Receive Number", "N/A")
        completeness_of_goods = details.get("All Goods Received?", "N/A")
        payment_status = details.get("Payment Status", "N/A")
        
        table_data.append([po, supplier, items, vendor_invoice, gr_number, completeness_of_goods, payment_status])

    headers = ["PO Number", "Supplier", "Items", "Vendor Invoice", "Good Receive Number", "All Goods Received?", "Payment Status"]
    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid") +"\n")

def view_specific_good_receive():
    '''Displays details of a specific good receive data by good receive number.'''
    gr_number = input("Enter the Good Receive number: ")

    # Search for the good receive in the orders dictionary
    for po_number, details in orders.items():
        if details.get("Good Receive Number") == gr_number:
            print(f"\nGood Receive Number: {gr_number}\nVendor Invoice: {details['Vendor Invoice']}\nPO Number: {po_number}\nSupplier: {details['Supplier']}\nItems: {', '.join(details['Items'])}\nAll Goods Received?: {details['All Goods Received?']}\nPayment Status: {details['Payment Status']}\n")
            return
    else:
        print(f"\n❌ Good Receive number {gr_number} is not found.\n")

def update_good_receive():
    '''Updates good receive data to spesific purchase order number'''
    po_number = input("\nEnter the PO number to modify Good Receive data: ")
    if po_number not in orders:
         print("\n❌ Purchase order not found.\n")
         return
    else:
        print(f"\nCurrent Good Receive Number for {po_number} is: {orders[po_number].get('Good Receive Number', 'N/A')}\n")
    
    try:
        good_receive_update = int(input("What do you want to be updated? (1. Good Receive Number 2. All Good Received?) "))
    except ValueError:
        print("\n❌ Invalid input! Please enter 1 or 2.\n")
        return
    
    if good_receive_update == 1:
        new_gr_number = generate_gr_number()
        orders[po_number]["Good Receive Number"] = new_gr_number
        print(f"\n✅ Good Receive with new number {new_gr_number} for purchase order number {po_number} has been updated successfully!\n")

    if good_receive_update == 2:
        while True:
            new_completeness_of_goods = input("Have all goods been received? (yes/no): ").strip().lower()
            if new_completeness_of_goods in ["yes", "no"]:
                break
            print("\n❌ Invalid input! Only enter 'yes' or 'no'.\n")

        payment_status = "This PO can be paid" if new_completeness_of_goods == "yes" else "This PO cannot be paid"

        orders[po_number]["All Goods Received?"] = new_completeness_of_goods
        orders[po_number]["Payment Status"] = payment_status

        print(f"\n✅ Good Receive data updated successfully for Purchase Order {po_number}.\n")

def delete_good_receive():
    '''Delete good receive data to spesific purchase order number'''
    po_number = input("\nEnter the PO number to delete existing good receive number: ")
    if po_number in orders:
         del orders[po_number]["Good Receive Number"]
         del orders [po_number]["All Goods Received?"]
         del orders [po_number]["Payment Status"]
         print(f"\n✅ Good Receive data for purchase order number {po_number} has been deleted")
    else:
        print(f"\n❌ Purchase order number {po_number} is not found.\n")

while True:
    print('Welcome to main menu of procure-to-pay system, Choose menus below:\n1. Purchase Order\n2. Vendor Invoice\n3. Good Receive\n4. Exit Program''')
    try:
        main_menu_input = int(input('Choose the number on the menu: '))
    except ValueError:
        print("Your input is INVALID ❌. Only choose number provided on the menu\n")
        continue
    
    if main_menu_input == 1:
        while True:
            print('\nYou are in Purchase Order Menu, Choose menus below:\n1. Add New Purchase Order\n2. View All Purchase Order Data\n3. View Spesific Purchase Order Data\n4. Update Purchase Order Item\n5. Delete Purchase Order\n6. Back to Main Menu\n7. Exit Program')
            try:
                purchase_order_menu_input = int(input('Choose the number on the menu: '))
            except ValueError:
                print("\nYour input is INVALID ❌, only choose number provide on the menus\n")
                continue
            if purchase_order_menu_input == 1:
                add_new_purchase_order()
            elif purchase_order_menu_input == 2:
                view_all_purchase_order()
            elif purchase_order_menu_input == 3:
                view_specific_purchase_order()
            elif purchase_order_menu_input == 4:
                update_purchase_order()
            elif purchase_order_menu_input == 5:
                delete_purchase_order()
            elif purchase_order_menu_input == 6:
                purchase_order_back_to_main_menu = input('\nAre you sure you want to back to Main Menu? (y/n): ').strip().lower()
                if purchase_order_back_to_main_menu == "y":
                    print('Returning to the Main Menu...\n')
                    break
                elif purchase_order_back_to_main_menu == "n":
                    print('Returning to the Purchase Order Menu...\n')
                    continue
            elif purchase_order_menu_input == 7:
                exit_program = input('\nAre you sure you want to exit from program? (y/n): ').strip().lower()
                if exit_program == "y":
                    print('Thank you for using this program, Goodbye! 👋')
                    sys.exit()
                elif exit_program == "n":
                    print('Returning to The Purchase Order Menu...\n')
                    continue
            else:
                print(f'There is no option number {purchase_order_menu_input} on the Purchase Order menus, Choose the number only on the menu!\n ')
        continue
    
    elif main_menu_input == 2:
        while True:
            print('\nYou are in Vendor Invoice Menu, Choose menus below:\n1. Add Vendor Invoice \n2. View Vendor Invoice \n3. View Specific Vendor Invoice \n4. Update Vendor Invoice \n5. Delete Vendor Invoice \n6. Back to Main Menu \n7. Exit Program')
            try:
                vendor_invoice_menu_input = int(input('Choose the number on the menu: '))
            except ValueError:
                print("\nYour input is INVALID ❌, only choose number provide on the menus\n")
                continue
            if vendor_invoice_menu_input == 1:
                add_vendor_invoice()
            elif vendor_invoice_menu_input == 2:
                view_vendor_invoice()
            elif vendor_invoice_menu_input == 3:
                view_specific_vendor_invoice()
            elif vendor_invoice_menu_input == 4:
                update_vendor_invoice()
            elif vendor_invoice_menu_input == 5:
                delete_vendor_invoice()
            elif vendor_invoice_menu_input == 6:
                vendor_invoice_back_to_main_menu = input('\nAre you sure you want to back to Main Menu? (y/n): ').strip().lower()
                if vendor_invoice_back_to_main_menu == "y":
                    print('Returning to the Main Menu...\n')
                    break
                elif vendor_invoice_back_to_main_menu == "n":
                    print('Returning to the Vendor Invoice Menu...\n')
                    continue
            elif vendor_invoice_menu_input == 7:
                exit_program = input('\nAre you sure you want to exit from program? (y/n): ').strip().lower()
                if exit_program == "y":
                    print('Thank you for using this program, Goodbye! 👋')
                    sys.exit()
                elif exit_program == "n":
                    print('Returning to The Vendor Invoice Menu...\n')
                    continue                
            else:
                print(f'There is no option number {vendor_invoice_menu_input} on the Vendor Invoice menu, Choose the number only on the menu!\n')
        continue
    
    elif main_menu_input == 3:
        while True:
            print('\nYou are in Good Receive Menu, Choose menus below:\n1. Add Good Receive Data\n2. View Good Receive Data\n3. View Specific Good Receive\n4. Update Good Receive Data \n5. Delete Good Receive Data \n6. Back to Main Menu \n7. Exit Program')
            try:
                good_receive_menu_input = int(input('Choose the number on the menu: '))
            except:
                print("\nYour input is INVALID ❌, only choose number provide on the menus\n")
                continue

            if good_receive_menu_input == 1:
                add_good_receive()
            elif good_receive_menu_input == 2:
                view_good_receive()
            elif good_receive_menu_input == 3:
                view_specific_good_receive()
            elif good_receive_menu_input == 4:
                update_good_receive()
            elif good_receive_menu_input == 5:
                delete_good_receive()
            elif good_receive_menu_input == 6:
                good_receive_back_to_main_menu = input('\nAre you sure you want to back to Main Menu? (y/n): ').strip().lower()
                if good_receive_back_to_main_menu == "y":
                    print('Returning to the Main Menu...\n')
                    break
                elif good_receive_back_to_main_menu == "n":
                    print('Returning to the Good Receive Menu...\n')
                    continue
            elif good_receive_menu_input == 7:
                exit_program = input('\nAre you sure you want to exit from program? (y/n): ').strip().lower()
                if exit_program == "y":
                    print('Thank you for using this program, Goodbye! 👋')
                    sys.exit()
                elif exit_program == "n":
                    print('Returning to The Good Receive Menu...\n')
                    continue
            else:
                print(f'There is no option number {good_receive_menu_input} on the Good Receive menu, Choose the number only on the menu!\n')
        continue
    
    elif main_menu_input == 4:
        exit_program = input('\nAre you sure you want to exit from program? (y/n): ')
        if exit_program == "y":
            print('Thank you for using this program, Goodbye! 👋')
            sys.exit()
        elif exit_program == "n":
            print('Returning to The Main Menu...\n')
            continue
    else :
        print(f'There is no option number {main_menu_input} on the menu, Choose the number only on the menu!\n ')
        continue