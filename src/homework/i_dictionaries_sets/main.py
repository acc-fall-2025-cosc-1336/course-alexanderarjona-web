from dictionary import add_inventory, remove_inventory_widget

def main():
    inventory = {}

    while True:
        print("\nInventory Menu")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter widget name: ")
            qty = int(input("Enter quantity: "))
            add_inventory(inventory, name, qty)
            print("Item added or updated.")

        elif choice == "2":
            name = input("Enter widget name to delete: ")
            print(remove_inventory_widget(inventory, name))

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
