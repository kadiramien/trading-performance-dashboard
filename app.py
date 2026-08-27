from __future__ import annotations

import os

from flask import Flask, jsonify, render_template, request

from analytics import performance_summary
from database import Trade, db


def create_app(database_url: str | None = None) -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        database_url
        or os.getenv("DATABASE_URL")
        or "sqlite:///trades.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.get("/api/trades")
    def list_trades():
        trades = Trade.query.order_by(Trade.created_at.desc()).all()
        return jsonify([trade.to_dict() for trade in trades])

    @app.post("/api/trades")
    def create_trade():
        payload = request.get_json(silent=True) or {}
        required = {"symbol", "side", "quantity", "entry_price", "exit_price"}
        missing = sorted(required - payload.keys())
        if missing:
            return {"error": f"Missing fields: {', '.join(missing)}"}, 400

        side = str(payload["side"]).lower()
        if side not in {"long", "short"}:
            return {"error": "side must be 'long' or 'short'"}, 400

        try:
            trade = Trade(
                symbol=str(payload["symbol"]).upper(),
                strategy=payload.get("strategy"),
                side=side,
                quantity=float(payload["quantity"]),
                entry_price=float(payload["entry_price"]),
                exit_price=float(payload["exit_price"]),
                fees=float(payload.get("fees", 0)),
            )
        except (TypeError, ValueError):
            return {"error": "Numeric trade fields must contain valid numbers"}, 400

        if trade.quantity <= 0:
            return {"error": "quantity must be positive"}, 400

        db.session.add(trade)
        db.session.commit()
        return trade.to_dict(), 201

    @app.get("/api/analytics")
    def analytics():
        trades = Trade.query.order_by(Trade.created_at.asc()).all()
        return performance_summary([trade.pnl for trade in trades])

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
