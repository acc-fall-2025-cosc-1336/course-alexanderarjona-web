#

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def menu():
    while True:
        print("\nHomework 4 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            num = int(input("Enter number (1-9): "))
            while num <= 0 or num >= 10:
                num = int(input("Invalid. Enter number (1-9): "))
            print(get_factorial(num))

        elif choice == "2":
            num = int(input("Enter number (1-99): "))
            while num <= 0 or num >= 100:
                num = int(input("Invalid. Enter number (1-99): "))
            print(sum_odd_numbers(num))

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
