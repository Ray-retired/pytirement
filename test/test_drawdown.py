from datetime import datetime

from pytirement import draw_down_final, draw_down_table


def test_no_change():
    """no depletion of funds or interest after 10 months"""
    start_month = datetime(2025, 2, 1)
    end_month = datetime(2025, 12, 1)
    init_balance = 10000
    annual_interest = 0
    monthly_draw = 0

    final_balance = (
        draw_down_table(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )
        .tail(1)["Remaining funds"]
        .values[0]
    )
    assert final_balance == init_balance == 10000

    assert (
        draw_down_final(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )["remaining_funds"]
        == init_balance
        == 10000
    )


def test_full_draw_no_interest():
    """drawdown after 10 months without accrued interest"""
    start_month = datetime(2025, 2, 1)
    end_month = datetime(2025, 12, 1)
    init_balance = 10000
    annual_interest = 0
    monthly_draw = 1000

    final_balance = (
        draw_down_table(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )
        .tail(1)["Remaining funds"]
        .values[0]
    )
    assert final_balance == 0

    assert (
        draw_down_final(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )["remaining_funds"]
        == 0
    )


def test_interest_only():
    """100% monthly interest - no drawdown"""
    start_month = datetime(2025, 2, 1)
    end_month = datetime(2025, 12, 1)
    init_balance = 10000
    annual_interest = 12
    monthly_draw = 0

    final_balance = (
        draw_down_table(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )
        .tail(1)["Remaining funds"]
        .values[0]
    )
    assert (
        final_balance == init_balance * (1 + (annual_interest / 12)) ** 10 == 10240000
    )  # 10 months

    assert (
        draw_down_final(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )["remaining_funds"]
        == 10240000
    )
