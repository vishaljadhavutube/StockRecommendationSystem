from app import create_app
from app.models.models import db, Stock

app = create_app()
with app.app_context():
    symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK"]
    names = ["Reliance", "TCS", "Infosys", "HDFC Bank", "ICICI Bank"]
    for sym, name in zip(symbols, names):
        db.session.add(Stock(symbol=sym, name=name))
    db.session.commit()
    print("✅ Stocks seeded.")