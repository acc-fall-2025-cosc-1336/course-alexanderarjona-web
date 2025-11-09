from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("\nMenu:")
        print("1 - Show the list low/high values")
        print("2 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            numbers = []
            while True:
                try:
                    value = float(input("Enter a list value: "))
                    numbers.append(value)
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                # Ask to stop after at least 3 values
                if len(numbers) >= 3:
                    again = input("Do you want to enter another value? (y/n): ").lower()
                    if again != "y":
                        break

            print(f"\nLowest value: {get_lowest_list_value(numbers)}")
            print(f"Highest value: {get_highest_list_value(numbers)}")

        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
