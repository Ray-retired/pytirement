import logging

import matplotlib.pyplot as plt
import pandas as pd


def draw_down_final(
    start_month, end_month, starting_balance, annual_interest, monthly_withdrawal
):
    """Returns final balance and scenario info as a dictionary"""

    months_to_goal = (end_month.year - start_month.year) * 12 + (
        end_month.month - start_month.month
    )
    working_balance = starting_balance
    monthly_interest = annual_interest / 12

    for month in range(months_to_goal):
        working_balance = (
            working_balance - monthly_withdrawal + (monthly_interest * working_balance)
        )

        logging.debug(working_balance)

    return {
        "start_year": start_month.year,
        "start_month": start_month.month,
        "end_year": end_month.year,
        "end_month": end_month.month,
        "start_balance": starting_balance,
        "monthly_draw": monthly_withdrawal,
        "annual_interest": round(annual_interest, 3),
        "remaining_funds": round(working_balance, 2),
    }


def draw_down_table(
    start_month, end_month, starting_balance, annual_interest, monthly_withdrawal
):
    """Returns monthly balance as a dataframe"""

    months_to_goal = (end_month.year - start_month.year) * 12 + (
        end_month.month - start_month.month
    )
    working_balance = starting_balance
    months_to_go = months_to_goal
    monthly_interest = annual_interest / 12

    out_data = []

    for month in range(months_to_goal):
        working_balance = (
            working_balance - monthly_withdrawal + (monthly_interest * working_balance)
        )

        logging.debug(working_balance)

        months_to_go -= 1
        out_data.append([month + 1, months_to_go, round(working_balance, 2)])

    logging.info(pd.date_range(start=start_month, end=end_month, freq="MS"))

    df = pd.DataFrame(out_data, columns=["Month", "Months to go", "Remaining funds"])
    df["Month Label"] = pd.date_range(start=start_month, end=end_month, freq="MS")[1:]

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
