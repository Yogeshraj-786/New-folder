import json

# Inventory dictionary to store item information
inventory = {}

# Function to add a new item to the inventory
def add_item():
    item_id = input("Enter Item ID: ")
    if item_id in inventory:
        print("Item already exists. Use update_stock to update quantity.")
        return
    name = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Unit: "))
    
    inventory[item_id] = {
        'name': name,
        'quantity': quantity,
        'price': price
    }
    print(f"Item '{name}' added successfully!")

# Function to update stock for an existing item
def update_stock():
    item_id = input("Enter Item ID to update: ")
    if item_id not in inventory:
        print("Item not found in inventory. Use add_item to add new items.")
        return
    new_quantity = int(input("Enter new quantity to add: "))
    inventory[item_id]['quantity'] += new_quantity
    print(f"Updated stock for '{inventory[item_id]['name']}'. New quantity: {inventory[item_id]['quantity']}")

# Function to view the current inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")
    print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price/Unit':<10}")
    print("-" * 50)
    for item_id, details in inventory.items():
        print(f"{item_id:<10} {details['name']:<20} {details['quantity']:<10} {details['price']:<10.2f}")

# Function to save inventory to a file
def save_inventory(filename="inventory.json"):
    with open(filename, 'w') as f:
        json.dump(inventory, f, indent=4)
    print("Inventory saved to file.")

# Function to load inventory from a file
def load_inventory(filename="inventory.json"):
    global inventory
    try:
        with open(filename, 'r') as f:
            inventory = json.load(f)
        print("Inventory loaded from file.")
    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")

# Main program loop
def main():
    load_inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Stock")
        print("3. View Inventory")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            update_stock()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            save_inventory()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
