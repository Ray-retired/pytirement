# __init__.py

# Allows direct import like:
# from pytirement import draw_down_table
from .functions import draw_down_final, draw_down_table, scenario_plot

__all__ = ["draw_down_final", "draw_down_table", "scenario_plot"]
