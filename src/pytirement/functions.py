import logging

import matplotlib.pyplot as plt
import pandas as pd


def calculate_months_difference(start_month, end_month):
    """Calculate the number of months between two dates."""
    return (
        (end_month.year - start_month.year) * 12
        + (end_month.month - start_month.month)
        + 1
    )


def draw_down_final(
    start_month, end_month, starting_balance, annual_interest, monthly_withdrawal
):
    """Returns final balance and scenario info as a dictionary"""

    months_to_goal = calculate_months_difference(start_month, end_month)
    working_balance = starting_balance
    monthly_interest = annual_interest / 12

    for month in range(months_to_goal):
        # At the start of each month, deduct expected withdrawal
        working_balance -= monthly_withdrawal
        # Then accumulate interest on the remaining balance of funds
        working_balance += monthly_interest * working_balance

        logging.debug(f"Month {month + 1}: Balance = {working_balance:.2f}")

    return {
        "start_year": int(start_month.year),
        "start_month": int(start_month.month),
        "end_year": int(end_month.year),
        "end_month": int(end_month.month),
        "start_balance": round(starting_balance, 1),
        "monthly_draw": round(monthly_withdrawal, 1),
        "annual_interest": round(annual_interest, 3),
        "remaining_funds": round(working_balance, 1),
    }


def draw_down_table(
    start_month, end_month, starting_balance, annual_interest, monthly_withdrawal
):
    """Returns monthly balance as a dataframe"""

    months_to_goal = calculate_months_difference(start_month, end_month)
    working_balance = starting_balance
    monthly_interest = annual_interest / 12

    out_data = []

    for month in range(months_to_goal):
        working_balance -= monthly_withdrawal
        working_balance += monthly_interest * working_balance

        logging.debug(f"Month {month + 1}: Balance = {working_balance:.1f}")

        out_data.append([month + 1, round(working_balance, 1)])

    logging.info(pd.date_range(start=start_month, end=end_month, freq="MS"))

    df = pd.DataFrame(out_data, columns=["Month", "Remaining funds"])
    df["Month Label"] = pd.date_range(start=start_month, end=end_month, freq="MS")
    df.set_index("Month Label", inplace=True)

    return df


def scenario_plot(df):
    """
    Generates a 3D plot from a dataframe of scenarios
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Scatter plot
    ax.scatter(
        df["monthly_draw"],
        df["annual_interest"],
        df["remaining_funds"],
        c="blue",
        marker="o",
    )

    # Add labels
    ax.set_xlabel("monthly draw")
    ax.set_ylabel("annual interest")
    ax.set_zlabel("remaining funds")

    # Show plot
    plt.show()
