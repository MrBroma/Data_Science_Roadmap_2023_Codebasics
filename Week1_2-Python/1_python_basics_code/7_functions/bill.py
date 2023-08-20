# Write a function pay_bill which will take a list of expenses,
# percent commission, and a special offer amount

# 1. If you don’t pass percent_comission it should be always 9.8%

# 2. The Last argument special_offer_amount is not a required argument,
# you don’t need to pass it. Make it an optional parameter.

# 3. If you want to give a special offer to the user, then you have
# to pass the third argument special_offer_amount. If the user makes the
# purchase greater than special_offer_amount, then give him an extra commission
# of 1.2%.

# 4. Calculate the final payable price of the bill and return it
# from the function.

def pay_bill(expenses, percent_commission=0.098, offer_amount=None):
    # calculating the total bill amount
    total_bill_amount = 0
    for amount in expenses:
        total_bill_amount += amount

    # calculate extra commision percentage
    extra_commission = 0
    if offer_amount:
        if total_bill_amount >= offer_amount:
            extra_commission = 0.012
            print(f"Congratulations! You earned 1.2% extra commission.")

    # Calculate final payable amount
    commission_amount = total_bill_amount * (
                percent_commission + extra_commission)
    final_amount = total_bill_amount - commission_amount
    return final_amount


print(pay_bill([100, 145, 567, 322], 0.09, 800))