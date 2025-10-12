
FICA_RATE = 0.0765
FEDERAL_TAX_RATE = 0.08

def get_gross_pay(hours, rate):
    """Calculate gross pay, including overtime (over 40 hrs is 1.5x rate)."""
    if hours <= 40:
        gross_pay = hours * rate
    else:
        overtime_hours = hours - 40
        gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    return gross_pay


def get_fica_tax(gross_pay):
    """Calculate FICA tax using global rate."""
    return gross_pay * FICA_RATE


def get_federal_tax(gross_pay):
    """Calculate federal tax using global rate."""
    return gross_pay * FEDERAL_TAX_RATE
