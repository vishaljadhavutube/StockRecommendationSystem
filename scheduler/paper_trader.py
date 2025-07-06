from app import create_app
from app.models.models import db, Recommendation, PaperTrade
from app.services.data_fetcher import get_stock_data
from datetime import date

app = create_app()
with app.app_context():
    for trade in PaperTrade.query.filter_by(status="OPEN").all():
        rec = Recommendation.query.get(trade.recommendation_id)
        df = get_stock_data(rec.stock.symbol)
        today_price = df.iloc[-1]['Close']
        if (date.today() - trade.buy_date).days >= rec.holding_days:
            trade.sell_price = today_price
            trade.sell_date = date.today()
            trade.pnl = today_price - trade.buy_price
            trade.status = "CLOSED"
            db.session.commit()
    for rec in Recommendation.query.filter_by(date=date.today()).all():
        if not PaperTrade.query.filter_by(recommendation_id=rec.id).first():
            new_trade = PaperTrade(recommendation_id=rec.id, buy_price=rec.entry_price, status="OPEN")
            db.session.add(new_trade)
            db.session.commit()