# Trading Performance Dashboard

A production-style Python backend for recording trades and calculating portfolio performance and risk metrics.

## Why this project exists

A raw P&L number does not explain whether a trading process is repeatable or whether returns are hiding unacceptable risk. This project turns trade-level data into an auditable analytics service.

## Current capabilities

- REST API for creating and retrieving trades
- Long/short P&L calculation with transaction fees
- Portfolio analytics:
  - total P&L
  - win rate
  - average trade
  - profit factor
  - maximum drawdown
  - volatility
- SQLAlchemy persistence
- SQLite for zero-config local development
- PostgreSQL-ready configuration through `DATABASE_URL`
- Input validation and structured error responses
- Unit and API integration tests with pytest
- Docker container
- GitHub Actions CI

## Tech stack

**Python 3.12 · Flask · SQLAlchemy · SQL · PostgreSQL/SQLite · pytest · Docker · GitHub Actions**

## Architecture

```text
Client
  |
  v
Flask REST API
  |
  +--> Trade validation + persistence --> SQLAlchemy --> PostgreSQL / SQLite
  |
  +--> Analytics engine --> P&L / win rate / drawdown / volatility
```

## API

### Health check

```http
GET /health
```

### Create a trade

```http
POST /api/trades
Content-Type: application/json

{
  "symbol": "AAPL",
  "strategy": "momentum",
  "side": "long",
  "quantity": 10,
  "entry_price": 100,
  "exit_price": 105,
  "fees": 2
}
```

### List trades

```http
GET /api/trades
```

### Portfolio analytics

```http
GET /api/analytics
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python app.py
```

Open `http://localhost:5000`.

## Run with Docker

```bash
docker build -t trading-performance-api .
docker run -p 5000:5000 trading-performance-api
```

## PostgreSQL

Copy `.env.example` and set:

```text
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/trading
```

The application falls back to SQLite when `DATABASE_URL` is not set.

## Engineering decisions

The analytics logic is kept separate from the web layer so it can be unit tested independently. The application-factory pattern allows isolated in-memory database tests. Database configuration is environment-driven so the same codebase can run locally with SQLite or against PostgreSQL.

## Roadmap

- pagination and filtering
- authentication
- richer time-series analytics
- asynchronous ingestion pipeline
- OpenAPI-first API version using FastAPI

## Author

Amien Kadir — Mechanical Engineering student and software engineering intern focused on Python backend engineering and fintech.
