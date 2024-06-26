import matplotlib.pyplot as plt
import numpy as np


def monthly_compounding_monthly_fee():
    """
    Collects information about the interest/principal/length of time.
    Calculates monthly interest given monthly fees and bonus.
    Plots balance at end of year.
    :return:
    index = interest/principal/time
    """
    # APY in decimal
    APY: float = float(input("What is the APY? Don't add percent sign. ")) * 0.01

    # time in months
    time = int(input("Over how long (months) will you be collecting interest? "))
    fee = int(input("Are there any flat monthly fees? If no, enter 0. "))
    principal = int(input("How much principal will you start with, or how much will you deposit? "))
    bonus = int(input("If bonus, please enter. Otherwise, enter 0:"))
    acc_balance = [] # tracks monthly account balance
    interest_over_time = [] # tracks monthly interest
    x_month = [i for i in range(time)]
    total_interest = 0
    starting_principal = principal

    for month in range(time):
        monthly_interest = principal * APY / 12
        principal += monthly_interest
        principal -= fee
        total_interest += monthly_interest
        interest_over_time.append(monthly_interest)
        acc_balance.append(principal)
        # print(f"month {month} - interest: {monthly_interest:.2f}, balance: {principal:.2f}")
    final = round(principal, 2) + bonus

    # acc_balance and y_month are not global variables

    print(f"After {time} months, you will have ${final}. You will have earned {total_interest:.2f} in interest")

    # plot principal at the end of each year.
    plt.scatter(x_month[0::], interest_over_time[0::])
    plt.title(f'Monthly interest over {time} months')
    plt.show()

    # calculate index
    product_interest_index = total_interest / starting_principal / time * 100
    print(f"The index of this investment opportunity is {product_interest_index:.5f}")
    return product_interest_index



monthly_compounding_monthly_fee()
def index_comparison():
    """
    Calls compounding monthly fee twice
    Compares the two indices
    Provides a principal amount where the two products would be equal/comparable.
    :return:
    """
    pass
