from void_functions import display_payroll_check

def main():
    print("=== Payroll Check Generator ===")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    print()
    display_payroll_check(hours, rate)

if __name__ == "__main__":
    main()
