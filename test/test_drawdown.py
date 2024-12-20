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
    end_month = datetime(2025, 11, 1)
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
    end_month = datetime(2025, 11, 1)
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


def test_first_month():
    """Hand calculate first month balance in drawdown table"""
    start_month = datetime(2025, 2, 1)
    end_month = datetime(2028, 6, 1)
    init_balance = 410000
    annual_interest = 0.04
    monthly_draw = 7500

    first_month_balance = (
        draw_down_table(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )
        .head(1)["Remaining funds"]
        .values[0]
    )

    assert first_month_balance == round(
        (init_balance - monthly_draw)
        + (annual_interest / 12 * (init_balance - monthly_draw)),
        1,
    )


def test_last_month():
    """draw_down_final result should match last row in draw down table"""
    start_month = datetime(2025, 2, 1)
    end_month = datetime(2028, 6, 1)
    init_balance = 410000
    annual_interest = 0.04
    monthly_draw = 7500

    last_month_balance = (
        draw_down_table(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )
        .tail(1)["Remaining funds"]
        .values[0]
    )

    assert (
        last_month_balance
        == draw_down_final(
            start_month, end_month, init_balance, annual_interest, monthly_draw
        )["remaining_funds"]
    )
