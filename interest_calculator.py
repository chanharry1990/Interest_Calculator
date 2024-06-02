import matplotlib.pyplot as plt
import numpy as np


def monthly_compounding_monthly_fee():
    # APY in decimal
    APY: float = float(input("What is the APY? Don't add percent sign. ")) * 0.01

    # time in months
    time = int(input("Over how long (months) will you be collecting interest? "))
    fee = int(input("Are there any flat monthly fees? If no, enter 0. "))
    principal = int(input("How much principal/deposit will you start with? "))
    bonus = int(input("If bonus, please enter. Otherwise, enter 0:"))
    acc_balance = []
    x_month = [i for i in range(time)]
    total_interest = 0

    for month in range(time):
        monthly_interest = principal * APY / 12
        principal += monthly_interest
        principal -= fee
        total_interest += monthly_interest
        acc_balance.append(principal)
        print(f"month {month} - interest: {monthly_interest:.2f}, balance: {principal:.2f}")
    final = round(principal, 2) + bonus

    # acc_balance and y_month are not global variables

    print(f"After {time} months, you will have ${final}. You will have earned {total_interest:.2f}")
    plt.scatter(x_month, acc_balance)
    plt.title(f'Account balance over {time} months')
    plt.show()


monthly_compounding_monthly_fee()
