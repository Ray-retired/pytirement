# pytirement

This repo allows you to perform basic retirement calculations and plots.

The primary purpose is to estimate funds remaining after a period of depletion (drawdown).

Two functions are available for estimating funds remaining:

- draw_down_final(): estimates the funds remaining after the last month of the drawdown period.
- draw_down_table(): generates a dataframe of estimated funds remaining at the end of each month.

Both functions take the following inputs:

- Start and end date (month of year)
- Starting balance
- Monthly withdrawal (assumed fixed)
- Annual interest or return (assumed fixed)

In addition, scenario_plot() generates a 3D plot of remaining funds by monthly withdrawal and annual interest rate. The plot is generated from a dataframe of scenarios defined with draw_down_final(). 

See the demo folder for Jupyter Notebook examples.