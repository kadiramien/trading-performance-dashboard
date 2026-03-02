# trading-performance-dashboard
Python-based trading P&L and performance analytics dashboard. Tracks trade-level returns, calculates cumulative performance, and analyses risk metrics such as drawdowns and volatility. Designed to understand performance drivers and improve decision-making.
# Trading Performance Dashboard (P&L Tracker)

A Python-based performance analytics dashboard built to track trade-level P&L, monitor cumulative returns, and surface key risk metrics (e.g., drawdowns, volatility) to understand **what is driving performance** over time.

This project was built to make trading results auditable and analyzable — not just a spreadsheet of wins/losses.

---

## What it does

- **Trade capture**: store trade entries (date, instrument, direction, size, entry/exit, P&L, notes)
- **Performance tracking**: equity curve, cumulative P&L, rolling returns
- **Risk analytics**:
  - Maximum drawdown + drawdown curve
  - Volatility / dispersion of returns
  - Win rate, avg win / avg loss
  - Profit factor (gross profit / gross loss)
  - Expectancy (avg return per trade)
- **Breakdowns**:
  - By instrument / asset
  - By strategy tag (if used)
  - By time (day/week/month)
- **Real-time dashboard views**: summary KPIs + charts for quick review

---

## Why I built it

Trading performance can look “good” while hiding risk (e.g., one lucky streak, hidden concentration, rising drawdowns).
This dashboard was built to answer practical questions like:

- **Am I actually profitable, or just volatile?**
- **What is my maximum drawdown and how often does it occur?**
- **Are returns driven by a single instrument or a repeatable edge?**
- **Is performance improving or degrading over time?**

---

## Tech stack

- **Backend:** Python (Flask)
- **Database:** SQL (SQLite or Postgres-style setup depending on config)
- **Frontend:** HTML/CSS + dashboard templates (or lightweight JS depending on build)
- **Charts:** (add library name if you used one: Plotly / Chart.js / Matplotlib)

---

## Project structure (example)
