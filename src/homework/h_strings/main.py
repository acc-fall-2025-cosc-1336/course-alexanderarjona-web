#def main():
    while True:
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")
            print("Hamming Distance:", get_hamming_distance(dna1, dna2))

        elif choice == "2":
            dna = input("Enter DNA string: ")
            print("DNA Complement:", get_dna_complement(dna))

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
