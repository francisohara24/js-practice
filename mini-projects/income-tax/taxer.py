"""Module containing taxer function"""


def taxer(salary: float) -> (float, float):
    """Accepts gross salary and returns a 2-tuple containing total tax and net salary"""
    tax_rate = [0, 0.05, 0.10, 0.175, 0.25, 0.3]  # tax rate for each level
    tax_payable = [0, 5.5, 13.00, 525, 4098.75, 6000]  # maximum tax payable for each level
    amount = [365, 110, 130, 3000, 16395, 20000]  # maximum chargeable income for each level
    levels = [0, 1, 2, 3, 4, 5]  # all levels
    gross = salary  # copy of salary for calculations
    tax = 0.0  # tax amount to be paid
    net = 0  # net income to be paid

    for level in levels:
        # if remaining gross income greater than max chargeable income for level
        if gross > amount[level]:
            tax += tax_payable[level]   # increment tax by max tax payable for level
            gross -= amount[level]   # decrement gross salary by max chargeable income for level

        # if remaining gross income less than or equals max chargeable income for level
        else:
            tax += tax_rate[level] * gross  # increment tax according to tax rate for level
            net = salary - tax  # calculate net salary
            return tax, net   # return total tax and net salary

