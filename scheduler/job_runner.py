from app import create_app
from app.models.models import db, Stock, Recommendation
from app.services.data_fetcher import get_stock_data
from app.services.strategy_engine import generate_signals
from datetime import date

app = create_app()
with app.app_context():
    for stock in Stock.query.all():
        df = get_stock_data(stock.symbol)
        signal = generate_signals(df)
        if signal:
            rec = Recommendation(stock_id=stock.id, **signal, date=date.today())
            db.session.add(rec)
            db.session.commit()
            print(f"Saved recommendation for {stock.symbol}")