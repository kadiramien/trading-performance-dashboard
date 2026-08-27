from __future__ import annotations

from math import sqrt
from statistics import mean, pstdev


def equity_curve(pnls: list[float]) -> list[float]:
    total = 0.0
    curve: list[float] = []
    for pnl in pnls:
        total += pnl
        curve.append(round(total, 2))
    return curve


def max_drawdown(pnls: list[float]) -> float:
    curve = equity_curve(pnls)
    if not curve:
        return 0.0

    peak = max(0.0, curve[0])
    worst = 0.0
    for value in curve:
        peak = max(peak, value)
        worst = min(worst, value - peak)
    return round(abs(worst), 2)


def performance_summary(pnls: list[float]) -> dict:
    if not pnls:
        return {
            "trade_count": 0,
            "total_pnl": 0.0,
            "win_rate": 0.0,
            "average_trade": 0.0,
            "profit_factor": 0.0,
            "max_drawdown": 0.0,
            "volatility": 0.0,
        }

    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p < 0]
    gross_profit = sum(wins)
    gross_loss = abs(sum(losses))

    return {
        "trade_count": len(pnls),
        "total_pnl": round(sum(pnls), 2),
        "win_rate": round((len(wins) / len(pnls)) * 100, 2),
        "average_trade": round(mean(pnls), 2),
        "profit_factor": round(gross_profit / gross_loss, 2) if gross_loss else 0.0,
        "max_drawdown": max_drawdown(pnls),
        "volatility": round(pstdev(pnls) * sqrt(len(pnls)), 2) if len(pnls) > 1 else 0.0,
    }
