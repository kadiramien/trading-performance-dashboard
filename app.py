from flask import Flask, render_template, request, redirect
from database import db, Trade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trades.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    trades = Trade.query.all()
    total_profit = sum(t.profit for t in trades)
    return render_template('index.html', trades=trades, total_profit=total_profit)

@app.route('/add', methods=['POST'])
def add_trade():
    symbol = request.form['symbol']
    profit = float(request.form['profit'])
    trade = Trade(symbol=symbol, profit=profit)
    db.session.add(trade)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

