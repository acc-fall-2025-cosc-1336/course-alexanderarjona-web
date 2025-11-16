from lists import get_p_distance_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:.5f}" for value in row))

def main():
    while True:
        print("1 - Get p distance matrix")
        print("2 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Enter DNA lists one per line.")
            print("Separate characters with spaces. Enter an empty line to finish.")

            lists = []
            while True:
                line = input("> ").strip()
                if line == "":
                    break
                lists.append(line.split())

            matrix = get_p_distance_matrix(lists)
            print("\nP-Distance Matrix:")
            print_matrix(matrix)
            print()

        elif choice == "2":
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
