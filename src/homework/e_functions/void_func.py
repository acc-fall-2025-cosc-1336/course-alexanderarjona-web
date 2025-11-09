from .value_return_functions import get_gross_pay, get_fica_tax, get_federal_tax

def display_payroll_check(hours, rate):
    """Display formatted payroll check information."""
    gross_pay = get_gross_pay(hours, rate)
    fica = get_fica_tax(gross_pay)
    federal = get_federal_tax(gross_pay)
    net_pay = gross_pay - (fica + federal)

    print(f"Gross Pay:      {gross_pay:>8.2f}")
    print(f"FICA:           {fica:>8.2f}")
    print(f"Federal Tax:    {federal:>8.2f}")
    print(f"Net Pay:        {net_pay:>8.2f}")
