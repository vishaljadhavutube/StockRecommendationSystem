from app import db
from datetime import date

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(100))

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    entry_price = db.Column(db.Float)
    target_price = db.Column(db.Float)
    holding_days = db.Column(db.Integer)
    confidence_score = db.Column(db.Float)
    date = db.Column(db.Date, default=date.today)
    stock = db.relationship('Stock')

class PaperTrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recommendation_id = db.Column(db.Integer, db.ForeignKey('recommendation.id'))
    buy_price = db.Column(db.Float)
    sell_price = db.Column(db.Float, nullable=True)
    buy_date = db.Column(db.Date, default=date.today)
    sell_date = db.Column(db.Date, nullable=True)
    pnl = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(10), default="OPEN")