from pytirement import draw_down_table

def test_no_change():
    """no depletion of funds or interest after 10 months"""
    init_balance = 10000
    monthly_interest = 0
    months = 10
    monthly_draw = 0
    final_balance = (
        draw_down_table(init_balance, months, monthly_interest, monthly_draw)
        .tail(1)["Remaining funds"]
        .values[0]
    )
    assert final_balance == init_balance


def test_full_draw_no_interest():
    """full drawdown after 10 months without accrued interest"""
    init_balance = 10000
    monthly_interest = 0
    months = 10
    monthly_draw = 1000
    final_balance = (
        draw_down_table(init_balance, months, monthly_interest, monthly_draw)
        .tail(1)["Remaining funds"]
        .values[0]
    )
    assert final_balance == 0


def test_interest_only():
    """Accrue 100% monthly interest - no drawdown"""
    init_balance = 10000
    monthly_interest = 1
    months = 10
    monthly_draw = 0
    final_balance = (
        draw_down_table(init_balance, months, monthly_interest, monthly_draw)
        .tail(1)["Remaining funds"]
        .values[0]
    )
    assert final_balance == init_balance * (1 + monthly_interest) ** months == 10240000


##add some error handling checks like zero inital balance, etc.