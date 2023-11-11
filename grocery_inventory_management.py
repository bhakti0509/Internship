# Grocery Store Inventory Management System

# Initialize empty inventory
inventory = []

#add new item to the inventory
def add_item():
    name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per unit: "))
    item = {"name": name, "quantity": quantity, "price": price}
    inventory.append(item)
    print(f"{name} added to the inventory.")

#update existing item's quantity
def update_quantity():
    name = input("Enter the item name to update quantity: ")
    for item in inventory:
        if item["name"] == name:
            new_quantity = int(input("Enter the new quantity: "))
            item["quantity"] = new_quantity
            print(f"Quantity of {name} updated to {new_quantity}.")
            return
    print(f"Item {name} not found in the inventory.")

#view the current inventory
def view_inventory():
    print("\nCurrent Inventory:")
    print("-------------------")
    for item in inventory:
        print(f"Item: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")
    print("-------------------")

#remove items from the inventory
def remove_item():
    name = input("Enter the item name to remove: ")
    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            print(f"{name} removed from the inventory.")
            return
    print(f"Item {name} not found in the inventory.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add new item to inventory")
    print("2. Update item quantity")
    print("3. View current inventory")
    print("4. Remove item from inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

