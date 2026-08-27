from analytics import equity_curve, max_drawdown, performance_summary


def test_equity_curve():
    assert equity_curve([100, -40, 20]) == [100.0, 60.0, 80.0]


def test_max_drawdown():
    assert max_drawdown([100, -40, -80, 60]) == 120.0


def test_performance_summary():
    summary = performance_summary([100, -50, 25])
    assert summary["trade_count"] == 3
    assert summary["total_pnl"] == 75
    assert summary["win_rate"] == 66.67
    assert summary["profit_factor"] == 2.5
