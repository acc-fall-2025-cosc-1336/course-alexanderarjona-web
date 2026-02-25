from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def main():
    option = int(input("Enter number of options: "))
    total = int(input("Enter total: "))

    ratio = get_options_ratio(option, total)
    rating = get_faculty_rating(ratio)

    print(f"Faculty rating: {rating}")

if __name__ == "__main__":
    main()
