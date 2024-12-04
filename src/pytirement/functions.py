import logging
import pandas as pd

def draw_down_table(tbill_balance, months_to_65, tbill_interest, monthly_withdrawal):
    """Returns monthly t bill balance as a dataframe
    
        Parameters
        tbill_balance       float   Starting balance
        months_to_65        int     Number of months to goal date
        tbill_interest      float   Monthly interest rate, e.g., .04/12 (assumes fixed rate)
        monthly_widthdrawal int     Amount of monthly widthdrawal (assumes fixed draw)
    
    """

    working_balance = tbill_balance
    months_to_go = months_to_65
    out_data = []

    for month in range(months_to_65):
        working_balance = (
            working_balance - monthly_withdrawal + (tbill_interest * working_balance)
        )

        logging.debug(working_balance)

        months_to_go -= 1
        out_data.append([month + 1, months_to_go, round(working_balance, 2)])

    return pd.DataFrame(out_data, columns=["Month", "Months to go", "Remaining funds"])
