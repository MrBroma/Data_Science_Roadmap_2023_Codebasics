def find_total(expenses):
    """
    This function take expenses list as an input
    and return a total sum of that list
    :param expenses: expenses
    :return: total expense
    """
    total_expense = 0
    for expense in expenses:
        total_expense += expense
    return total_expense


expenses_sergey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

total_expense = find_total(expenses_sergey)

print("Sergey's total expense: ", total_expense)

total_expense = find_total(expenses_sundar)

print("Sundar's total expense: ", total_expense)

print(help(find_total))